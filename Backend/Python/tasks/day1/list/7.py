#1)How do you create a list in Python?
a=[1,2,3,4,5]
#2)How can you access the first element of a list?
print(a[0])
#3)How do you access the last element of a list?
lastEle=a[-1]
print(lastEle)
#4)How do you access an element at a specific index in a list?
print(a[3])
#5)How can you slice a list to get a sublist
#6How do you get the length of a list?
print(len(a))
#7)How do you add an item to the end of a list?
a.append(6)
print(a)
#8)How do you insert an item at a specific index in a list?
a.insert(2,9)
print(a)
#9)How can you remove an item by value from a list?
a.remove(2)
print(a)
#10)How do you remove an item by index from a list?
a.pop(2)
print(a)
#11)What method allows you to remove all items from a list?
a.clear()
print("remmoved",a)
a=[3,2,1,5,4,3]

#12)How can you find the index of the first occurrence of a value in a list?
f=a.index(3)
print(f)
#13)How can you check if a value is in a list?
# print(a in 3)
#14)How do you count the number of occurrences of a 387
b=387
print(len(str(b)))
#15)
#16)How do you sort a list in ascending order?
a.sort()
print(a)

#17)How can you sort a list in descending order?
a.sort(reverse=True)
print(a)
#18)How can you reverse the order of elements in a list?
a.reverse()
print(a)
#19)How do you concatenate two lists?
c=[9,11,23,43]
print(a+c)
#20)How can you repeat a list multiple times?
d=a*3
print(d)
#21)How do you copy a list to create a new list with the same elements?
#22)How can you get the maximum value in a list of numbers?
print(max(a))
#23)How do you get the minimum value in a list of numbers?
print(min(a))
#24)How can you find the sum of all elements in a list of numbers?
print(sum(a))
#25)How do you remove duplicates from a list?
print(set(a))
#26)How do you create a list of numbers using a range?
print(list(range(1,10,2)))
#27)How can you create a list of lists (a matrix)?
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix)
#28)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [item for sublist in matrix for item in sublist]
print(flattened_list)
#29)How do you convert a list of strings into a single string?
p=['a','b','c','d']
f=','.join(p)
print(f,p)
#30)How can you convert a list into a tuple?
print(tuple(p))
#31How do you check if a list is empty?
print("empty") if len(p) == 0  else print(p)
#32How do you get the last N elements of a list?
print(p[-1])
#33
#34
#35
#36
#37
#38
#39
#40
#41
#42
#43
#44
#45
#46
#47
#48
#49
#50
#51
#52
#53
#54
#55
#56
#57
#58
#59
#60
#61
#62
#63
#64
#65
#66
#67
#68
#69
#70
#71
#72
#73
#74
#75
#76
#77
#78
#79
#80
#81
#82
#83
#84
#85
#86
#87
#88
#89
#90
#91
#92
#93
#94
#95
#96
#97
#98
#99
#90
#100