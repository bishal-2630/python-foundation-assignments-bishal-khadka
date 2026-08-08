"""
Exercise: Retry Simulation
Student: Bishal Khadka
Day: 2
"""

# Given variables
attempt = 2
max_attempts = 3
operation_successful = False

# while loop to retry upto max attempts
while attempt <= max_attempts:
    print(f"Attempt {attempt}")

    # simulate operation success on the second attempt
    if attempt == 2:
        operation_successful = True
        break #stop the loop if operation is successful

    # increment the attempt counter
    attempt += 1

if operation_successful:
    print("Operation completed successfully")
else:
    print("Operation failed after three attempts")
        
# Output:
''' when attempt = 1
Attempt 1
Attempt 2
Operation completed successfully

when attempt = 2
Attempt 2
Operation completed successfully

when attempt =3
Attempt 3
Operation failed after three attempts
'''