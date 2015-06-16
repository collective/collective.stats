""" plone.transformchain time """
from collective.stats import STATS
from collective.stats import init_stats
from datetime import datetime
from plone.transformchain import zpublisher

orig_applyTransform = zpublisher.applyTransform


def applyTransform(request, body=None):
    t1 = datetime.now()
    res = orig_applyTransform(request, body)

    try:
        if getattr(STATS, 'stats', None) is None:
            init_stats()
        STATS.stats['transchain'] = datetime.now() - t1
    except:
        pass

    return res


zpublisher.applyTransform = applyTransform
