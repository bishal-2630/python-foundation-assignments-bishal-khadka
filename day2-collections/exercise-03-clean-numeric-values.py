"""
Exercise: Clean Numeric Values
Student: Bishal Khadka
Day: 2
"""
# Given values
raw_values = [100, None, 250, "invalid", 300, None, 450]

valid_values = []  # list to store valid integer values

# Clean numeric values from the list
for value in raw_values:
    if  not isinstance(value, int): # check if the value is not an integer
        continue  # skip non-integer values

    valid_values.append(value)  # add valid integer values to the list

print(valid_values)

# Using list comprehension
raw_values = [100, None, 250, "invalid", 300, None, 450]

# integer values stored in valid_values using list comprehension
valid_values = [value for value in raw_values if isinstance(value, int)]

print(valid_values)


# Output:
# [100, 250, 300, 450]