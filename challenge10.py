class vehicles:
    def __init__(self,x):
        self.x = x

    def getspecs(self):
        self.x = input("Enter the specifications:")

    def displayspecs(self):
        print(self.x)
        
class car(vehicles):
    def specialspec(self):
        print("has four wheels")


class bike(vehicles):
    def specialspec(self):
        print("Has two wheels")

obj = car("")
obj.getspecs()
obj.displayspecs()
obj.specialspec()