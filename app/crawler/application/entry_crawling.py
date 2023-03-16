from app.crawler.domain.crawler import Crawler
from app.crawler.domain.entry import Entry


class EntryCrawling:
    """
    Represents an entry crawling process.
    """

    def __init__(self, crawler, repository):
        """Init EntryCrawling with a crawler and a repository."""

        self.crawler = crawler
        self.repository = repository

    def crawl(self):
        """Crawls entries."""

        entries = self.crawler.get_entries()
        self.repository.save_entries(entries)
