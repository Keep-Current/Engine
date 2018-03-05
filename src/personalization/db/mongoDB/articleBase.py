# -*- coding: utf-8 -*-

"""
an implementation of connecting to the MongoDB 
using: https://api.mongodb.com/python/current/

"""

import personalization.db.db-article
from pymongo import MongoClient

class MongoDB (DbArticleBase):
    
    def __init__(self, *args, **kwargs):
        connection_string = 'mongodb://....'
        client = MongoClient(connection_string)
        client.close()
