#!/usr/bin/python3
# -*- coding: utf-8 -*-
from abc import ABC


class DbArticleBase(ABC):
    """ 

    This is the abstract interface for communicating with the DB
    We begin with an implementation of MongoDB

    ToDo: decide if to use strict interface (list of arguments) or an object
    method, where the arguments are the object's properties and the functions
    scans the object and saves them in an internfal implementation


    Entities:
     Users
     Topics (Themes)
     Sources (URLs)              --> a list of trusted locations where to 
                                     crawl and look for content
     Sources-Locations              For the first version, store the xpath
                                    where the content is, for retrieval
     Processed Articles (Texts)

    Relations:
     - Sources are classified by one or more topics
     - Processed Articles should have a relation to the sources 
            (1 to 1? 1 to many? depends if we summarize multiple sources)
    """

    """

    Topics / Themes - every user can register to get notifications about a set of 
    preferred themes. 

        To Decide: should we support hierarchy of topics?

    """
    def get_topics(self):
        """
        Get a list of currently available topics/themes in the system
        """
        raise NotImplementedError

    def save_new_topic(self, topic):
        """
        Save a new topics/themes.
        """
        raise NotImplementedError

    def save_user_topics_relation(self, user_guid, topics):
        """
        Connect a list of preferred topics with the user
        """
        raise NotImplementedError

    """

    Sources, inputs and processed sources (after they have passed 
    the pipleline)
    
    """
    def save_source(self, url, topics):
        """
        adds a new source to the list of sources with its assigned 
        classification topic
        """
        raise NotImplementedError

    def save_processed_source(self, source_content):
        """
        source_content should be an object that contains the following:
        source_url: string
        topics: list[string]
        summary: list[string]
        """
        raise NotImplementedError
