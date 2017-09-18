#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 10:10:31 2017

@author: paulblankley
"""

# Sorting algorithms
print('Original Array:')
array = [14,2,5,13,11,86,56,35,74,35,462,1,352,1,4,-3,-11,88]
print(array,'',sep='\n')
# Heap Sort
import heapq
import copy
      
def heapsort(a):
    ar = copy.deepcopy(a)
    heapq.heapify(ar)
    out = []
    for i in range(len(ar)):
        out.append(heapq.heappop(ar))
        heapq.heapify(ar)          
    return out
   
## Code to run
print('HeapSort:')
hs_out = heapsort(array)   
print(hs_out, '' ,sep='\n') 

########################################################

# Quick Sort

def qsort(lst):
    if lst == []:
        return []
    else:
        pivot = lst[0]
        lesser = qsort([x for x in lst[1:] if x < pivot])
        greater = qsort([x for x in lst[1:] if x >= pivot])
        return lesser + [pivot] + greater

print('QuickSort:')
qs_out = qsort(array)
print(qs_out, '' ,sep='\n')

########################################################

# Merge Sort

def merge_sort(a):
    if len(a)<=1:
        return a
    left = []
    right = []
    for i,x in enumerate(a):
        if i < len(a)/2:
            left.append(x)
        else:
            right.append(x)
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def merge(ar1, ar2):
    res = []
    while ar1 != [] and ar2 != []:
        if ar1[0] < ar2[0]:
            res.append(ar1[0])
            ar1 = ar1[1:]
        else:
            res.append(ar2[0])
            ar2 = ar2[1:]
    while ar1 != []:
        res.append(ar1[0])
        ar1 = ar1[1:]
    while ar2 != []:
        res.append(ar2[0])
        ar2= ar2[1:]
    return res

print('Merge Sort:')
ms_out = merge_sort(array)
print(ms_out,'',sep='\n')

########################################################

# Insertion Sort

def insertion_sort(a):
    ar = copy.deepcopy(a)
    for i in range(1,len(ar)):
        key = ar[i]
        j = i-1
        while j>=0 and key<ar[j]:
            ar[j+1] = ar[j]
            j -=1
        ar[j+1] = key
    return ar

print('Insertion Sort:')
is_out = insertion_sort(array)
print(is_out,'',sep='\n')

########################################################

# Selection Sort  
def selection_sort(a):
    ar = copy.deepcopy(a)
    for i in range(len(ar)):
        min_idx = i
        for j in range(i,len(ar)):
            if ar[j] < ar[min_idx]:
                min_idx = j
        ar[i], ar[min_idx] = ar[min_idx],ar[i]
    return ar
 
print('Selection Sort:')
ss_out = selection_sort(array)
print(ss_out,'',sep='\n')

########################################################

# Bubble Sort    
   
def bubble_sort(a):
    ar = copy.deepcopy(a)
    for i in range(len(ar)):
        for j in range(len(ar)-i-1):
            if ar[j]>ar[j+1]:
                ar[j],ar[j+1] = ar[j+1],ar[j]
    return ar
        
print('Bubble Sort:')
bs_out = bubble_sort(array) 
print(bs_out,'',sep='\n')   
    
    
    
    
    
    
    
    
    
    
    