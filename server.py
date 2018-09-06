#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask, request
import json
import marisa_trie
from functools import lru_cache
import logging as log

log.basicConfig(level=log.DEBUG, format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

app = Flask(__name__)

@lru_cache(5)
def get_trie():
    '''创建 Trie 树，添加敏感词至 Trie，并缓存'''

    words = []

    with open('words.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            words.append(line.strip('\n'))

    trie = marisa_trie.Trie(words)

    return trie


@app.route('/clear_cache')
def clear_cache():
    '''清空缓存接口'''
    log.debug('清空缓存')
    log.debug(get_trie.cache_info())
    get_trie.cache_clear()
    return json.dumps(get_trie.cache_info())


@app.route('/filter', methods=['GET', 'POST'])
def word_filter():
    '''提供 HTTP 过滤接口'''
    content = request.values.get('content', None)
    log.debug(content)
    trie = get_trie()
    result = []

    i = 0

    while True:

        log.debug(content[i:])
        filter_word = trie.prefixes(content[i:])

        if not content[i:]:
            break

        log.debug(filter_word)
        if filter_word:
            current_filter_word_max_len = len(sorted(filter_word, key=lambda k: len(k), reverse=True)[0])
            i = i + current_filter_word_max_len
            result.extend(filter_word)
        else:
            i = i + 1


    log.debug(get_trie.cache_info())
    log.debug(','.join(list(set(result))))
    return json.dumps(list(set(result)))


if __name__ == '__main__':
    app.debug = True
    app.run()
