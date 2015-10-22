#!/usr/bin/env python

from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch([{'host':'aianalytics01.cern.ch', 'port':9200}])

# "jobid": 9,"step": "RAWtoESD","component":"InDetSiSpTrackFinder","domain": "InnerDetector","stage": "evt","n": 99,"cpu"  : 7432,"vmem" : 0,"malloc" : 18870

doc = {
    'jobid': 9,
    'step': 'RAWtoESD',
    "component":"InDetSiSpTrackFinder",
    "domain": "InnerDetector",
    "stage": "evt",
    "n": 99,
    "cpu"  : 7432,
    "vmem" : 0,
    "malloc" : 18870,
    'timestamp': datetime.now(),
}
res = es.index(index="pmbtest5", doc_type='alg', body=doc)
print(res['created'])