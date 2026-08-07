"""
Exercise: Customer Cleaner
Student: Bishal Khadka
Day: 1
"""

# Given data
raw_name = "  sAgar THAPA "
raw_city = "kATHMANDU "
raw_age = "27"
raw_email = " SAGAR@MAIL.COM "

# Clean the data
name = raw_name.strip().title()
city = raw_city.strip().title()
age = int(raw_age.strip())
email = raw_email.strip().lower()

#Ternary expression for adult status
status = "Adult" if age >= 18 else "Minor"

#Print clean data with adult status
print(f'Name: {name}')
print(f'City: {city}')
print(f'Age: {age}')
print(f'Email: {email}')
print(f'Status: {status}')