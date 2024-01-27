# Practice declaring variables and using different types

# EXERCISE - create two variables: one containing your first name and another containing your last name
# give meaningful names to both variables using snakecase
first_name = "Bek"
last_name = "Rootes"

# EXERCISE - use the print function to output your full name with a space between your first and last name
# concatenate the two variables with + " " +
print(first_name + " " + last_name)

# concatenate using .format() method - better than previous version
print(("{} {}").format(first_name, last_name))

# use an f-string to concatenate the variables - best way as easily read
print(f"{first_name} {last_name}")
# all print as: Bek Rootes

# EXERCISE - transfer these variable values into a list
# create a new variable for the list name and enter the existing variables within square brackets (list),
# separated by a comma
full_name = [first_name, last_name]
# print the new variable
print(full_name)
# prints as: ['Bek', 'Rootes']

# Lists are mutable, therefore values can change
# index 0 = first_name and index 1 = last_name
# if I were to get married I would change the string value of index 1
full_name[1] = "Glean"
print(full_name)

# TO DO: add to list, remove from list, extract and put into an f-string
# list slicing

# EXERCISE - take the variables and now store the values in a dictionary, using the keys 'first' and 'last'
# create a new variable for the dictionary name eg. name
# use curly braces for a dictionary
# Declare as follows; '"key": value' and separate with a comma
name = {
    "first": first_name,
    "last": last_name
}

# or

name2 = {
    "first": "Bek",
    "last": "Rootes"
}

# EXERCISE - display the dictionary values
# print the dictionary variable
print(name)
print(name2)
# prints as: {'first": 'Bek', 'last': 'Rootes'}

# //////// EXTRAS ////////

# Access the value of keys
print(name["first"])
# prints as: Bek
print(name["last"])
# prints as: Rootes

# TO DO: print type!
