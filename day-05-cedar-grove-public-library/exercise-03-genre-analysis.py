"""
Exercise: Genre Analysis 
Student: Bishal Khadka
Day: 7
"""

import pandas as pd 

checkouts_df = pd.read_csv('day-05-cedar-grove-public-library/checkouts.csv', parse_dates=['checkout_date', 'due_date', 'return_date'])

checkouts_clean = checkouts_df.copy()
checkouts_clean["is_returned"] = checkouts_clean["return_date"].notnull()

returned_books = checkouts_clean[checkouts_clean["is_returned"]] #for data where is_returned is True

#filters and calculate avg 
avg_late_fee_by_genre = returned_books.groupby("genre")["late_fee"].mean().sort_values(ascending = False) 

print("\nAverage Late Fee by Genre:")
print(avg_late_fee_by_genre)

# Check yourself
assert len(avg_late_fee_by_genre) == checkouts_clean["genre"].nunique()
assert avg_late_fee_by_genre.is_monotonic_decreasing
print("Looks good -- worst genre for late fees:", avg_late_fee_by_genre.idxmax())

'''
Output:
Average Late Fee by Genre:
genre
Dystopian             0.702381
Historical Fiction    0.694444
Adventure             0.632353
Gothic                0.464286
Classic Fiction       0.338710
Name: late_fee, dtype: float64
Looks good -- worst genre for late fees: Dystopian
'''