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

# Simulate the behavior of _init_.py
# In real scenarios, this would be in the _init_.py file within a package directory

def initialize_package():
    # Expose classes directly when "importing" this script as a package
    globals()['Class1'] = Class1
    globals()['Class2'] = Class2


# Simulate package initialization
initialize_package()

# Testing the classes
if _name_ == "_main_":
    obj1 = Class1("Alice")
    obj2 = Class2("Bob")

    obj1.greet()  # Output: Hello from Class1! My name is Alice
    obj2.greet()  # Output: Hello from Class2! My name is Bob