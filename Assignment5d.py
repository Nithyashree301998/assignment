class Account:
    def __init__(self, title=None, balance=0):
        self.title=title
        self.balance=balance


class SavingsAccount(Account):
    def __init__(self,title=None,balance=0,interestRate=0):
        super().__init__(title,balance)
        self.interestRate=interestRate        

s1=input("enter the title:")
s2=int(input("enter the balance :"))
s3=int(input("enter the interest rate:"))
a1=SavingsAccount(s1,s2,s3)

