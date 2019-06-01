#! /usr/bin/env python
# # -*- coding: utf-8 -*-

x = 'spam'
y = 99
z = ['eggs']


sourceFile = open('python.txt', 'a')
print(x,y,z, sep=',',end='\n\t', file = sourceFile)
sourceFile.close()