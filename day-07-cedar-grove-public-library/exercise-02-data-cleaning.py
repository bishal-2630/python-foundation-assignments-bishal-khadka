"""
Exercise: Data Cleaning 
Student: Bishal Khadka
Day: 7
"""

import pandas as pd

checkouts_df = pd.read_csv('day-07-cedar-grove-public-library/checkouts.csv', parse_dates=['checkout_date', 'due_date', 'return_date'])

checkouts_clean = checkouts_df.copy()

checkouts_clean["is_returned"] = checkouts_clean["return_date"].notnull() #check if return_date is present and returns in Boolean

checkouts_clean["late_fee"] = checkouts_clean["late_fee"].fillna(0) #fills with 0 if empty

print(checkouts_clean.head()) 

# Check yourself
assert checkouts_clean["late_fee"].isna().sum() == 0
assert checkouts_clean["is_returned"].dtype == bool
assert checkouts_clean["is_returned"].sum() == checkouts_clean["return_date"].notna().sum()
print("Looks good:", checkouts_clean["is_returned"].value_counts().to_dict())


'''
Output:
    checkout_id member_id              book_title            genre checkout_date   due_date return_date  late_fee  is_returned
0    CHK-3001  MEM-0014        The Great Gatsby  Classic Fiction    2026-06-12 2026-07-03  2026-07-03       0.0         True
1    CHK-3002  MEM-0034               Jane Eyre           Gothic    2026-07-19 2026-08-09         NaT       0.0        False
2    CHK-3003  MEM-0060  The Catcher in the Rye  Classic Fiction    2026-01-02 2026-01-23         NaT       0.0        False
3    CHK-3004  MEM-0051              The Hobbit        Adventure    2026-06-16 2026-07-07         NaT       0.0        False
4    CHK-3005  MEM-0028  The Catcher in the Rye  Classic Fiction    2026-04-01 2026-04-22  2026-04-22       0.0         True
Looks good: {True: 112, False: 48}
'''