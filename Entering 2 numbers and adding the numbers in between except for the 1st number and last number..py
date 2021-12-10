# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 11:19:36 2021

@author: PCC5
"""

x = int(input("Please enter a number between 0 and 100: "))


sum = 0

y = int(input("please enter a number between 0 and 100: "))

while x < y:
    print(x)
    sum = sum + x
    x = x+1    


print("The sum is", sum)