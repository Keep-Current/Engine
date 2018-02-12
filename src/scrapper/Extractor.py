import datetime;
import urllib.request
from logzero import logger
from bs4 import BeautifulSoup

class TextExtractor()
    
    def __init__(self, url):
        self.initTime = datetime.datetime.now().timestamp()
        self.url = url

    def parseUrl(self, url):        
        with urllib.request.urlopen(url) as response:
          html = response.read()
          self.soup = BeautifulSoup(html)

    def __exit__(self):
        self.endTime = datetime.datetime.now().timestamp()
        logger.info(self.initTime - self.endTime)
