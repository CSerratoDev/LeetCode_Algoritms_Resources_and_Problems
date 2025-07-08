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
x = "\ooo"              # Octal value
x = "\xhh"              # Hex value

#String methods
a = "Hello"
a.capitalize()          # Converts the first character to upper case
a.casefold()            # Converts string into lower case (more aggressive than lower())
a.center()              # Returns a centered string
a.count()               # Returns the number of times a specified value occurs in a string
a.encode()              # Returns an encoded version of the string
a.endswith()            # Returns True if the string ends with the specified value
a.expandtabs()          # Sets the tab size of the string
a.find()                # Searches the string for a specified value and returns the position where it was found
a.format()              # Formats specified values in a string
a.format_map()          # Formats specified values in a string using a mapping
a.index()               # Searches the string for a specified value and returns the position where it was found
a.isalnum()             # Returns True if all characters in the string are alphanumeric
a.isalpha()             # Returns True if all characters in the string are in the alphabet
a.isascii()             # Returns True if all characters in the string are ASCII characters
a.isdecimal()           # Returns True if all characters in the string are decimals
a.isdigit()             # Returns True if all characters in the string are digits
a.isidentifier()        # Returns True if the string is a valid identifier
a.islower()             # Returns True if all characters in the string are lower case
a.isnumeric()           # Returns True if all characters in the string are numeric
a.isprintable()         # Returns True if all characters in the string are printable
a.isspace()             # Returns True if all characters in the string are whitespaces
a.istitle()             # Returns True if the string follows the rules of a title
a.isupper()             # Returns True if all characters in the string are upper case
a.join()                # Joins the elements of an iterable to the end of the string
a.ljust()               # Returns a left justified version of the string
a.lower()               # Converts a string into lower case
a.lstrip()              # Returns a left trimmed version of the string
a.maketrans()           # Returns a translation table to be used in translations
a.partition()           # Returns a tuple where the string is parted into three parts
a.replace()             # Returns a string where a specified value is replaced with another value
a.rfind()               # Searches the string for a specified value and returns the last position where it was found
a.rindex()              # Searches the string for a specified value and returns the last position where it was found
a.rjust()               # Returns a right justified version of the string
a.rpartition()          # Returns a tuple where the string is parted into three parts (searching from the right)
a.rsplit()              # Splits the string at the specified separator, and returns a list (from the right)
a.rstrip()              # Returns a right trimmed version of the string
a.split()               # Splits the string at the specified separator, and returns a list
a.splitlines()          # Splits the string at line breaks and returns a list
a.startswith()          # Returns True if the string starts with the specified value
a.strip()               # Returns a trimmed version of the string
a.swapcase()            # Swaps cases, lower case becomes upper case and vice versa
a.title()               # Converts the first character of each word to upper case
a.translate()           # Returns a translated string
a.upper()               # Converts a string into upper case
a.zfill()               # Fills the string with a specified number of 0 values at the beginning