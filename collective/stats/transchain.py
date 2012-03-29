""" plone.transformchain time """
from datetime import datetime
from plone.transformchain import zpublisher
from collective.stats import STATS

orig_applyTransform = zpublisher.applyTransform


def applyTransform(request, body=None):
    t1 = datetime.now()
    res = orig_applyTransform(request, body)

    try:
        STATS.stats['transchain'] = datetime.now() - t1
    except:
        pass

    return res


zpublisher.applyTransform = applyTransform
