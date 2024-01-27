# Practice with methods and functions
# https://www.sololearn.com/en/Discuss/2236259/how-to-assign-input-value-to-a-variable-in-python


#  EXERCISE a - print the value of var as upper case
#  Use .upper() string method in a print function to convert all input letters to capitals
var = input("Please enter a value: ").upper()

# print variable uppercase
print(var)

# EXERCISE b - print the number of characters in var
# len() is used to count the number of characters in a string, including spaces. Also counts integers

print(len(var))


# EXERCISE c - does it contain numeric characters? (try the isdecimal() method)
# returns boolean value True if the input string contains ALL decimal characters,
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
