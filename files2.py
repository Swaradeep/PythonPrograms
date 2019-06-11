#count the no. of words and characters from the  data of a file

file1 = open("file1.txt", "w")
file1.write(input("Enter a sentence: "))
file1.close()

file2 = open("file1.txt", "r")
items = file2.read()
data = items.split()
combine = ""
wordcount = 0
charcount = 0
for i in data:
    combine += i
    wordcount += 1
for i in combine:
    charcount += 1
print("Characters count: ", charcount)
print("Words count: ", wordcount)