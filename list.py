names = ['john','mary','james']

n = int(input("Enter the number of names needed to input: "))
for i in range(n):
   name = input("Enter the name: ")

names.append(name)
school = []
school = names.sorted()
print(names.sort())
print(school)