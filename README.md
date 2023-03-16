# Hacker News Cralwer

A web crawler for the [Hacker News website](https://news.ycombinator.com/).

## Install

Clone this project and use poetry to install dependencies:

```
poetry shell
poetry install 
```


## Usage 

### Tests

Run tests with:

```
poetry run pytest
```

Test coverage can also be checked with:

```
poetry run pytest --cov=app
```

<details>
<summary>Test coverage output</summary>
  
```
---------- coverage: platform linux, python 3.8.10-final-0 -----------
Name                                                 Stmts   Miss  Cover
------------------------------------------------------------------------
app/__init__.py                                          0      0   100%
app/controller.py                                       23      1    96%
app/crawler/__init__.py                                 10      0   100%
app/crawler/application/__init__.py                      0      0   100%
app/crawler/application/entry_crawling.py                9      0   100%
app/crawler/application/entry_filtering.py              14      0   100%
app/crawler/domain/__init__.py                           0      0   100%
app/crawler/domain/crawler.py                            3      1    67%
app/crawler/domain/entry.py                             26      0   100%
app/crawler/domain/filter.py                            13      0   100%
app/crawler/domain/repository.py                         5      2    60%
app/crawler/infrastructure/__init__.py                   0      0   100%
app/crawler/infrastructure/crawler_hacker_news.py       24      0   100%
app/crawler/infrastructure/filter_functions.py           9      0   100%
app/crawler/infrastructure/in_memory_repository.py      10      0   100%
------------------------------------------------------------------------
TOTAL                                                  146      4    97%
```
  
</details>


### API

To launch the news crawler API run:

```
cd app
poetry run flask --app app/controller.py run
```

You can then use `curl` to test the endpoints:

```
curl -X POST -H "Content-Type: application/json" http://127.0.0.1:5000/crawl  
curl -X GET -H "Content-Type: application/json" http://127.0.0.1:5000/filter/more_than_five
curl -X GET -H "Content-Type: application/json" http://127.0.0.1:5000/filter/less_than_or_five
```
