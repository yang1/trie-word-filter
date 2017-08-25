#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask, request

import json

import marisa_trie

from functools import lru_cache

import time

app = Flask(__name__)

@lru_cache()
def get_trie():
    trie = marisa_trie.Trie()

    print('test')

    trie.load('my_trie.marisa')

    return trie


@app.route('/', methods=['GET'])
def word_filter():
    s = time.time()
    content = request.args.get('content', None)

    trie = get_trie()

    # print(get_trie.cache_info())
    # print(get_trie.cache_clear())

    result = []

    for i in range(len(content)):
        filter_word = trie.prefixes(content[i:])
        if filter_word:
            result.extend(filter_word)

    return json.dumps(list(set(result)))


if __name__ == '__main__':
    app.debug = True
    app.run()




