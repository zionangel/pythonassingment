class SuperClass:
    def _init_(self, arg1=None, arg2=None):
        if arg1 is None and arg2 is None:
            print("SuperClass Default constructor called!")
        elif arg2 is None:
            print(f"SuperClass One-argument constructor called with arg1: {arg1}")
        else:
            print(f"SuperClass Two-argument constructor called with arg1: {arg1} and arg2: {arg2}")

class SubClass(SuperClass):
    def _init_(self, arg1=None, arg2=None):
        # Calling the default constructor of the superclass
        if arg1 is None and arg2 is None:
            super()._init_()
        # Calling the one-argument constructor of the superclass
        elif arg1 is not None and arg2 is None:
            super()._init_(arg1)
        # Calling the two-argument constructor of the superclass
        elif arg1 is not None and arg2 is not None:
            super()._init_(arg1, arg2)

        print("SubClass constructor called!")

# Running the SubClass to demonstrate calling constructors of the SuperClass
if _name_ == "_main_":
    print("Instantiating SubClass with no arguments:")
    obj1 = SubClass()

    print("\nInstantiating SubClass with one argument:")
    obj2 = SubClass("Hello")

    print("\nInstantiating SubClass with two arguments:")
    obj3 = SubClass("Hello", "World")