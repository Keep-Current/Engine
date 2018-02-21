# -*- coding: utf-8 -*-
import datetime
from urllib import request
from logzero import logger
from bs4 import BeautifulSoup
from bs4 import UnicodeDammit

class HTMLExtractor():
    """
    The HTMLExtractor recieves an HTML based URL and extracts the Text out of it.

    It should examine the different blocks in it and outputs the blocks which
    contains text (as in pargraphs, and anything that is longer than a few words)
    In a way, it behaves as a small classifer.

    """

    def __init__(self, 
                 url = "", 
                 parser="", 
                 encoding="utf8"):

        self.initTime = datetime.datetime.now().timestamp()
        self.url = url
        self.parser = parser
        self.encoding = encoding

    def should_ignore(tag):
        return tag.lower() not in ['script', 'style']

    def get_content(self, url = ""):
        assert isinstance(url, basestring), "argument url must be a string"
        assert not (url and url.strip()), "argument url must not be empty"

        self.url = url

        with request.urlopen(self.url) as response:
          self.html = response.read().decode(self.encoding)

        return self

    def parse_html():
        assert not (self.html and self.html.strip()), \
               "URL HTML must not be empty"

        # ensuring to unicode
        self.html = UnicodeDammit(self.html)        
        self.html_soup = BeautifulSoup(html, self.parser)


    def parocess_content():
        assert not (self.html_soup and self.html_soup.strip()), \
               "HTMLSoup string must not be empty"

        strings = [string for string in self.html_soup.body.stripped_strings]


    def __exit__(self):
        self.endTime = datetime.datetime.now().timestamp()
        logger.info(self.initTime - self.endTime)

    def execute():


