# Given datasets:

dataset_a = {
    "customer",
    "sales",
    "product",
    "employee"
}

dataset_b = {
    "sales",
    "product",
    "supplier",
    "inventory"
}

# for all datasets
all_datasets = dataset_a | dataset_b
print(f"All Datasets: {all_datasets}")

#common datasets
common_datasets = dataset_a & dataset_b
print(f"Common Datasets: {common_datasets}")

# unique datasets in dataset_a
unique_datasets_a = dataset_a - dataset_b
print(f"Unique Datasets in Dataset A: {unique_datasets_a}")

# unique datasets in dataset_b
unique_datasets_b = dataset_b - dataset_a
print(f"Unique Datasets in Dataset B: {unique_datasets_b}")

# Output:
'''
All Datasets: {'customer', 'product', 'sales', 'inventory', 'supplier', 'employee'}
Common Datasets: {'sales', 'product'}
Unique Datasets in Dataset A: {'customer', 'employee'}
Unique Datasets in Dataset B: {'inventory', 'supplier'}
'''