from datetime import datetime
from datetime import timedelta
import os
import psutil
import threading

try:
    import ZPublisherEventsBackport  # noqa
except ImportError:
    pass


def initialize(context):
    from zodbstats import patchObjectReader
    patchObjectReader()

    try:
        import collective.stats.transchain  # noqa
    except ImportError:
        pass


process = psutil.Process(os.getpid())
zero = timedelta(0)


def init_stats():

    setattr(STATS, 'stats', {
        'time-start': datetime.now(),
        'time-after-traverse': zero,
        'time-before-commit': zero,
        'time-end': zero,
        'transchain': zero,
        'memory': process.memory_info(),
        'modified': 0,
        'zodb-loads': [],
        'zodb-cached': [],
        'zodb-uncached': [],
    })

STATS = threading.local()
