# Practice declaring variables and using different types


# EXERCISE: create two variables: one containing your first name and another containing your last name
# Assigned a string value to each variable ''
# variables are containers for storing data value
# give meaningful names to both variables using snakecase
first_name = 'Leticia'
last_name = 'Santos'

# summary: the print function is used to run the arguments of the parameters inside the parentheses.
print(first_name, last_name)

# concatenate the two variables with + " " +
print(first_name + " " + last_name)

# concatenate using .format() method - better than previous version
print("{} {}".format(first_name, last_name))

# use an f-string to concatenate the variables - best way as easily read
print(f"{first_name} {last_name}")

# EXERCISE - transfer these variable values into a list

# lists full_name concatenate the two list items as one with + " " +
# created two lists and input string items in the []
full_name = ['leticia' + ' ' + 'santos', ]  # think it is bad coding,
full_name1 = ['leticia', 'santos']

# summary: the print function is used to run the list items of the list variable names above inside the parentheses.
# print the new variable
print(full_name)
print(full_name, full_name1)
print(type(full_name))

# Lists are mutable, therefore values can change
# index 0 = leticia and index 1 = santos
# if I were to get married I would change the string value of index 1
full_name1[1] = "Odigili"
print(full_name1)

# EXERCISE: take the variables and now store the values in a dictionary, using the keys 'first' and 'last'
# create a new variable for the dictionary name eg. name
# use curly braces for a dictionary
# Declare as follows; '"key": value' and separate with a comma

full_name_dictionary = {
    'first': 'Leticia',
    'last': 'Santos'
}

# print the dictionary values
print(type(full_name_dictionary))
print(full_name_dictionary)

# Access the value of keys
print(full_name_dictionary["first"])
print(full_name_dictionary["last"])
