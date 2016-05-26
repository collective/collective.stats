from collective.stats import STATS
from collective.stats import init_stats
from collective.stats import process
from datetime import datetime
from datetime import timedelta
from zope import component
import ZPublisher.interfaces
import logging
import os
import statsd

logger = logging.getLogger('collective.stats')


@component.adapter(ZPublisher.interfaces.IPubStart)
def pubStartHandler(ev):
    init_stats()


@component.adapter(ZPublisher.interfaces.IPubAfterTraversal)
def pubAfterTraverseHandler(ev):
    if getattr(STATS, 'stats', None) is None:
        init_stats()
    STATS.stats['time-after-traverse'] = datetime.now() - STATS.stats['time-start']  # noqa


@component.adapter(ZPublisher.interfaces.IPubBeforeCommit)
def pubBeforeCommitHandler(ev):
    if getattr(STATS, 'stats', None) is None:
        init_stats()
    STATS.stats['time-before-commit'] = datetime.now() - STATS.stats['time-start']  # noqa

    try:
        ob = ev.request['PARENTS'][-1]
        conn = ob._p_jar
        STATS.stats['modified'] = len(conn._registered_objects)
    except:
        pass


@component.adapter(ZPublisher.interfaces.IPubSuccess)
def pubSucessHandler(ev):
    environ = ev.request.environ
    if getattr(STATS, 'stats', None) is None:
        init_stats()
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

    def printTD(td, string=True):
        s = td.seconds + td.microseconds / 1000000.0
        if string:
            return '%2.4f' % s
        else:
            return s

    rss1 = stats['memory'][0] / 1024
    rss2 = process.memory_info()[0] / 1024

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
        printTD(t_total),
        printTD(t_cached),
        printTD(t_uncached),
        rss1,
        rss2
    )

    if os.getenv("COLLECTIVE_STATS_DISABLE_LOG") != "1":
        logger.info(
            '| %s %s %s %s %s %0.4d %0.4d %0.4d '
            '| %s:%s | t: %s, t_c: %s, t_nc: %s '
            '| RSS: %s - %s' % info
        )

    if os.getenv("COLLECTIVE_STATS_DISABLE_RESPONSE_HEADER") != "1":
        ev.request.response.setHeader(
            'x-stats', '%s %s %s %s %s %0.4d %0.4d %0.4d' % info[:8]
        )

    if os.getenv('COLLECTIVE_STATS_STATSD_SERVER'):
        server = os.getenv('COLLECTIVE_STATS_STATSD_SERVER')
        port = os.getenv('COLLECTIVE_STATS_STATSD_SERVER_PORT', 8125)
        prefix = os.getenv('COLLECTIVE_STATS_STATSD_PREFIX', 'collective.stats')
        resource = environ['PATH_INFO'].replace('/', '.')
        method = environ['REQUEST_METHOD']
        logkey = '{prefix}.{key}.{method}'.format(
            prefix=prefix, method=method, resource=resource, key='{key}',
        )
        client = statsd.StatsClient(server, port)
        client.timing(
            logkey.format(key='time_end'),
            printTD(stats['time-end'], string=False)
        )
        client.timing(
            logkey.format(key='time_aftertraverse'),
            printTD(stats['time-after-traverse'], string=False)
        )
        client.timing(
            logkey.format(key='time_beforecommit'),
            printTD(stats['time-before-commit'], string=False)
        )
        client.timing(
            logkey.format(key='time_transchain'),
            printTD(stats['transchain'], string=False))
        client.timing(
            logkey.format(key='time_loads'),
            printTD(loads, string=False)
        )
        client.gauge(
            logkey.format(key='objects_total'),
            total)
        client.gauge(
            logkey.format(key='objects_total_cached'),
            total_cached)
        client.gauge(
            logkey.format(key='objects_modified'),
            stats['modified'])
        client.timer(
            logkey.format(key='objects_time_t_total'),
            printTD(t_total, string=False))
        client.timer(
            logkey.format(key='objects_time_t_cached'),
            printTD(t_cached, string=False))
        client.timer(
            logkey.format(key='objects_time_t_uncached'),
            printTD(t_uncached, string=False))
        client.gauge(
            logkey.format(key='memory_rss'),
            rss2 - rss1)

    del STATS.stats
