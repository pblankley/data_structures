#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May  6 21:27:42 2017

@author: paulblankley
"""

## Make a heap

def satisfyheap(array, i, heapsize):
    l = 2*i+1
    r = 2*i+2
    if l <= heapsize and array[l] > array[i]:
        largest = l
    else:
        largest = i
    if r <= heapsize and array[r] > array[largest]:
        largest = r
    if largest != i:
        temp = array[i]
        array[i] = array[largest]
        array[largest] = temp
        satisfyheap(array, largest, heapsize)
        
def buildheap(a):
    length = len(a)
    for i in range(length/2, -1, -1):
        satisfyheap(a, i, length-1)
        
def heapsort(a):
    buildheap(a)
    heapsize = len(a) - 1
    for i in range(heapsize, -1, -1):
        temp = a[0]
        a[0] = a[i]
        a[i] = temp
        i -= 1
        satisfyheap(a, 0, i)           
    return a

       
## Code to run
a = [4,6,7,2,10,1]
print(a)

a = heapsort(a)   
print(a) 
    