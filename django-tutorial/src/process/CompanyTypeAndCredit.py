# Author: LoanHuynh
# Date:
# Desc: this script calculate company factors for prediction

import src.dbconnect.ConnectionInformation as connInfo
# from elasticsearch import Elasticsearch
import elasticsearch
from elasticquery import ElasticQuery, Query
# from pyes import QueryStringQuery, TermQuery
# import  pyes as py

class CompanyInformation:
    def getCompanyTypeAndCreditByES(self, company_name):
        res = None
        try :
            es = elasticsearch.Elasticsearch([{'host': connInfo.esHost, 'port': 9200}])
            print (es.info)
            query = {"query": {
                                    "multi_match": {
                                        "query" : company_name,
                                        "fields": ["name"]
                                    }
                                }}
            result = es.search(body=query, index= 'vsprofile', doc_type= connInfo.es_type_company)
            # for hit in res['hits']['hits']:
            #     print hit['_source']['type']
            # for r in res:
            #     print r[0]

        except Exception as err:

            print err

        return res

    # def search(query):


# "query_string": {
#     "default_field": "name",
#     "query"        : "IBM"
# }