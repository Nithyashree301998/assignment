#Question 1

n=lambda i:i + 25
x=int(input("enter the number to be added:"))
print(n(x))


#Question 2
l=input("enter the list to be updated:").split(',')

def triple_num(b):
    c= int(b)*3 
    return c
print(list(map(triple_num,l)))
#print(result)


#Question 3

def square_num(m):

    k= int(m)*int(m)
    return k

user_input=input("enter the list:").split(',')
result1=list(map(square_num,user_input))
print(result1)    