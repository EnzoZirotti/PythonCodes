# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 09:05:49 2021

@author: PCC5
"""

n = 10
a = 0
s = 0
num_list = list()
c = 0
av = 0
for _ in range(n):
    a = int(input("enter a number: "))
    num_list.append(a)
    c += 1
    s += a
    av = s/c
    
    
print("list of numbers: ", num_list)
print("you have entered the max count of numbers")
print("final sum:", s, "\nfinal aveg:",av)