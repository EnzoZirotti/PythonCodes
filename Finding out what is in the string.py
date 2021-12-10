# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 09:59:43 2021

@author: PCC5
"""

words = str(input("Enter a Letter: "))
numbers = False
if not words.isdigit():
    for character in words:
        if character.isdigit():
            print("Contains Letters and Digits.")
            numbers = True
            break
if not words.isdigit() and words.islower() and not words.endswith(".") and not numbers:
    print("Contains only letters.")
    print("Contains only lower case letters.")
elif not words.isdigit() and words.islower() and words.endswith(".") and not numbers:
    print("Contains only letters.")
    print("Contains only lower case letters.")
    print("Ends with period.")
elif not words.isdigit() and words.isupper() and not words.endswith(".") and not numbers:
    print("Contains only letters.")
    print("Contains only upper letters.")
elif not words.isdigit() and words.isupper() and words.endswith(".") and not numbers:
    print("Contains only letters.")
    print("Contains only upper letters.")
    print("Ends with period.")
elif words.isdigit():
    print("Contains only digits.")
elif words[0].isupper():
    print("Starts with an uppercase")