import threading

try:
    import ZPublisherEventsBackport
except ImportError:
    pass


def initialize(context):
    from zodbstats import patchObjectReader
    patchObjectReader()

    try:
        import collective.stats.transchain
    except ImportError:
        pass


STATS = threading.local()
