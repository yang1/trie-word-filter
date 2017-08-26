#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask, request
import json
from functools import lru_cache
import my_trie

app = Flask(__name__)


@lru_cache()
def get_trie():
    trie = my_trie.Trie()
    trie.load('words.txt')
    return trie


@app.route('/', methods=['GET'])
def word_filter():
    content = request.args.get('content', None)

    trie = get_trie()

    return json.dumps(trie.search_all(content))


if __name__ == '__main__':
    get_trie()
    app.debug = True
    app.run()
