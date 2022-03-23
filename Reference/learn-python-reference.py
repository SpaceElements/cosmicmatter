#This tutorial / reference was obtained from https://www.learnpython.org

#Hello, World
print("This line will be printed.")

#Indentation
x = 1
if x == 1:
	# indented four spaces
	print("x is 1.")

#Numbers
#To define an integer use the following syntax.
myint = 7
print(myint)

#Floating point number
#To define a floating point number, you may use one of the following notations.
myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)

#Strings
#Strings are defined either with a single quote or a double quotes.
mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)
mystring = "Don't worry about apostrophes"
print(mystring)

#Operators on strings
one = 1
two = 2
three = one + two
print(three)
hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

#Assignments can be done on more than one variable "simultaneously" on the same line lke this
a, b = 3, 4
print(a, b)

#Example strings and numbers exercise
mystring = "hello"
myfloat = 10.0
myint = 20

if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)

#Lists
#Lists are very similar to arrays. They can contain any type of variable, and they can contain as many variables as you wish. Lists can also be iterated over in a very simple manner. Here is an example of how to build a list.
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3

# prints out 1,2,3
for x in mylist:
	print(x)

#Example exercise with Lists, strings and numbers
numbers = [1,2,3]
strings = ["hello", "world"]
names = ["John", "Eric", "Jessica"]

# write your code here
second_name = names[1]


# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

#Basic Operators
#Arithmetic Operators
number = 1 + 2 * 3 / 4.0
print(number)

#modulo % operator (returns the integer remainder of the division)
remainder = 11 % 3
print(remainder)

#Power Relationship (squares, cubes, exponents)
squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)

#Using Operators with Strings
helloworld = "hello" + " " + "world"
print(helloworld)

#multiplying strings to form a string with a repeating sequence
lotsofhellos = "hello" * 10
print(lotsofhellos)

#Using Operators with Lists
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

#forming new lists with a repeating sequence using the multiplication operator
print([1,2,3] * 3)

#Exercise using concatenating with two lists that have repeating variables
x = object()
y = object()

# TODO: change this code
x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")

#String Formatting
# This prints out "Hello, John!"
name = "John"
print("Hello, %s!" % name)

#Using a tuple (parentheses) with two or more argument specifiers
# This prints out "John is 23 years old."
name = "John"
age = 23
print("%s is %d years old." % (name, age))

#Using %s to format an object which is not a string, such as a number list
# This prints out: A list: [1, 2, 3]
mylist = [1,2,3]
print("A list: %s" % mylist)

# Here are some basic argument specifiers you should know:
# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
# %x/%X - Integers in hex representation (lowercase/uppercase)

#Another example with string formatting
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."
print(format_string % data)

###########################
# Basic string operations #
###########################

# Defining Strings

astring = "Hello world!"
astring2 = 'Hello world!'

# Print length of string

astring = "Hello world!"
print("single quotes are ' '")

print(len(astring))

# Print out first occurance of character 'o' or 'l' in string

astring = "Hello world!"
print(astring.index("o"))

astring = "Hello world!"
print(astring.count("l"))

# This prints the characters of string from 3 to 7 skipping one character, etc.
# This is extended slice syntax. The general form is [start:stop:step].

astring = "Hello world!"
print(astring[3:7:2])

astring = "Hello world!"
print(astring[3:7])
print(astring[3:7:1])

astring = "Hello world!"
print(astring[::-1])

# Make strings upper or lowercase
astring = "Hello world!"
print(astring.upper())
print(astring.lower())

# figure out if a string starts or ends with something (gives you a true)
astring = "Hello world!"
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))

# convert string in to list, starting w/ 0
astring = "Hello world!"
afewwords = astring.split(" ")

# Example exercise basic string operations

s = "Strings are awesome!"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))

##############
# Conditions #
##############

# Basic boolean logic
x = 2
print(x == 2) # prints out True
print(x == 3) # prints out False
print(x < 3) # prints out True

# Using and/or

name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")


# Figure out if something exists in a list, then do something if true

name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")

##> Example of python using code blocks

statement = False
another_statement = True
if statement is True:
    # do something
    pass
elif another_statement is True: # else if
    # do something else
    pass
else:
    # do another thing
    pass

x = 2
if x == 2:
    print("x equals two!")
else:
    print("x does not equal to two.")

##> This shows the difference of == and is. 
# Is matches the instances themselves, not the values

x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False

# Inverting a boolean expression using 'not'
print(not False) # Prints out True
print((not False) == (False)) # Prints out False

##> Example script with boolean

# change this code
number = 16
second_number = 0
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")

#############
# Loops #####
#############

##> For loop, interating over a given sequence

primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)

##> For loops can iterate over a sequence of numbers using the "range" 
# and "xrange" functions. The difference between range and xrange is 
# that the range function returns a new list with numbers of that 
# specified range, whereas xrange returns an iterator, which is more 
# efficient. (Python 3 uses the range function, which acts like xrange). 
# Note that the range function is zero based.

# Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x)

# Prints out 3,4,5
for x in range(3, 6):
    print(x)

# Prints out 3,5,7
for x in range(3, 8, 2):
    print(x)

# While Loop, repeats while a condition is true
# Prints out 0,1,2,3,4

count = 0
while count < 5:
    print(count)
    count += 1  # This is the same as count = count + 1


##> break is used to exit a for loop or a while loop, 
# whereas continue is used to skip the current block, 
# and return to the "for" or "while" statement.
# Prints out 0,1,2,3,4

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)


##> Else Clause in Loop? Unlike languages like C,CPP.. 
# we can use else for loops. When the loop condition of 
# "for" or "while" statement fails then code part in "else" 
# is executed. If a break statement is executed inside the 
# for loop then the "else" part is skipped. Note that the 
# "else" part is executed even if there is a continue statement.

# Prints out 0,1,2,3,4 and then it prints "count value reached 5"

count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))

# Prints out 1,2,3,4
for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")


##> Example Loop Exercise
# Loop through and print out all even numbers from the numbers list in 
# the same order they are received. Don't print any numbers that come 
# after 237 in the sequence.

numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

# your code goes here
for number in numbers:
    if number == 237:
        break

    if number % 2 == 1:
        continue

    print(number)


#############
# Functions #
#############
# Functions are a convenient way to divide your code into useful blocks,
# allowing us to order our code, make it more readable, reuse it and save
# some time. Also functions are a key way to define interfaces so 
# programmers can share their code.
#############

##> define a function using 'def'

def my_function():
    print("Hello From My Function!")

##> Function receiving arguments (variables passed from caller to function)

def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))

##> Functions may return a value to the caller, using the keyword return

def sum_two_numbers(a, b):
    return a + b

##> Calling functions in Python

# Define our 3 functions
def my_function():
    print("Hello From My Function!")

def my_function_with_args(username, greeting):
    print("Hello, %s, From My Function!, I wish you %s"%(username, greeting))

def sum_two_numbers(a, b):
    return a + b

# print(a simple greeting)
my_function()

#prints - "Hello, John Doe, From My Function!, I wish you a great year!"
my_function_with_args("John Doe", "a great year!")

# after this line x will hold the value 3!
x = sum_two_numbers(1,2)

##> Example script with functions

# Modify this function to return a list of strings as defined above
def list_benefits():
    return "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit


def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()

#######################
# Classes and Objects #
#######################



