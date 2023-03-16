from app.crawler.application.entry_crawling import EntryCrawling
from app.crawler.application.entry_filtering import EntryFiltering

from app.crawler.infrastructure.crawler_hacker_news import CrawlerHackerNews
from app.crawler.infrastructure.in_memory_repository import InMemoryRepository
from app.crawler.infrastructure.filter_functions import (
    more_than_five_words,
    less_than_or_five_words,
)

crawler_hacker_news = CrawlerHackerNews()
in_memory_repository = InMemoryRepository()
filter_functions = [more_than_five_words, less_than_or_five_words]

entry_crawling = EntryCrawling(crawler_hacker_news, in_memory_repository)
entry_filtering = EntryFiltering(filter_functions, in_memory_repository)
