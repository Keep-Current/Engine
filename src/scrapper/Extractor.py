# -*- coding: utf-8 -*-
"""
The Extractor receives a URL and tries to estimate its type
(HTML, PDF, XML...)
"""

import datetime
from urllib import request
from logzero import logger
import HTMLExtractor

class Extractor():
    
    def __init__(self, parser="", url = ""):
        self.initTime = datetime.datetime.now().timestamp()
        self.url = url
        self.parser = parser

    def parseUrl(self, url):
        assert isinstance(url, basestring), "argument url must be a string"
        self.url = url

        with request.urlopen(self.url) as response:
          html = response.read().decode('utf8')
        
        self.soup = BeautifulSoup(html, self.parser)
        return self.soup.get_text()

    def __exit__(self):
        self.endTime = datetime.datetime.now().timestamp()
        logger.info(self.initTime - self.endTime)

    def execute():

