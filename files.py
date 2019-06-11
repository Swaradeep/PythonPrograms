# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 13:59:25 2019

@author: kon-boot
"""

#reading the data from existing file
file1 = open("file1.txt", "w+")
file1.write("This is sample data")
file1.close()

file2 = open("file1.txt", "r")
file3 = open("file2.txt", "w+")

#writing data from file2 to file3
file3.write(file2.read())
print(file3.read())
file2.close()
file3.close()

#writing user data into file2
file4 = open("file2.txt", "a+")
file4.write(" with the message: " + input("Enter some message:"))
file4.close()

#reading total data
file5 = open("file2.txt", "r")
print(file5.read())
file5.close()