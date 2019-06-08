# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 18:07:39 2019

@author: kon-boot
"""
mylist = []
myset = {}
def readNum():
    num = int(input("Enter a number: "))
    mylist.append(num)

def sum():    
    sum1 = 0
    sum2 = 0
    for i in mylist:
        sum1 += i
    myset = set(mylist)
    for i in myset:
        sum2 += i
    return sum1, sum2
n = int(input("Enter size: "))
for i in range(n):
    readNum()
listsum, setsum = sum()
print("Sum of all elements:", listsum,"\nSum of non-repeating elements:", setsum)