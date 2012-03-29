"""

$Id:  2007-12-12 12:27:02Z fafhrd $
"""
import os, psutil
import logging
import threading
from datetime import datetime, timedelta
from zope import component
from collective.stats import STATS
import ZPublisher.interfaces

logger = logging.getLogger('collective.stats')

process = psutil.Process(os.getpid())

zero = timedelta(0)


@component.adapter(ZPublisher.interfaces.IPubStart)
def pubStartHandler(ev):
    STATS.stats = {
        'time-start': datetime.now(),
        'time-after-traverse': zero,
        'time-before-commit': zero,
        'time-end': zero,
        'transchain': zero,
        'memory': process.get_memory_info(),
        'modified': 0,
        'zodb-loads': [],
        'zodb-cached': [],
        'zodb-uncached': [],
        }


@component.adapter(ZPublisher.interfaces.IPubAfterTraversal)
def pubAfterTraverseHandler(ev):
    STATS.stats['time-after-traverse'] = datetime.now()-STATS.stats['time-start']


@component.adapter(ZPublisher.interfaces.IPubBeforeCommit)
def pubBeforeCommitHandler(ev):
    STATS.stats['time-before-commit'] = datetime.now()-STATS.stats['time-start']

    try:
        ob = ev.request['PARENTS'][-1]
        conn = ob._p_jar
        STATS.stats['modified'] = len(conn._registered_objects)
    except:
        pass


@component.adapter(ZPublisher.interfaces.IPubSuccess)
def pubSucessHandler(ev):
    environ = ev.request.environ
    stats = STATS.stats
    stats['time-end'] = datetime.now() - stats['time-start']

    total = 0
    total_cached = 0
    t_total = timedelta()
    t_cached = timedelta()
    t_uncached = timedelta()

    for td in stats['zodb-cached']:
        total += 1
        total_cached += 1
        t_total = t_total + td
        t_cached = t_cached + td

    for td in stats['zodb-uncached']:
        total += 1
        t_total = t_total + td
        t_uncached = t_uncached + td

    loads = timedelta()
    for td in stats['zodb-loads']:
        loads = loads + td

    def printTD(td):
        s = td.seconds + td.microseconds/1000000.0
        return '%2.4f'%s

    rss1 = stats['memory'][0]/1024
    rss2 = process.get_memory_info()[0]/1024

    info = (
        printTD(stats['time-end']),
        printTD(stats['time-after-traverse']),
        printTD(stats['time-before-commit']),
        printTD(stats['transchain']),
        printTD(loads),
        total,
        total_cached,
        stats['modified'],
        environ['REQUEST_METHOD'],
        environ['PATH_INFO'],
        printTD(t_total), printTD(t_cached), printTD(t_uncached),
        rss1, rss2)

    logger.info(
        '| %s %s %s %s %s %0.4d %0.4d %0.4d '
        '| %s:%s | t: %s, t_c: %s, t_nc: %s '
        '| RSS: %s - %s'%info)

    ev.request.response.setHeader(
        'x-stats', '%s %s %s %s %s %0.4d %0.4d %0.4d'%info[:8])

    del STATS.stats
