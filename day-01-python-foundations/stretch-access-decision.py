"""
Exercise: Access Decision
Student: Bishal Khadka
Day: 1
"""

# User information
user_role = "pilot"
is_active = True
requested_dataset = "sales_data"

# Allowed roles
allowed_roles = ["analyst", "scientist", "engineer"]

# Restricted datasets
restricted_datasets = ["salary_data", "personal_data"]

#Check access
if not is_active:
    print("Access Denied: User is not active.")
elif user_role not in allowed_roles:
    print(f"Access Denied: User role '{user_role}' is not allowed.")
elif requested_dataset in restricted_datasets:
    print(f"Access Denied: Dataset '{requested_dataset}' is restricted.")
else:
    print("Access Granted: User has permission to access the requested dataset.")