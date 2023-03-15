from app.crawler.domain.filter import Filter
from app.crawler.domain.entry import Entry
import re
import pytest


def filter_function(entry):
    title = entry.to_dict()['title']
    words = re.findall(r'\w+', title)
    return len(words) > 10

config = {
    'title': 'This is an entry title with more than ten words in it',
    'order': '1',
    'comments': '10',
    'points': '10'
}

entry = Entry(**config)

def test_filter_is_applied():
    filter = Filter(filter_function)
    filter.apply([entry]) == True