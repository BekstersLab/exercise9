# Practice declaring variables and using different types

# create two variables: one containing your first name and another containing your last name
first_name = "Bek"
last_name = "Rootes"

# use the print function to output your full name with a space between your first and last name
print(f"{first_name} {last_name}")
# prints as: Bek Rootes

# transfer these variable values into a list
full_name = [first_name, last_name]
print(full_name)
# prints as: ['Bek', 'Rootes']

# take the variables and now store the values in a dictionary, using the keys 'first' and 'last'
name = {
    "first" : first_name,
    "last": last_name
}

# display the dictionary values
print(name)
# prints as: {'first": 'Bek', 'last': 'Rootes'}

# Access the value of keys
print(name["first"])
# prints as: Bek
print(name["last"])
# prints as: Rootes
