"""
Exercise: Load and get oriented 
Student: Bishal Khadka
Day: 7
"""

import pandas as pd 

# Load the checkout data from the CSV file
checkout_df = pd.read_csv('day-05-cedar-grove-public-library/checkouts.csv' ,parse_dates = ['checkout_date', 'due_date', 'return_date']) 

n_total_checkouts = len(checkout_df)

n_still_checked_out = len(checkout_df[checkout_df['return_date'].isnull()])

print(f"{n_total_checkouts} total checkouts, {n_still_checked_out} still checked out")

# Check yourself
assert n_total_checkouts == len(checkout_df)
assert n_still_checked_out == checkout_df["return_date"].isna().sum()
assert n_still_checked_out < n_total_checkouts
print("Looks good.")

'''
Output:
160 total checkouts, 48 still checked out
Looks good.
'''