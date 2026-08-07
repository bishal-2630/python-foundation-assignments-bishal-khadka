"""
Exercise: Data Quality Checker
Student: Bishal Khadka
Day: 1
"""
#Input values
total_rows = 2000
missing_rows = 120
duplicate_rows = 30

# For problematic rows
problematic_rows = missing_rows + duplicate_rows

# For problematic percentage
problematic_percentage = (problematic_rows / total_rows) * 100
print(f'Total Rows: {total_rows}')
print(f'Problematic Rows: {problematic_rows}')
print(f'Problematic Percentage: {problematic_percentage: .2f}%')


# For classification of data quality 
if problematic_percentage <= 2:
    print(f'Final Classification: Excellent')
elif problematic_percentage >= 2 and problematic_percentage <= 5:
    print(f'Final Classification: Acceptable')
elif problematic_percentage >= 5:
    print(f'Final Classification: Needs Cleaning')