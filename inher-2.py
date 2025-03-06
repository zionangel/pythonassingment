# Superclass A
class A:
    def method_A(self):
        print("Method from class A")

# Subclass B (Inherits from A)
class B(A):
    def method_B(self):
        print("Method from class B")

# Subclass C (Inherits from B)
class C(B):
    def method_C(self):
        print("Method from class C")

# Creating an instance of C
obj = C()

# Accessing methods from all classes
obj.method_A()  # Inherited from A
obj.method_B()  # Inherited from B
obj.method_C()  # Defined in C