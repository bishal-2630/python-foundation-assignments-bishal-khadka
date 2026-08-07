
"""
Exercise: Sales Summary
Student: Bishal Khadka
Day: 1
"""

product_name = "Mechanical Keyboard"
unit_price = 3500
quantity_sold = 8
discount_percentage = 0.20

print(f'Product: {product_name}')

# Calculate the gross sales 
gross_sales = unit_price * quantity_sold
print(f'Gross Sales: {gross_sales: .2f}')

# Calculate the discount amount
discount_amount = gross_sales * discount_percentage
print(f'Discount Amount: {discount_amount: .2f}')

# Calculate the net sales
net_sales = gross_sales - discount_amount
print(f'Final Sales: {net_sales: .2f}')