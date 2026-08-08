# Given
monthly_sales = [85000, 120000, 95000, 140000, 75000, 160000]

# sort monthly sales in descending order
descending_sales = sorted(monthly_sales, reverse=True)
print(f"Monthly Sales in Descending Order: {descending_sales}")

# print the values above in 100000
above_100000 = [value for value in monthly_sales if value > 100000]
print(f"Monthly Sales above 100000: {above_100000}")

# list for amount of 13% tax
sales_with_tax = [amount * 1.13 for amount in monthly_sales]
print(f"Monthly Sales with 13% Tax: {sales_with_tax}")

# print total sales amount 
total_sales = sum(monthly_sales)
print(f"Total Sales Amount: {total_sales}")

# print average sales amount
average_sales = total_sales / len(monthly_sales)
print(f"Average Sales Amount: {average_sales: .2f}")

# Output:
'''
Monthly Sales in Descending Order: [160000, 140000, 120000, 95000, 85000, 75000]
Monthly Sales above 100000: [120000, 140000, 160000]
Monthly Sales with 13% Tax: [96049.99999999999, 135600.0, 107349.99999999999, 158199.99999999997, 84749.99999999999, 180799.99999999997]
Total Sales Amount: 675000
Average Sales Amount:  112500.00
'''