#question2 to print index 2 to 6
# li1 = [1,2,3,5,7,6,9]

# li2 = li1[2:7]

# print(li2)

#question 3 to print the second last of tuple after append and insert
tup = (1,2,3,4,5,7)

li3 = list(tup)

li3.append(10)
li3.insert(3,12)

tup = tuple(li3)
print(tup.index(tup[-2]))