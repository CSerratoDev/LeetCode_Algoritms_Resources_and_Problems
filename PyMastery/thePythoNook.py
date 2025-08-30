#Setting the Data Type
x = "Hello"                 # str
x = 10                      # int
x = 10.5                    # float
x = 1j                      # complex
x = [1, 2, 3]               # list
x = (1, 2, 3)               # tuple
x = range(6)                # range
x = {"name": "Ale"}         # dict
x = {1, 2, 3}               # set
x = frozenset({1,2,3})      # frozenset
x = True                    # bool
x = b"Hello"                # bytes
x = bytearray(5)            # bytearray
x = memoryview(bytes(5))    # memoryview
x = None                    # NoneType

#Setting the specific Data Type
x = str("Hello")            # str
x = int(10)                 # int
x = float(10.5)             # float
x = complex(1j)             # complex
x = list((1, 2, 3))         # list
x = tuple((1, 2, 3))        # tuple
x = range(6)                # range
x = dict(name="Ale")        # dict
x = set((1, 2, 3))          # set
x = frozenset((1, 2, 3))    # frozenset
x = bool(True)              # bool
x = bytes(5)                # bytes
x = bytearray(5)            # bytearray
x = memoryview(bytes(5))    # memoryview
x = None                    # NoneType

#Variable example
x = str(3)                  # x will be '3'
y = int(3)                  # y will be 3
z = float(3)                # z will be 3.0

#type
y = "Ale"
x = 3
z = 3.0
type(x)                     # x is 'int'
type(y)                     # y is 'str'
type(z)                     # z is 'float'

#Case-Sensitive
a = 4                       # a is 4
A = "Alexis"                # A will not overwrite a, therefore is "Alexis"

#Legal variable names
myvar = "Ale"
my_var = "Ale"
_my_var = "Ale"
myVar = "Ale"
MYVAR = "Ale"
myvar2 = "Ale"

#Illegal variable names
#2myvar = "Ale"
#my-var = "Ale"
#my var = "Ale"

#Multi words variable names
myVariableName = "Ale"                      # Camel case
MyVariableName = "Ale"                      # Pascal case
my_variable_name = "Ale"                    # Snake case


x, y, z = "Orange", "Apple", "Lemon"        #Many values to multiple variables, you can assign values to multiple variables in one line
x = y = z = "Orange"                        #One value to multiple variables, you can assign the same value to multiple variables 
fruits = ["apple", "banana", "cherry"]      # Unpack a collection
x, y, z = fruits

x = "World"                                 #Global variables is when your created a variable outside of a function, and use it inside the function

def myfunc():                               #If you create a variable with the same name inside a function
    print("Hello " + x)                     # this variable will be local, and can only be used inside the function.
myfunc()

def myfuncKeyword():
    global x                                #The global Keyword
    x = "World with Keyword"
myfuncKeyword()
print("Hello " + x)

print("Hello with double quotation marks is the same as" + 'Hello with single quotation marks') #Strings quotation marks

#Strings are Arrays
a = 'Hello'
b = a[2]                    # You can bring in the position of a character

#Looping through a string
for x in "apple":
    print(x)

#String length
a = "Hello World"
b = len(a)                  # You can get the length of a string

#Check string
txt = "my name is ale"
print("ale" in txt)         # You can to check if a certain phrase or character is present in a string.

#Check if NOT
print("alexis" not in txt)  # You can to check if a certain phrase or character is NOT present in a string.

#Slicing with String
a = "Alexis"
b = a[2:3]                  # You can specify the start index and the end index, separated by a colon, to return a part of the string.
c = a[:3]
d = a[2:]
e = a[-5:-2]

#Modify strings
a = "my name is: ale"
#Upper case
b = a.upper()               # Return string in upper case
#Lower case
c = a.lower()               # Return string in lower case
#Remove whitespace
d = a.strip()               # When you want to delete whitespace is the space before and/or after the actual text
#Replace string
e = a.replace("m", "M")     # Replaces a string with another string
#Split string
f = a.split(":")            # This method returns a list where the text between the specified separator becomes the list items.

#Concatenate strings
a = "my name is: "
b = "ale"

c = a + b
c = a + " " + b

#Format strings
age = 25
#txt = "My name is Ale, I am " + age          We cannot combine strings and numbers like this:
txt = f"My name is Ale, I am {age}"         # F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.

#Placeholders and Modifiers
price = 50
txt = f"The price is {price} dollars"
txt = f"The price is {price:.2f} dollars"   # A placeholder can include a modifier to format the value.
print(txt)
txt = f"The price is {20 * price} dollars"  # A placeholder can contain Python code, like math operations:

#Escape character
#txt = "We are the so-called "Vikings" from the north." You will get an error if you use double quotes inside a string that is surrounded by double quotes
txt = "We are the so-called \"Vikings\" from the north."        #To fix this problem, use the escape character \":

x = "\'"                # Single quote
x = "\\"                # Backslash
x = "\n"                # New line
x = "\r"                # Carriage return
x = "\t"                # Tab
x = "\b"                # Backspace
x = "\f"                # Form feed
#x = "\ooo"              # Octal value
#x = "\xhh"              # Hex value

# Booleans
a = 10
b = 9
print(a > b)
print(a == b)
print(a < b)
x = bool(a)             # This function allows you to evaluate any value, and give you True or False in return
# except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.

"""
for example

class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))


"""
#You can execute code based on the Boolean answer of a function
def myFunction() :
    return True

if myFunction():
    print("YES!")
else:
    print("NO!")    

x = 200
print(isinstance(x, int))       # Which can be used to determine if an object is of a certain data type

#Arithmetic Operators
x = 2
y = 3

z = x + y                       # Addition
z = x - y                       # Subtraction
z = x * y                       # Multiplication
z = x / y                       # Division
z = x % y                       # Modulus
z = x ** y                      # Exponentiation
z = x // y                      # Floor division

#Assignment Operators
x = 5
x += 3                          # Addition assignment
x -= 2                          # Subtraction assignment
x *= 4                          # Multiplication assignment
x /= 2                          # Division assignment
x %= 3                          # Modulus assignment
x //= 2                         # Floor division assignment
x **= 3                         # Exponentiation assignment
x &= 2                          # Bitwise AND assignment
x |= 2                          # Bitwise OR assignment
x ^= 2                          # Bitwise XOR assignment
x >>= 1                         # Bitwise right shift assignment
x <<= 1                         # Bitwise left shift assignment
print(x := 3)                   # Print into 

#Comparison Operators
a = 1
b = 2
print(a == b)                   # Equal to
print(a != b)                   # Not equal to
print(a < b)                    # Less than
print(a > b)                    # Greater than
print(a >= b)                   # Greater than or equal to
print(a <= b)                   # Less than or equal to 

#Logical Operators
if a < 5 and a < 10:            # True if both conditions are true (AND)
    print("Yes")
if a < 5 or a < 4:              # True if at least one condition is true (OR)
    print("Yes")
if not(a < 5 and a < 10):       # True if the condition inside not is false (NOT)
    print("False")

#Identity Operators
a is b                          # Used to compare the objects
a is not b                      # but if they are actually the same object, with the same memory location

#Membership Operators
a in b                          # Returns True if a sequence with the specified value is present in the object
a not in b                      # Returns True if a sequence with the specified value is not present in the object

#Bitwise Operators
x = 5                           # 0101
y = 3                           # 0011

z = x & y   # Bitwise AND:        0001 (1)      Sets each bit to 1 if both bits are 1
z = x | y   # Bitwise OR:         0111 (7)      Sets each bit to 1 if one of two bits is 1
z = x ^ y   # Bitwise XOR:        0110 (6)      Sets each bit to 1 if only one of two bits is 1
z = ~x      # Bitwise NOT:        -(x+1) (-6)   Inverts all the bits
z = x << 1  # Bitwise left shift: 1010 (10)     Shift left by pushing zeros in from the right and let the leftmost bits fall off
z = x >> 1  # Bitwise right shift:0010 (2)      Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

#Operator precedence
# Operator precedence (from highest to lowest):

# 1. () Parentheses
# 2. ** Exponentiation
# 3. +x, -x, ~x (Unary plus, minus, bitwise NOT)
# 4. *, /, //, %
# 5. +, -
# 6. <<, >>
# 7. &
# 8. ^
# 9. |
# 10. ==, !=, >, >=, <, <=, is, is not, in, not in  Comparison operators
# 11. not
# 12. and
# 13. or
# 14. (=, +=, -=, etc.) Assignment operators 
# 15. Lambda expressions