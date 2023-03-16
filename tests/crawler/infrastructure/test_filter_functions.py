from app.crawler.infrastructure.filter_functions import (
    more_than_five_words,
    less_than_or_five_words,
)
from app.crawler.domain.entry import Entry
import pytest


six_words_entry = Entry("This is a six word entry", "1", "1", "1")
four_words_entry = Entry("This is an entry", "1", "1", "1")


def test_six_words_entry_passes_more_than_five_words_filter():
    assert more_than_five_words(six_words_entry) == True


def test_six_words_entry_does_not_pass_less_than_or_five_words_filter():
    assert less_than_or_five_words(six_words_entry) == False


def test_four_words_entry_does_not_pass_more_than_five_words_filter():
    assert more_than_five_words(four_words_entry) == False


def test_four_words_entry_passes_less_than_or_five_words_filter():
    assert less_than_or_five_words(four_words_entry) == True
