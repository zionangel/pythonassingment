# Class 1 definition
class Class1:
    def _init_(self, name):
        self.name = name
    
    def greet(self):
        print(f"Hello from Class1! My name is {self.name}")

# Class 2 definition
class Class2:
    def _init_(self, name):
        self.name = name
    
    def greet(self):
        print(f"Hello from Class2! My name is {self.name}")

# Main program logic
if _name_ == "_main_":
    # Creating an object of Class1
    obj1 = Class1("Alice")
    obj1.greet()  # Calling greet method from Class1

    # Creating an object of Class2
    obj2 = Class2("Bob")
    obj2.greet()  # Calling greet method from Class2