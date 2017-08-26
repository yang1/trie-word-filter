#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask, request
import json
import marisa_trie
from functools import lru_cache

app = Flask(__name__)


@lru_cache()
def get_trie():
    '''创建 Trie 树，添加敏感词至 Trie，并缓存'''

    words = []

    with open('words.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            words.append(line.strip('\n'))

    trie = marisa_trie.Trie(words)

    return trie


@app.route('/filter', methods=['GET', 'POST'])
def word_filter():
    '''提供 HTTP 过滤接口'''
    content = request.values.get('content', None)

    trie = get_trie()

    result = []

    for i in range(len(content)):
        filter_word = trie.prefixes(content[i:])
        if filter_word:
            result.extend(filter_word)

    return json.dumps(list(set(result)))


if __name__ == '__main__':
    # 启动时生成一次trie，并缓存
    get_trie()

    app.debug = True
    app.run()
