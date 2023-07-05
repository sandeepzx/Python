class Hospital:
    def __init__(self,admin,doctor,sister,department) :
        self.admin = admin 
        self.doctor = doctor
        self.sister = sister
        self.department = department

    def getdetails(self):
        self.admin = input("Enter the admin  name: ") 
        self.doctor = input("Enter doctor name: ") 
        self.sister = input("Enter sister name: ") 
        self.department = input("Enter department name: ") 
        
class Depart(Hospital):
    def putdetails(self):
        print(self.admin,self.doctor,self.sister,self.department)
    
class Patient:
    def __init__(self,name,age,num):
        self.name = name
        self.age = age
        self.num = num

    def detail(self):
        self.name = input("Enter name:")
        self.age = int (input("Enter age:"))
        self.num = int (input("Enter number:"))
        print(self.name,self.age,self.num)

obj = Patient("","","")
obj.detail()


seta = {16,4,82,56,43}
seta.add(23)
seta.remove(4)
setb = {1,43,56,7}
print(seta - setb)