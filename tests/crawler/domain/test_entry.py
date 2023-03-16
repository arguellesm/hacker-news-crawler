from app.crawler.domain.entry import Entry
import pytest


def test_cant_create_titleless_entry():
    config = {"title": "", "order": "1", "comments": "10", "points": "10"}

    with pytest.raises(ValueError):
        Entry(**config)


def test_cant_create_orderless_entry():
    config = {"title": "Breaking news", "order": "z", "comments": "10", "points": "10"}

    with pytest.raises(TypeError):
        Entry(**config)


def test_cant_create_non_positive_order_entry():
    config = {"title": "Breaking news", "order": "-1", "comments": "10", "points": "10"}

    with pytest.raises(ValueError):
        Entry(**config)


def test_cant_create_non_numeric_comments_entry():
    config = {"title": "Breaking news", "order": "1", "comments": "z", "points": "10"}

    with pytest.raises(TypeError):
        Entry(**config)


def test_cant_create_non_numeric_points_entry():
    config = {"title": "Breaking news", "order": "1", "comments": "10", "points": "z"}

    with pytest.raises(TypeError):
        Entry(**config)


def test_to_dict_returns_dict():
    config = {"title": "Breaking news", "order": "1", "comments": "10", "points": "10"}

    assert Entry(**config).to_dict() == {
        "title": "Breaking news",
        "order": 1,
        "comments": 10,
        "points": 10,
    }
