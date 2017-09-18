#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 21:51:58 2017

@author: paulblankley
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def getData(self):
        return self.data
    def setData(self, data):
        self.data = data
    def getNext(self):
        return self.next
    def setNext(self, idx):
        self.next = idx

class llist:
    def __init__(self):
        self.head = None

    def add(self, data):
        temp = Node(data)
        temp.setNext(self.head)
        self.head = temp
        
    def isempty(self):
        return self.head == None
    
    def search(self, data):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == data:
                found = True
            else:
                current = current.getNext()
        return found
        
    def delete(self, data):
        previous = None
        current = self.head
        found = False
        while not found:
            if current.getData() == data:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())  
    
    def printl(self):
        current = self.head
        while current != None:
            print(current.getData())
            current = current.getNext()
        
        
listi = llist()
listi.add(6)
listi.add(3)
listi.add(991)
listi.add(300)
listi.printl()
print(listi.search(300))
listi.delete(3)
print(listi.search(3))
listi.printl()

        
                
        
    
    