class Bcolors:
    WHITE = "\033[97m"
    CYAN = "\033[96m"
    MAGENTA = "\033[95m"
    BLUE = "\033[94m"
    YELLOW = "\033[93m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    GREY = "\033[90m"
    SOFTWHITE = "\033[37m"
    SOFTCYAN = "\033[36m"
    SOFTMAGENTA = "\033[35m"
    SOFTBLUE = "\033[34m"
    SOFTYELLOW = "\033[33m"
    SOFTGREEN = "\033[32m"
    SOFTRED = "\033[31m"
    SOFTGREY = "\033[30m"
    DRACULA = "\033[38;5;87m"
    ENDC = "\033[0m"


# A simple Person class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        rep = "variableforclass(" + self.name + "," + str(self.age) + ")"
        return rep

# Let's make a Person object and print the results of repr()

variableForClass = Person("John", 20)
print(repr(variableForClass))


class Equipment:
    def __init__(self, item1, item2, item3):
        self.item1 = item1
        self.item2 = item2
        self.item3 = item3

    def __repr__(self):
        rep = (
            Bcolors.GREY
            + "You are currently equiped with the following"
            + "\n"
            + bcolors.WHITE
            + "_______________________________________"
            + "\n"
            + bcolors.BLUE
            + "Item1: "
            + self.item1
            + "\n"
            + "item 2: "
            + self.item2
            + "\n"
            + "item 3: "
            + self.item3
            + bcolors.ENDC
        )
        return rep


someVariable = Equipment("shield", "sword", "helmet")
print(repr(someVariable))

# Defining a class ()
# class Test:
#    def __init__(self, a, b):
#        self.a = a
#        self.b = b
#
#    def __repr__(self):
#        return "Test a:% s b:% s" % (self.a, self.b)
#
#    def __str__(self):
#        return "From str method of Test: a is % s, " \
#              "b is % s" % (self.a, self.b)

# Driver Code
# t = Test(1234, 5678)

# This calls __str__()
# print(t)

# This calls __repr__()
# print([t])


# A simple Person class

# class Person:
#    def __init__(self, name, age):
#        self.name = name
#        self.age = age
#
#    def __repr__(self):
#        rep = 'Person(' + self.name + ',' + str(self.age) + ')'
#        return rep
