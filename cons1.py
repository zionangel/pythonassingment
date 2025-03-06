class MyClass:
    
    def _init_(self, a=None, b=None):
        if a is None and b is None:
            print("Default constructor called: No arguments")
        elif b is None:
            print(f"One argument constructor called: {a}")
        else:
            print(f"Two arguments constructor called: {a}, {b}")


if _name_ == "_main_":
    
    obj1 = MyClass()  
    

    obj2 = MyClass(10)  
    
    obj3 = MyClass(10, 20)