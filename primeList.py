# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

mylist = []

def readPrime():
    fact = 0
    num = int(input("Enter a prime number: "))
    for i in range(1, num):
        rem = int(num%i)
        if rem == 0:
            fact += 1
    if fact <= 2:
        mylist.append(num)
    else:
        print(num, "is not a prime number")

n = int(input("Enter size: "))
for i in range(n):
    readPrime()
print(mylist)