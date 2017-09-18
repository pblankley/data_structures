#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 15:05:09 2017

@author: paulblankley
"""

# BST

class tNode:
    def __init__(self, val, parent=None):
        self.val = val
        self.p = parent
        self.left = None
        self.right = None
        self.count = 1
    def findmin(self):
        current = self
        while current.left != None:
            current = current.left
        return current
    def replace_parent(self, node):
        if self.p:
            if self.p.left == self:
                self.p.left = node
            else:
                self.p.right = node
        if node:
            node.p = self.p
            
class bst:
    def __init__(self):
        self.root = None
        
    def insert(self, val):
        if self.root == None:
            self.root = tNode(val)
        else:
            return self.insert_(val, self.root) 
    def insert_(self, val, node):
        if val == node.val:
            node.count +=1
        elif val < node.val:
            if node.left:
                return self.insert_(val, node.left)
            else:
                node.left = tNode(val, node)
        else:
            if node.right:
                return self.insert_(val, node.right)
            else:
                node.right = tNode(val, node)
                
    def search(self, val):
        if self.root == None:
            return False
        else:
            return self.search_(val, self.root)     
    def search_(self, val, node):
        if node == None:
            return False
        elif val == node.val:
            return True
        elif val < node.val:
            return self.search_(val, node.left)
        else:
            return self.search_(val, node.right)

    def prin(self, in_order=True):
        if self.root == None:
            return 
        else:
            return self.prin_(in_order, self.root)    
    def prin_(self, in_order, node):
        if in_order:
            if node.left: self.prin_(in_order, node.left)
            print(node.val)
            if node.right: self.prin_(in_order, node.right)
        else:
            print(node.val)
            if node.left: self.prin_(in_order, node.left)
            if node.right: self.prin_(in_order, node.right)

    def delete(self, val):
        return self.delete_(val, self.root) 
    def delete_(self, val, node):
        if node == None:
            return
        elif val < node.val:
            return self.delete_(val, node.left)
        elif val > node.val: 
            return self.delete_(val, node.right)
        else:
            if node.right and node.left:
                successor = node.right.findmin()
                node.val = successor.val
                return self.delete_(successor.val, successor)
            elif node.right:
                node.replace_parent(node.right)
            elif node.left:
                node.replace_parent(node.left)
            else:
                node.replace_parent(None)
                
    def mirror(self):
        return self.mirror_(self.root)
    def mirror_(self, node):
        if not node:
            return None
        else:
            self.mirror_(node.right)
            self.mirror_(node.left)
            node.right, node.left = node.left, node.right        
        

               
tree  = bst()
tree.insert(33)
tree.insert(2)
tree.insert(9)
tree.insert(22)
tree.insert(90)
tree.insert(4)
tree.insert(16)
tree.prin()  

print('')
tree.prin()
tree.delete(22)
tree.delete(23)
print('')
tree.prin() 

print('')
tree.mirror()   
tree.prin()         