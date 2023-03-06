#Question1 Square numbers
class Point:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def sqSum(self):
        return self.x**2 + self.y**2 + self.z**2
        
#user_input=input("enter the numbers:").split(',')
n1=int(input("enter the the value of x:"))
n2=int(input("enter the the value of y:"))
n3=int(input("enter the the value of z:"))
p1=Point(n1,n2,n3)
p2=p1.sqSum()
print(p2)            