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


STATS = threading.local()
