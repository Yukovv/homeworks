import requests


RANDOM_QOUTE_API_URL = "https://favqs.com/api/qotd"


def rand_quote_gen():
    res = requests.get(RANDOM_QOUTE_API_URL, params="json")
    data = res.json()
    return {data["quote"]["author"]: data["quote"]["body"]}