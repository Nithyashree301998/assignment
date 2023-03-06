class Student:
    def __init__(self, name, rollNumber):
        self.__name = name
        self.__rollNumber = rollNumber

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getRollNumber(self):
        return self.__rollNumber

    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber

s1=input("enter the name:")
s2=int(input("enter the rollnumber:"))
student1 = Student(s1, s2)

print("Name:", student1.getName())
print("Roll Number:", student1.getRollNumber())

s3=input("enter the name:")
s4=int(input("enter the rollnumber:"))


student1.setName(s3)
student1.setRollNumber(s4)


print("Name:", student1.getName())
print("Roll Number:", student1.getRollNumber())        