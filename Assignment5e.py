class Account:
    def __init__(self, title=None, balance=0):
        self.title=title
        self.balance=balance

    def getBalance(self):
        return self.balance  
    

    def withdrawal(self,amount):
        self.amount=amount
        if float(amount)<float(self.balance):
            float(self.balance)-float(amount)  
        else:
            print("insufficient balance")

    def deposit(self,amount):
        self.amount=amount
        float(self.balance)+float(amount)
    
     


class SavingsAccount(Account):
    def __init__(self,title=None,balance=0,interestRate=0):
        super().__init__(title,balance)
        self.interestRate=interestRate     

    def interestAmount(self):
        return (self.balance*self.interestRate)/100
              

#s1=input("enter the title:")
#s2=int(input("enter the balance :"))
#s3=int(input("enter the interest rate:"))
a1=SavingsAccount("Ashish",2000,5)
#x1=input("enter the amount to withdraw:")
a1.withdrawal(500)
#x2=input("enter the amount to be deposited:")
a1.deposit(500)
a2=a1.interestAmount()
print(a2)