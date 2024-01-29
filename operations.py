# Practice with methods and functions


#  EXERCISE a - print the value of var as upper case
# input function allows user to input a prompt which defines the variable
#  Use .upper() string method in a print function to convert all input letters to capitals
var = input("Please enter a value: ").upper()

# print variable uppercase
print(var)

# EXERCISE b - print the number of characters in var
# len() is used to count the number of characters in a string, including spaces. Also counts integers

print(len(var))


# EXERCISE c - does it contain numeric characters? (try the isdecimal() method)
# returns boolean value True if the input string contains ALL decimal characters,
# Decimal characters are numbers from 0-9
# otherwise it returns False
print(var.isdecimal())


# //////// EXTRAS ////////

# Only works with a string input, a numerical input will display as normal three times...

# use .lower() string method to convert all input letters to lower case
print(var.lower())

# use .capitalize() string method to convert the first letter of the first input word to a capital
print(var.capitalize())

# use .title() string method to convert the first letter of each input word to a capital
print(var.title())
