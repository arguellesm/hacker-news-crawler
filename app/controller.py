from app.crawler import entry_crawling, entry_filtering
from flask import Flask
import json
import requests


api = Flask(__name__)


@api.route('/crawl', methods = ['POST'])
def index():
    """Crawls entries."""

    entry_crawling.crawl()
    return json.dumps({'Status': 'OK'})
    

@api.route('/filter/more_than_five', methods = ['GET'])
def filter_more_than_five():
    """Applies filter to crawled entries."""

    res = entry_filtering.filter('more_than_five_words')
    return json.dumps(res, indent=4, ensure_ascii=False)


@api.route('/filter/less_than_or_five', methods = ['GET'])
def filter_less_than_or_five():
    """Applies filter to crawled entries."""

    res =  entry_filtering.filter('less_than_or_five_words')
    return json.dumps(res, indent=4, ensure_ascii=False)