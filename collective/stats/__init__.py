import threading

try:
    import ZPublisherEventsBackport
except ImportError:
    pass


def initialize(context):
    from zodbstats import patchObjectReader
    patchObjectReader()


STATS = threading.local()
