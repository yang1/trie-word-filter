#!/usr/bin/env python3
# -*- coding:utf-8 -*-


class Node:
    def __init__(self):
        self.value = None
        self.children = {}    # children is of type {char, Node}

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, key):      # key is of type string
        # key should be a low-case string, this must be checked here!
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
                pass
            else:
                node = node.children[char]
        return node.value

    def display_node(self, node):
        if (node.value != None):
            print(node.value)
        else:
            for char in node.children:
                self.display_node(node.children[char])
        return

    def display(self):
        self.display_node(self.root)