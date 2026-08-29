Day 06 – SQL Assignments

# Topics Covered

During Day 6, I learned how to query, filter, calculate, and analyze employee data using SQL and PostgreSQL. The main concepts covered include:

Selecting data from a table using SELECT
Performing arithmetic calculations on numeric columns
Creating calculated columns using AS
Filtering records with the WHERE clause
Using comparison operators such as >, <, >=, <=, <>, and =
Combining conditions using AND and OR
Filtering multiple values using IN
Filtering ranges using BETWEEN
Pattern matching using LIKE and wildcards (%)
Working with NULL values using IS NULL and IS NOT NULL
Combining multiple filtering conditions
Calculating annual salary and total compensation
Working with employee attributes such as department, city, employment type, performance rating, and employment status

# Exercises

The assignment task.sql file contains 50 SQL exercises based on the employees table.

Exercise 01–06: Arithmetic calculations and calculated columns
Exercise 07–18: Comparison operators and logical filtering
Exercise 19–25: Pattern matching and IN
Exercise 26–33: IN and BETWEEN filtering
Exercise 34–38: NULL, missing values, and non-null filtering
Exercise 39–50: Combined conditions, pattern matching, calculations, and business-rule filtering

# Files

assignment task.sql
Contains the SQL queries for all 50 Day 6 exercises.
employees_postgresql.sql
Contains the PostgreSQL employees table structure and employee data used for the exercises.

# How to Run

Open the SQL script in DBeaver and execute the queries against the PostgreSQL database containing the employees table.
For example:
SELECT \*
FROM employees;
You can also execute individual exercises one at a time.

# Example

-- Find employees whose monthly_salary is greater than 100000.
SELECT \*
FROM employees
WHERE monthly_salary > 100000;

# What I Learned

During Day 6, I learned how to retrieve specific information from a relational database and apply different SQL filtering techniques to employee data. I practiced arithmetic operations, calculated fields, aliases, comparison operators, logical operators, IN, BETWEEN, LIKE, and NULL handling.

# Challenges Faced

One of the main challenges was understanding the difference between NULL, an empty string (''), and text values such as 'None'. I also practiced using parentheses correctly when combining AND and OR conditions.

# Key Takeaways

Created calculated columns using arithmetic operators and AS.
Used WHERE to filter records.
Combined conditions using AND and OR.
Used IN to match multiple values.
Used BETWEEN to filter values within a range.
Used LIKE and % for pattern matching.
Used IS NULL and IS NOT NULL for SQL NULL values.
Learned that NULL, empty strings, and values such as 'None' are different.
Practiced writing SQL queries that combine multiple conditions to solve business-oriented data questions.
