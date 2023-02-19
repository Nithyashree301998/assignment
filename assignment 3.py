#question 1
def sum(*num):
    add=0
    for i in num:
        add=add+i
    return add
result=sum(8,2,3,0,7)
print(result)        


#Question 2
def reverse(string):
    str=" "
    for i in string:
        str=i+str
    return str
string=input("enter the string:")
result=reverse(string)
print("the reverse of the string is :",result)    










#Question 3
def upper_lower(string):
    upper=0
    lower=0
    for i in string:
        if i.isupper():
            upper=upper+1
        elif i.islower():
            lower=lower+1
    print("number of upper case letters are",upper)
    print("number of upper case letters are",lower)
#string='The quick Brow Fox'
string=input("enter the string:")
upper_lower(string)

            

