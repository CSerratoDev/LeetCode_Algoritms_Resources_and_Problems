#Data Types
str                             # Text Type
int, float, complex             # Numeric Types
list, tuple, range              # Sequence Types
dict                            # Mapping Type
set, frozenset                  # Set Types
bool                            # Boolean Type
bytes, bytearray, memoryview    # Binary Types
None                            # None Type

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
x = str(3)      # x will be '3'
y = int(3)      # y will be 3
z = float(3)    # z will be 3.0

#type
y = "Ale"
x = 3
z = 3.0
type(x) # x is 'int'
type(y) # y is 'str'
type(z) # z is 'float'

#Case-Sensitive
a = 4           # a is 4
A = "Alexis"    # A will not overwrite a, therefore is "Alexis"

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
myVariableName = "Ale"      # Camel case
MyVariableName = "Ale"      # Pascal case
my_variable_name = "Ale"    # Snake case


x, y, z = "Orange", "Apple", "Lemon"        #Many values to multiple variables, you can assign values to multiple variables in one line
x = y = z = "Orange"                        #One value to multiple variables, you can assign the same value to multiple variables 
fruits = ["apple", "banana", "cherry"]      # Unpack a collection
x, y, z = fruits

x = "World"                 #Global variables is when your created a variable outside of a function, and use it inside the function

def myfunc():               #If you create a variable with the same name inside a function
    print("Hello " + x)     #this variable will be local, and can only be used inside the function.
myfunc()

def myfuncKeyword():
    global x                    #The global Keyword
    x = "World with Keyword"
myfuncKeyword()
print("Hello " + x)



