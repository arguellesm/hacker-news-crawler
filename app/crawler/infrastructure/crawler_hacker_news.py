from app.crawler.domain.crawler import Crawler
from app.crawler.domain.entry import Entry
from bs4 import BeautifulSoup
import requests
import re


class CrawlerHackerNews(Crawler):
    """
    Represents a crawler for the Hacker News website.
    """

    def __init__(self):
        """Inits CrawlerHackerNews with a url to check."""
        self.url = 'https://news.ycombinator.com/'


    def get_entries(self,num_entries=30):
        """Retrieves a number of entries.
        
        Parameter
        ---------
        num_entries: int
            Number of entries willing to retrieve (default is 30).
        
        Returns
        -------
        entries: Dict list
            List containing all the entries as dictionaries.
        """

        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        raw_entries = soup.find_all('tr', class_='athing')[:num_entries]
        
        entries = []

        for tr in raw_entries:
            order = tr.find('span', class_='rank').text.strip('.')
            title = tr.find('span', class_= 'titleline').a.text

            subtext = tr.find_next_sibling('tr').find('td', class_='subtext')
            points = subtext.find('span', class_='score').text.replace('points','')
            
            comments = subtext.find_all('a')[-1].text
            if 'comments' in comments:
                comments = comments.replace('comments','')
            else:
                comments = 0

            entries.append(Entry(title=title, order=order, comments=comments, points=points))

        return entries