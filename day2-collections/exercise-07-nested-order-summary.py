# Given:

orders = {
    "ORD-001": {
        "customer": "Anisha",
        "amount": 2500,
        "status": "Completed"
    },
    "ORD-002": {
        "customer": "Ravi",
        "amount": 1800,
        "status": "Pending"
    },
    "ORD-003": {
        "customer": "Maya",
        "amount": 3200,
        "status": "Completed"
    }
}

# 1. to print order id and customer name
print("All Orders:")
for order_id, order_details in orders.items():
    print(f"Order: {order_id}, Customer: {order_details['customer']}")

# 2. to print completed orders and total amount of completed orders
print("\nCompleted Orders:")
total_completed = 0 # initialize total amount of completed orders as 0

for order_id, order_details in orders.items():
    if order_details['status'] == "Completed": # for completed orders

       print(f"Order: {order_id}, Customer: {order_details['customer']}, Amount: {order_details['amount']}")
    total_completed += order_details["amount"] # 3. for total amount of completed orders

print(f"Total Completed Order Amount: {total_completed}")


# 4. to print total number of pending orders
pending_count  = 0  # initialize pending order count as 0 

for order_id, order_details in orders.items():
    if order_details['status'] == "Pending": # for pending orders
        pending_count += 1 # for total number of pending orders

print(f"Total Pending Orders: {pending_count}")


# 5. to add a new order to the orders dictionary
orders["ORD-004"] = {
    "customer": "Sagar",
    "amount": 4500,
    "status": "Pending"
}

print("\nNew order added:")
print(orders["ORD-004"])

# Output:
'''
All Orders:
Order: ORD-001, Customer: Anisha
Order: ORD-002, Customer: Ravi
Order: ORD-003, Customer: Maya

Completed Orders:
Order: ORD-001, Customer: Anisha, Amount: 2500
Order: ORD-003, Customer: Maya, Amount: 3200

Total Completed Order Amount: 7500

Total Pending Orders: 1

New order added:
{'customer': 'Sagar', 'amount': 4500, 'status': 'Pending'}
'''