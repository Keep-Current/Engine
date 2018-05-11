#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
an implementation of connecting to the MongoDB 
using: https://api.mongodb.com/python/current/

"""
from personalization.services.db_article import DbArticleBase
from pymongo import MongoClient
from personalization.common.settings import DBSettings

class Article (DbArticleBase):
    
    def __init__(self, *args, **kwargs):
        self.connection_string = DBSettings['connection']['port']


    def connect(self):
        client = MongoClient(self.connection_string)
        client.close()
