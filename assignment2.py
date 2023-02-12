#LIST AND TUPLE 
l1=[(2,5),(1,2),(4,4),(2,3),(2,1)]
for i in range(0,len(l1)):
    for j in range(0,len(l1)-i-1):
        if(l1[j][-1]>l1[j+1][-1]):
            a=l1[j]
            l1[j]=l1[j+1]
            l1[j+1]=a
print(l1)            













#CREATING DICTIONARY
dict={}
for i in range(97,123):
    dict[chr(i)] = str(i)
print(dict)    
