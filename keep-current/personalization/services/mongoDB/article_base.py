#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
an implementation of connecting to the MongoDB 
using: https://api.mongodb.com/python/current/

"""
from personalization.services.db_article import DbArticleBase
from pymongo import MongoClient

class MongoDB (DbArticleBase):
    
    def __init__(self, *args, **kwargs):
        connection_string = 'mongodb://....'
        client = MongoClient(connection_string)
        client.close()
