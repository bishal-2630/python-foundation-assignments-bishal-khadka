-- 1. Display employee_id, monthly_salary, and monthly_salary + 10000 as increased_salary.
SELECT employee_id, monthly_salary, monthly_salary + 10000 AS increased_salary
FROM employees;


-- 2. Calculate reduced_salary by subtracting 5000 from monthly_salary.
SELECT employee_id, monthly_salary, monthly_salary - 5000 AS reduced_salary
FROM employees;


-- 3. Calculate annual_salary by multiplying monthly_salary by 12.
SELECT employee_id, monthly_salary, monthly_salary * 12 AS annual_salary
FROM employees;


-- 4. Calculate average_monthly_bonus by dividing annual_bonus by 12.
SELECT employee_id, annual_bonus, annual_bonus / 12.0 AS average_monthly_bonus
FROM employees;


-- 5. Display age and age % 2 as remainder.
SELECT age, age % 2 AS remainder
FROM employees;


-- 6. Calculate total_compensation as (monthly_salary * 12) + annual_bonus.
SELECT employee_id, monthly_salary, annual_bonus,
       (monthly_salary * 12) + annual_bonus AS total_compensation
FROM employees;


-- 7. Find employees whose monthly_salary is greater than 100000.
SELECT *
FROM employees
WHERE monthly_salary > 100000;


-- 8. Find employees whose age is less than 30.
SELECT *
FROM employees
WHERE age < 30;


-- 9. Find employees with performance_rating greater than or equal to 4.5.
SELECT *
FROM employees
WHERE performance_rating >= 4.5;


-- 10. Find employees whose years_experience is less than or equal to 5.
SELECT *
FROM employees
WHERE years_experience <= 5;


-- 11. Find employees whose department is equal to IT.
SELECT *
FROM employees
WHERE department = 'IT';


-- 12. Find employees whose employment_status is not equal to Active.
SELECT *
FROM employees
WHERE employment_status <> 'Active';


-- 13. Find employees from Kathmandu AND monthly_salary greater than 100000.
SELECT *
FROM employees
WHERE city = 'Kathmandu'
  AND monthly_salary > 100000;


-- 14. Find employees from Kathmandu OR Pokhara.
SELECT *
FROM employees
WHERE city = 'Kathmandu'
  OR city = 'Pokhara';


-- 15. Find employees from IT OR Analytics with performance_rating greater than 4.
SELECT *
FROM employees
WHERE (department = 'IT' OR department = 'Analytics')
  AND performance_rating > 4;


-- 16. Find employees who are NOT remote workers.
SELECT *
FROM employees
WHERE remote_worker = 'No';


-- 17. Find employees with age below 40 AND years_experience above 5 AND employment_status = Active.
SELECT *
FROM employees
WHERE age < 40
  AND years_experience > 5
  AND employment_status = 'Active';


-- 18. Find Full-Time employees with salary above 80000 OR performance_rating above 4.5.
SELECT *
FROM employees
WHERE employment_type = 'Full-Time'
  AND (monthly_salary > 80000 OR performance_rating > 4.5);


-- 19. Find employees whose first_name starts with A.
SELECT *
FROM employees
WHERE first_name LIKE 'A%';


-- 20. Find employees whose first_name ends with a.
SELECT *
FROM employees
WHERE first_name LIKE '%a';


-- 21. Find employees whose first_name contains the letter i.
SELECT *
FROM employees
WHERE first_name LIKE '%i%';


-- 22. Find employees whose last_name starts with S.
SELECT *
FROM employees
WHERE last_name LIKE 'S%';


-- 23. Find employees whose job_title contains the word Analyst.
SELECT *
FROM employees
WHERE job_title LIKE '%Analyst%';


-- 24. Find employees whose email ends with @company.com.
SELECT *
FROM employees
WHERE email LIKE '%@company.com';


-- 25. Find employees working in Kathmandu, Pokhara, or Lalitpur.
SELECT *
FROM employees
WHERE city IN ('Kathmandu', 'Pokhara', 'Lalitpur');

--26. Find employees in the IT, Analytics, or Finance departments.
select * from employees 
where department in ('IT', 'Analytics', 'Finance departments');

--27. Find employees with employment_type Full-Time or Contract.
select * from employees 
where employment_type  in ('Full-Time', 'Contract');

--28. Find employees whose education_level is Bachelor, Master, or PhD.
select * from employees 
where education_level   in ('Bachelor', 'Master', 'PhD');

--29. Find employees aged between 25 and 40.
SELECT *
FROM employees
WHERE age BETWEEN 25 AND 40;

-- 30. Find employees whose monthly_salary is between 80000 and 150000.
select * from employees
where monthly_salary between 80000 and 150000;

--31. Find employees with performance_rating between 3.5 and 4.5.
select * from employees 
where performance_rating between 3.5 and 4.5;

--32. Find employees with years_experience between 3 and 10.
select * from employees 
where years_experience between 3 and 10;

--33. Find employees who joined between 2020-01-01 and 2024-12-31.
SELECT *
FROM employees
WHERE join_date BETWEEN '2020-01-01' AND '2024-12-31';

--34. Find employees whose email is NULL.
SELECT *
FROM employees
WHERE email = '';

--35. Find employees whose phone is NULL.
SELECT *
FROM employees
WHERE phone is null ;

--36. Find employees whose emergency_contact is NULL.
SELECT *
FROM employees
WHERE emergency_contact  is null ;

--37. Find employees whose certification is NULL.
SELECT *
FROM employees
WHERE certification = '' ;

--38. Find employees whose email is NOT NULL AND phone is NOT NULL.
SELECT *
FROM employees
WHERE email != '' and phone is not null ;

--39. Find Active employees from Kathmandu or Lalitpur whose salary is between 90000 and 180000.
SELECT *
FROM employees
WHERE employment_status = 'Active' and city in ('Kathmandu', 'Lalitpur') and monthly_salary between 90000 and 180000;

--40. Find employees in IT or Analytics whose first_name starts with A and performance_rating is at least 4.
SELECT *
FROM employees
WHERE department IN ('IT', 'Analytics')
AND first_name LIKE 'A%'
AND performance_rating >= 4;

--41. Find employees who are not Interns and have completed more than 5 projects.
SELECT *
FROM employees
where employment_type != 'Intern' and projects_completed > 5;

--42. Find employees with NULL certification OR NULL emergency_contact.
SELECT *
FROM employees
WHERE certification in ('None', '')
  OR emergency_contact IS NULL;

--43. Find employees whose job_title contains Manager and whose employment_status is Active.
SELECT *
FROM employees
WHERE job_title LIKE '%Manager%'
and employment_status = 'Active';

--44. Display employees aged between 30 and 50 who work remotely and have salary above 120000.
SELECT *
FROM employees
WHERE age BETWEEN 30 AND 50
  AND remote_worker = 'Yes'
  AND monthly_salary > 120000;

--45. Calculate annual_salary and total_compensation for employees in Finance, IT, and Analytics.
SELECT
    employee_id,
    monthly_salary,
    annual_bonus,
    department,
    monthly_salary * 12 AS annual_salary,
    (monthly_salary * 12) + annual_bonus AS total_compensation
FROM employees
WHERE department IN ('Finance', 'IT', 'Analytics');

--46. Find employees whose promotion_eligible = Yes AND performance_category = Excellent.
SELECT *
FROM employees
where promotion_eligible = 'Yes' and  performance_category = 'Excellent';


--47. Find employees with overtime_hours between 20 and 60 and leave_days_taken less than 15.
SELECT *
FROM employees
where overtime_hours between 20 and 60 and leave_days_taken > 15;

--48. Find employees from cities other than Kathmandu whose first_name contains the letter u.
SELECT *
FROM employees
where city != 'Kathmandu' and first_name like '%u%';

--49. Find employees with monthly_salary > 100000 OR annual_bonus > 150000.
SELECT *
FROM employees
where monthly_salary  > 100000 or annual_bonus > 150000;

--50. Display employee_id, employee_code, first_name, department, monthly_salary, and monthly_salary * 12 as annual_salary for Active employees.
SELECT
    employee_id,
    employee_code,
    first_name,
    department,
    monthly_salary,
    monthly_salary * 12 AS annual_salary
FROM employees
WHERE employment_status = 'Active';
