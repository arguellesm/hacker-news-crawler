from app.crawler.application.entry_filtering import EntryFiltering
from app.crawler.domain.repository import Repository
from app.crawler.domain.entry import Entry
import pytest


class DummyRepository(Repository):
    def __init__(self):
        self.entries = []

    def save_entries(self, entries):
        self.entries = entries

    def get_entries(self):
        return self.entries


def dummy_filter_function(entry):
    return entry


def test_filters_entries():

    dummy_entries = [
        Entry(
            title='Breaking News',
            order='2',
            comments='10',
            points='100'
        ),
        Entry(
            title='Even more Breaking News',
            order='1',
            comments='23',
            points='200'
        )
    ]

    dummy_repository = DummyRepository()
    dummy_repository.save_entries(dummy_entries)

    entry_filtering = EntryFiltering(filter_functions=[dummy_filter_function], repository=dummy_repository)
    assert entry_filtering.filter() == [entry.to_dict() for entry in dummy_entries]