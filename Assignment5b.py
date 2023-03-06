class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def add(self):
        return self.num1+self.num2

    def subtract(self):
        return self.num1-self.num2

    def multiply(self):
        return self.num1*self.num2

    def divide(self):
        return float(self.num1)/float(self.num2)

n1=int(input("enter the first number:"))
n2=int(input("enter the second number:"))  
c1=Calculator(n1,n2)
r1=c1.add()
r2=c1.subtract()
r3=c1.multiply()
r4=c1.divide()
print(r1,"\n",r2,"\n",r3,"\n",r4)      
