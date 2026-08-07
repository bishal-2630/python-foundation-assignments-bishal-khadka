"""
Exercise: Pipeline Health Status
Student: Bishal Khadka
Day: 1
"""

# Given data
rows_loaded = 9900
rows_failed = 100
runtime_minutes = 30

# for total rows processed
total_rows = rows_loaded + rows_failed

#for failure rates
failure_rate = (rows_failed / total_rows) * 100

# for health status
if failure_rate <= 2 and runtime_minutes <= 20:
    health_status = "Healthy"
elif failure_rate <=5:
    health_status = "Warning"
else:
    health_status = "Critical"

# Display results
print(f"Failure Rate: {failure_rate:.2f}%")
print("Pipeline Status:", health_status)