
employee = dict()
name = ["anil","arun","anjali","harry"]
id = [1,2,3,4]
ph = ["n0","n1","n2","n3"]
position = ["manager","sales","account","owner"]


n = input("enter name: ")
l = len(name)
f = 0
for i in range(l):
    if n == name[i]:
        p = i
        s =[id[p],ph[p],position[p]]
        employee[n] = s
        print(employee)
        f = 1

if f == 0:
    print("not in list")  

