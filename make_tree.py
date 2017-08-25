#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import marisa_trie

words = []

with open('6.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        words.append(line.strip('\n'))

trie = marisa_trie.Trie(words)

trie.save('my_trie.marisa')