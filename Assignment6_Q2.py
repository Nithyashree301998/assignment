class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color
    
    def description(self):
        print(f"{self.name} is {self.age} years old.")
    
    def get_info(self):
        print(f"{self.name} has a {self.coat_color} coat.")
    

class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)
        
    def origin(self):
        print(f"{self.name} has its origin in fox hunting in England.")
        
    def possess(self):
        print(f"{self.name} is a possessive dog.")
        

class Bulldog(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)
        
    def sound(self):
        print(f"{self.name} is scared of loud noices such as thunder.")
        
    def getalong(self):
        print(f"{self.name} gets along well with children.")


dog1 = Dog("Fido", 3, "brown")

# Call Dog methods
dog1.description()  # Output: Fido is 3 years old.
dog1.get_info()     # Output: Fido has a brown coat.

# Create a JackRussellTerrier object
jr_terrier = JackRussellTerrier("Rex", 2, "white")

# Call Dog methods inherited by JackRussellTerrier
jr_terrier.description()  # Output: Rex is 2 years old.
jr_terrier.get_info()     # Output: Rex has a white coat.

# Call JackRussellTerrier methods
jr_terrier.origin()  # Output: Rex loves to play fetch.
jr_terrier.possess()   # Output: Rex is a skilled hunter.

# Create a Bulldog object
bulldog = Bulldog("Spike", 5, "gray")

# Call Dog methods inherited by Bulldog
bulldog.description()  # Output: Spike is 5 years old.
bulldog.get_info()     # Output: Spike has a gray coat.

# Call Bulldog methods
bulldog.sound()  # Output: Spike is famous for its loud snoring.
bulldog.getalong()  # Output: Spike makes a great guard dog.