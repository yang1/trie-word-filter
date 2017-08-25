#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pickle

import my_trie

trie = my_trie.Trie()

words = []

with open('6.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        trie.insert(line.strip('\n'))


with open('my.tree', 'wb') as f:
    pickle.dump(trie, f)
