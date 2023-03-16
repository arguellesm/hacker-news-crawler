from app.crawler.application.entry_crawling import EntryCrawling
from app.crawler.domain.crawler import Crawler
from app.crawler.domain.repository import Repository
from app.crawler.domain.entry import Entry
import pytest


class DummyCrawler(Crawler):
    def get_entries(self):
        entries = []

        entries.append(
            Entry(title="Breaking News", order="2", comments="10", points="100")
        )

        entries.append(
            Entry(
                title="Even more Breaking News", order="1", comments="23", points="200"
            )
        )

        return entries


class DummyEmptyCrawler(Crawler):
    def get_entries(self):
        entries = []
        return entries


class DummyRepository(Repository):
    def __init__(self):
        self.entries = []

    def save_entries(self, entries):
        self.entries = entries

    def get_entries(self):
        return self.entries


def test_crawl():
    dummy_repository = DummyRepository()
    entry_crawling = EntryCrawling(crawler=DummyCrawler(), repository=dummy_repository)
    entry_crawling.crawl()

    assert dummy_repository.entries == [
        Entry(title="Breaking News", order="2", comments="10", points="100"),
        Entry(title="Even more Breaking News", order="1", comments="23", points="200"),
    ]


def test_crawl_with_empty_crawler():
    dummy_repository = DummyRepository()
    entry_crawling = EntryCrawling(
        crawler=DummyEmptyCrawler(), repository=dummy_repository
    )
    entry_crawling.crawl()

    assert dummy_repository.entries == []
