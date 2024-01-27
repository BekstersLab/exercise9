# Practice declaring variables and using different types
# 1. Why is this coding concept this way?
# 2. Is there another way to do this?
# 3. What can I build to help me learn this more? (Maybe not want to build with it)
from typing import List

# create two variables: one containing your first name and another containing your last name
# created two variables: first_name and last_name
# Assigned a string value to each variable ''
# variables are containers for storing data value
first_name = 'Leticia'
last_name = 'Santos'

# use the print function to output your full name with a space between your first and last name
print(first_name, last_name)

# notes on above block of code
# summary: the print function is used to run the arguments of the parameters inside the parentheses.
# function is a block of code which runs when called.
# parentheses () are necessary to call on a function - allow the code it to run.
# parameters is the variables listed inside the parentheses ()
# arguments is the values sent to the function when it is called
# print is a function which runs the string values assigned to the variables inside the brackets
# This displays the first and last name with a space


# transfer these variable values into a list
# look into rules of a list and explain
# lists are ordered so will display the first value in the list
# created a list [] to transfer variable values first_name and last_name
# Concatenated with + both variable to list both variable values together with a name
full_name_list = ['leticia' + ' ' + 'santos', ]
print(type(full_name_list))
print(full_name_list)
# is there a way to use the print function to display the list values and store the names without concantenation
# print(full_name_list[0:]) prints first name and excludes last

# TO DO: add to list, remove list, extract and put into an f-string
# list slicing

full_name_1 = ['leticia', 'santos']
print(full_name_1)

# take the variables and now store the values in a dictionary, using the keys 'first' and 'last'
# key: values

full_name_dictionary = {
    'first': 'Leticia',
    'last': 'Santos'
}

# display the dictionary values
print(type(full_name_dictionary))
print(full_name_dictionary)