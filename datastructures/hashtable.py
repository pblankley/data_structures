#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 18:00:39 2017

@author: paulblankley
"""

# Hash Table 

class HashMap:
    def __init__(self):
        self.hashmap = [[] for i in range(256)]
        
    def insert(self,key, value):
        key_exists = False
        hashkey = hash(key) % len(self.hashmap)
        bucket = self.hashmap[hashkey]
        for i,kv in enumerate(bucket):
            k,v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
            bucket = ((key, value))
        else:
            bucket.append((key, value))
    
    def search(self, key):
        hashkey = hash(key) % len(self.hashmap)
        bucket = self.hashmap[hashkey]
        if bucket == [None]:
            return None
        for i,kv in enumerate(bucket):
            k,v = kv
            if key == k:
                return key
            raise KeyError
    
    def delete(self, key):
        hashkey = hash(key) % len(self.hashmap)
        bucket = self.hashmap[hashkey]
        for i,kv in enumerate(bucket):
            k, v = kv
            if key == k:
                idx = i
                break
        if idx != None:
            bucket[idx] = None
            return True
        else:
            return True
        
    def prinhm(self):
        for i in self.hashmap: 
            if i != []: 
                print(i)
             
data1 = ('80226','Lakewood, CO')
data2 = ('06770','Nagatuck, CT')  

hm = HashMap()
hm.insert(*data1)
hm.insert(*data2)
hm.prinhm()
print(hm.search('80226'))
print(hm.search('28117'))
hm.delete('06770')
print(hm.search('06770'))
print(hm.search('80226'))


     