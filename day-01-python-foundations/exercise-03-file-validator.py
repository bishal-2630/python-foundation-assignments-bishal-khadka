"""
Exercise: File Validator
Student: Bishal Khadka
Day: 1
"""

# Ask user for input
file_name = input("Enter the file name: ")

#remove extra spaces and convert to lowercase
file_name = file_name.strip().lower()

#Check file name extension
if file_name.endswith('.csv'):
    print(f'Valid file name: {file_name}')
elif file_name.endswith('.json'):
    print(f'Valid file name: {file_name}')
elif file_name.endswith('.parquet'):
    print(f'Valid file name: {file_name}')
else:
    print(f'Invalid file format.')