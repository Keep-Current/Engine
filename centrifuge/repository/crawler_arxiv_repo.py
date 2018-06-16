import urllib.request
import feedparser
import json

from centrifuge.domain import document as ad

class CrawlerArxivRepo:
    """
    This is a helper class to parse arxiv.org site.
    It uses the arxiv.org REST API to search for articles.

    based on karpathy's arxiv-sanity:
    https://github.com/karpathy/arxiv-sanity-preserver/blob/master/fetch_papers.py
    and arxiv example:
    https://arxiv.org/help/api/examples/python_arXiv_parsing_example.txt
    """
        
    # Base api query url
    base_url = 'https://keepcurrent-crawler.herokuapp.com/'

    def list(self, filters=None): 
        if not filters:
            return self.fetch_papers()

    def run_query(self):
        query = 'arxiv'
        with urllib.request.urlopen(self.base_url+query) as url:
            response = url.read()
        parsed_response = feedparser.parse(response)

        return parsed_response
    
    def fetch_papers(
            self
        ):
        """
        fetch results from our crawler
        """
        # num_added_total = 0
        parsed_response = self.run_query()                
        return parsed_response.entries

