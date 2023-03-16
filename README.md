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
