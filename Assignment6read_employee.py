import json

class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state
    def __str__(self):
        return f"{self.name} ,({self.dob}), {self.height}, {self.city}, {self.state}"
    

file= open("C:\\Users\\Vishnu\\vs code\\Assignment6_Q1a\\employee.json")
data = json.load(file)

employees = []
for employee_data in data["employees"]:
    name = employee_data["name"]
    dob = employee_data["dob"]
    height = employee_data["height"]
    city = employee_data["city"]
    state = employee_data["state"]
    employee = Employee(name,dob,height,city,state)
    employees.append(employee)

for employee in employees:
    print(employee)