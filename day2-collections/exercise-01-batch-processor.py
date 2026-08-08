"""
Exercise: Batch Processor
Student: Bishal Khadka
Day: 2
"""

# Display number from range 1 to 10
for batch_number in range(1, 11):
    print(f'Processing batch {batch_number}')
    #modulo operator to check if batch_number is divisible by 3
    if batch_number % 3 == 0:
        print(f"Checkpoint reached")


#Output:
'''
Processing batch 1
Processing batch 2
Processing batch 3
Checkpoint reached
Processing batch 4
Processing batch 5
Processing batch 6
Checkpoint reached
Processing batch 7
Processing batch 8
Processing batch 9
Checkpoint reached
Processing batch 10
'''