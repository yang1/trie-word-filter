#!/usr/bin/env python3
# -*- coding:utf-8 -*-


class Node:
    def __init__(self):
        self.value = None
        self.children = {}  # children is of type {char, Node}


class Trie:
    def __init__(self):
        self.root = Node()

    def load(self, file):
        with open(file, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                self.insert(line.strip('\n'))

    def insert(self, key):
        node = self.root
        for char in key:
            if char not in node.children:
                child = Node()
                node.children[char] = child
                node = child
            else:
                node = node.children[char]
        node.value = key

    def search(self, key):
        node = self.root
        for char in key:
            if char not in node.children:
                return node.value
            else:
                node = node.children[char]
        return node.value

    def search_all(self, key):
        result = []

        for i in range(len(key)):
            filter_word = self.search(key[i:])
            if filter_word:
                result.append(filter_word)

        return list(set(result))
