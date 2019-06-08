# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

mylist = []

def readNum():
    num = int(input("Enter a palindrome number: "))
    temp = num
    rev = 0
    while temp != 0:
        rem = temp % 10
        rev = rev*10 + rem
        temp = temp // 10
    if num == rev:
        mylist.append(num)
    else :
        print(num, "is not a palindrome")

n = int(input("Enter size: "))
for i in range(n):
    readNum()
print(set(mylist))