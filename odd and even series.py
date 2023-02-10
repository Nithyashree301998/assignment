series=input("enter the series:").split(',')
even=0
odd=0
for i in series:
    if int(i)%2==0:
        even=even+1
    else:
        odd=odd+1
print("Number of even numbers",even)  
print("Number of odd numbers",odd)          