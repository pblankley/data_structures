#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 19:29:34 2017

@author: paulblankley
"""

# Trie Implementation

class Trie:
    def __init__(self):
        self.root = dict()
        
    def insert(self, *words):
        root = self.root
        for word in words:
            current_dict = root
            for letter in word:
                current_dict = current_dict.setdefault(letter, {})
            current_dict['_end_'] = '_end_'
        return root
    
    def search(self, word):
        current_dict = self.root
        for letter in word:
            if letter in current_dict:
                current_dict = current_dict[letter]
            else:
                return False
        else:
            if '_end_' in current_dict:
                return True
            else:
                return False
        
    def remove(self, word):
        current_dict = self.root
        for letter in word:
            if letter in current_dict:
                current_dict = current_dict[letter]
            else:
                return True
        if '_end_' in current_dict:
            del current_dict['_end_']
        else:
            return True
        
    def prinTrie(self):
        print(self.root)


trie = Trie()    
trie.insert('foo','bar','baz','barz')
trie.prinTrie()
trie.search('baz')
trie.search('food')
trie.search('fo')
trie.remove('baz')
trie.prinTrie()
trie.search('baz')
trie.insert('baz')
trie.search('baz')
trie.prinTrie()
