from ZODB import broken
from ZODB.Connection import Connection
from ZODB.broken import Broken
from ZODB.serialize import ObjectReader
from collective.stats import STATS
from collective.stats import init_stats
from datetime import datetime
from persistent import PickleCache

############
# ZODB Stats

has_new_ghost = hasattr(PickleCache, 'new_ghost')


def patchObjectReader():
    Connection.setstate = setstate
    ObjectReader.load_persistent = load_persistent

# [zoid, class name, from cache, time]


def load_persistent(self, oid, klass):
    # Quick instance reference.  We know all we need to know
    # to create the instance w/o hitting the db, so go for it!
    try:
        if getattr(STATS, 'stats', None) is None:
            init_stats()
        stats_cached = STATS.stats['zodb-cached']
        stats_uncached = STATS.stats['zodb-uncached']
    except:
        stats_cached = []
        stats_uncached = []

    t1 = datetime.now()

    obj = self._cache.get(oid, None)
    if obj is not None:
        stats_cached.append(datetime.now() - t1)
        return obj

    if isinstance(klass, tuple):
        klass = self._get_class(*klass)

    if issubclass(klass, Broken):
        # We got a broken class. We might need to make it
        # PersistentBroken
        if not issubclass(klass, broken.PersistentBroken):
            klass = broken.persistentBroken(klass)

    try:
        obj = klass.__new__(klass)
    except TypeError:
        # Couldn't create the instance.  Maybe there's more
        # current data in the object's actual record!
        stats_uncached.append(datetime.now() - t1)

        return self._conn.get(oid)

    if has_new_ghost:
        self._cache.new_ghost(oid, obj)
    else:
        obj._p_oid = oid
        obj._p_jar = self._conn
        obj._p_changed = None
        self._cache[oid] = obj

    stats_uncached.append(datetime.now() - t1)
    return obj


origSetstate = Connection.setstate


def setstate(self, obj):
    t1 = datetime.now()
    res = origSetstate(self, obj)
    try:
        STATS.stats['zodb-loads'].append(datetime.now() - t1)
    except:
        pass
    return res
