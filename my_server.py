#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask, request
import json
from functools import lru_cache
import time
import pickle

app = Flask(__name__)


@lru_cache()
def get_trie():
    s = time.time()

    with open('my.tree', 'rb') as f:
        trie = pickle.load(f)
    e = time.time()

    print(e - s)
    return trie


@app.route('/', methods=['GET'])
def word_filter():
    content = request.args.get('content', None)

    trie = get_trie()

    # print(get_trie.cache_info())
    print(get_trie.cache_clear())

    result = []

    for i in range(len(content)):
        filter_word = trie.search(content[i:])
        if filter_word:
            result.append(filter_word)

    return json.dumps(list(set(result)))


if __name__ == '__main__':
    app.debug = True
    app.run()
