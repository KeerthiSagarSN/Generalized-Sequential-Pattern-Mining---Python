# -*- coding: utf-8 -*-
"""
Created on Sun Aug 06 14:02:01 2017

@author: Keerthi
"""

import Crypto.Hash.SHA

class Node:
    def __init__ (self, parent=None, contents="", children=[]):
        self.valid = False
        self.hash = False
        self.contents = contents
        self.children = children


    def append_child (self, child):
        self.children.append(child)

        self.invalidate()

    def invalidate (self):
        self.valid = False
        if self.parent:
            self.parent.invalidate()

    def gethash (self):
        if self.valid:
            return self.hash

        digester = crypto.hash.SHA.new()

        digester.update(self.contents)

        if self.children:
            for child in self.children:
                digester.update(child.gethash())
            self.hash = "1"+digester.hexdigest()
        else:
            self.hash = "0"+digester.hexdigest()

        return self.hash

    def setcontents (self):
        self.valid = False
        return self.contents
     