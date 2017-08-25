#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask, request

import json

import my_trie

from functools import lru_cache

import time

app = Flask(__name__)

@lru_cache()
def get_trie():
    trie = my_trie.Trie()

    trie.insert('王')
    trie.insert('玉鹏')
    trie.insert('鹏')
    trie.insert('meet')
    trie.insert('you')
    # trie.display()

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
        filter_word = trie.search(content[i:])
        print(content[i:])
        if filter_word:
            result.append(filter_word)
    e = time.time()

    print(e-s)

    return json.dumps(list(set(result)))


if __name__ == '__main__':
    app.debug = True
    app.run()




