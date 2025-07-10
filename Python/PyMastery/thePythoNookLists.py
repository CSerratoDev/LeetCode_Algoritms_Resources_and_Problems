#In this PythoNook we're going to go deep into using list in python
#List is a collection which is ordered and changeable. Allows duplicate members.

#Lists
simple_list = ["apple", "orange", "lemon"]  #Lists are created using square brackets

#List items are ordered, changeable, and allow duplicate values
#If you add new items to a list, the new items will be placed at the end of the list.

"""List items - Data Types"""
#List items can be of any data types
str_list = ["Hello", "World", "!"]  
int_list = [1,2,3,4,5]
bool_list = [True, False, True]

#A list can contain different data types
random_list = ["abc", 25, True, 2025, "male"]

#From python's perspective, lists are defined as objects with the data types 'list'
type(str_list)
type(int_list)
type(bool_list)
type(random_list)

#It is also possible to use the list() constructor when creating a new list.
list_constructor = list(("apple", "orange", "lemon"))
