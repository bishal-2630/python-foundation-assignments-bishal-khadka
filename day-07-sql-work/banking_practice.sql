--1. Show every ACTIVE account together with the owning customer's full name and email. Only Active accounts should appear.
select
a.*,
c.full_name
from accounts a
left join (
select
customer_id, 
first_name || ' ' || last_name as full_name 
from customers
) c on a.customer_id = c.customer_id
where a.status = 'Active';


-- 2. Find every customer who currently has NO account at all.
select
c.*
from customers c 
left join  accounts a
on c.customer_id = a.customer_id
where a.customer_id is null;


--3. Find every account whose customer_id does not match any row in the customers table (orphaned accounts).
select
a.*
from accounts a 
left join customers c 
on a.customer_id = c.customer_id
where c.customer_id is null;

--4. Produce one result set of every customer and every account regardless of whether a match exists on either side, and label each row as 'Matched', 'No Account' or 'Missing Customer'.
select
c.customer_id as customer_table_id,
first_name || ' ' || c.last_name as customer_name,
a.account_id,
a.account_type,
a.balance,
case
	when c.customer_id is not null and a.account_id is not null then 'Matched'
	when c.customer_id is not null and a.account_id is null then 'No Account'
	when c.customer_id is null and a.account_id is not null then 'Missing Customer'
end as audit_level
from customers c 
full outer join accounts a
on c.customer_id  = a.customer_id;

--5. For every transaction, show the transaction id, amount, account type, branch and the owning customer's full name - a single query joining three tables.
select
c.first_name || ' ' || c.last_name as full_name,
t.transaction_id,
t.amount,
a.account_type,
a.branch
from transactions t 
join accounts a
on t.account_id  = a.account_id 
join customers c 
on a.customer_id  = c.customer_id


--6. Find the total balance held at each branch, ordered from highest to lowest.
select 
branch,
sum(balance) as total_balance
from accounts a 
group by branch
order by total_balance desc;

	
--7.Find the TOP 5 branches by total balance, counting only Active accounts.
select 
branch,
sum(balance) as total_balance
from accounts a 
where a.status = 'Active'
group by branch
order by total_balance desc
limit 5;


--8. Find account types where the average balance exceeds 50,000. Round the average to 2 decimal places.
select 
account_type,
round(avg(balance)::numeric, 2) as average_balance
from accounts a 
group by(account_type)
having avg(balance) > 50000;

--9. Count how many accounts each customer holds, and list only customers who hold more than 1 account.
select
c.customer_id,
c.first_name || ' ' || c.last_name as full_name,
count(a.account_id ) as total_accounts
from customers c
join accounts a  
on c.customer_id = a.customer_id 
group by c.customer_id, c.first_name, c.last_name 
having count(a.account_id ) > 1
order by total_accounts desc;

--10. Find the branch and account_type combination that has the single highest total transaction amount.
select
a.branch,
a.account_type,
sum(t.amount) as transaction_amount
from accounts a 
join transactions t 
on a.account_id = t.account_id 
group by a.branch, a.account_type 
order by transaction_amount desc
limit 1;


--11.Find every customer whose COMBINED account balance is greater than the overall average balance across all accounts.
select
c.customer_id,
c.first_name || ' ' || c.last_name as full_name,
sum(a.balance) as account_balance
from accounts a
join customers c 
on a.customer_id = c.customer_id 
group by c.customer_id, c.first_name, c.last_name
having sum(a.balance) > (select avg(balance) from accounts)
order by account_balance desc;

--12.Find accounts whose balance is above the average balance of their own account_type (correlated subquery).
select
a.account_id,
a.customer_id,
a.account_type,
a.balance
from accounts a 
where a.balance > (select avg(sub.balance)
from accounts sub
where sub.account_type = a.account_type
)
order by a.account_type, a.balance desc;


--13.Using EXISTS, find every customer who has made at least one 'Withdrawal' transaction.
select
c.customer_id,
c.first_name || ' ' || c.last_name as customer_name
from customers c 
where exists(
select 1
from accounts a 
join transactions t
on a.account_id = t.account_id
where a.customer_id  = c.customer_id
and t.txn_type = 'Withdrawal'
);

--14. Using NOT EXISTS, find every account that has never had a single transaction.
select
a.account_id,
a.customer_id,
a.account_type,
a.balance,
a.branch
from accounts a
where not exists(
select 1
from transactions t
where t.account_id  = a.account_id
);


--15. Using IN with a subquery, list customers who live in a city that has more than 3 customers.
select
c.customer_id,
c.first_name || ' ' || c.last_name as customer_name,
c.city
from customers c 
where c.city in (
select city 
from customers 
group by city 
having count(customer_id) > 3
)
order by c.city, c.customer_id;


--16. Using a subquery in the FROM clause (inline view), compute the number of accounts and average balance per branch, then keep only branches with more than 5 accounts.
select
branch_stats.branch,
branch_stats.total_accounts,
round(branch_stats.average_balance::numeric, 2) as average_balance
from (
select
branch,
count(account_id) as total_accounts,
avg(balance) as average_balance
from accounts
group by branch
) as branch_stats
where branch_stats.total_accounts > 5
order by branch_stats.total_accounts desc;

--17. Combine the customer ids that hold a Savings account with the customer ids that hold a Checking account into ONE de-duplicated list, using UNION.
select customer_id 
from accounts
where account_type = 'Savings'

union

select customer_id
from accounts
where account_type = 'Checking'

order by customer_id

--18. Produce the same combined Savings/Checking customer list but KEEP duplicates (a customer with both types should appear twice), using UNION ALL.
select customer_id 
from accounts
where account_type = 'Savings'

union all

select customer_id
from accounts
where account_type = 'Checking'

order by customer_id

--19. Find customer ids that appear in BOTH the Savings list and the Checking list, using INTERSECT.
select customer_id 
from accounts
where account_type = 'Savings'

intersect

select customer_id
from accounts
where account_type = 'Checking'

order by customer_id

--20. Find customer ids that have a Savings account but do NOT have a Fixed Deposit account, using EXCEPT.
select customer_id 
from accounts
where account_type = 'Savings'

except

select customer_id
from accounts
where account_type = 'Fixed Deposit'

order by customer_id

--21. Write a CTE that calculates each account's total transaction amount, then use it to list only accounts whose total exceeds 100,000.
with account_totals as (
select
account_id,
sum(amount) as total_transation_amount
from transactions 
group by account_id 
) 
select 
account_id,
total_transation_amount
from account_totals
where total_transation_amount > 100000
order  by total_transation_amount desc;


--22. Write a CTE to find the single highest-balance account in EACH branch.
with ranked_accounts as (
select 
branch,
account_id,
customer_id,
balance,
row_number() over(
partition by branch
order by balance desc
) as rank
from accounts
)
select 
branch,
account_id,
customer_id,
balance as highest_balance
from ranked_accounts
where rank = 1
order by branch;


--23. Chain two CTEs together: the first totals Deposit transactions per account, the second joins that total to accounts and returns accounts whose total deposits exceed their current balance.
with account_deposits as(
select
account_id,
sum(amount) as total_deposit_amount
from transactions
where txn_type = 'Deposit'
group by account_id
),

deposits as (
select 
a.account_id,
a.customer_id,
a.account_type,
a.balance as current_balance,
ad.total_deposit_amount as total_deposits
from accounts a 
join account_deposits ad
on a.account_id = ad.account_id
where ad.total_deposit_amount > a.balance    
)

select
account_id,
customer_id,
account_type,
current_balance,
total_deposits
from deposits
order by (total_deposits  - current_balance) desc;

--24. Create a VIEW named active_accounts_view exposing only Active accounts along with the owning customer's full name.
create view active_accounts_view as 
select
a.account_id,
a.customer_id,
c.first_name || ' ' || c.last_name AS customer_name,
a.account_type,
a.balance,
a.branch,
a.status
from accounts a 
join customers c on a.customer_id = c.customer_id
where a.status = 'Active';


--25. Create a MATERIALIZED VIEW named branch_balance_summary that pre-aggregates total balance and account count per branch, and write the command to refresh it CONCURRENTLY.

create materialized view branch_balance_summary as 
select
branch,
count(account_id) as account_count,
sum(balance) as total_balance,
avg(balance) as avg_balance
from accounts
group by branch

--create a unique index
CREATE UNIQUE INDEX idx_branch_balance_summary_branch 
ON branch_balance_summary (branch);

--refresh the materialized view
REFRESH MATERIALIZED VIEW CONCURRENTLY branch_balance_summary;

--26. Using ROW_NUMBER(), return only the MOST RECENT transaction for every account.
with ranked_transactions as (
select 
transaction_id,
account_id,
txn_date,
amount,
txn_type,
row_number() over(
partition by account_id 
order by txn_date desc, transaction_id desc
) as rnk
from transactions 
)
select 
transaction_id,
account_id,
txn_date,
amount,
txn_type
from ranked_transactions
where rnk = 1
order by account_id;


--27.Using RANK(), rank customers by their total account balance so that tied balances share the same rank (with a gap afterward).
with customer_balance as (
select
c.customer_id,
c.first_name || ' ' || c.last_name as customer_name,
sum(a.balance) as total_balance
from customers c 
join accounts a 
on c.customer_id  = a.customer_id 
group by c.customer_id, c.first_name, c.last_name 
)
select
customer_id,
customer_name,
total_balance,
rank() over(
order by total_balance desc 
) as balance_rank
from customer_balance 
order by  balance_rank 

--28. Using DENSE_RANK(), rank branches by total transaction amount with NO gaps in the ranking numbers.
with branch_total as (
select
a.branch,
sum(t.amount) as total_transaction_amount
from accounts a 
join transactions t 
on a.account_id  = t.account_id
group by a.branch
)

select
branch,
total_transaction_amount,
dense_rank() over(
order by total_transaction_amount desc 
) as branch_rank
from branch_total
order by  branch_rank


--29. Using LAG(), show each transaction next to the amount of the PREVIOUS transaction on the same account, ordered by date.
select
account_id,
transaction_id,
txn_date,
txn_type,
amount as current_amount,
lag(amount, 1) over (
partition by account_id
order by txn_date asc, transaction_id asc
) as previous_amount
from transactions 
order by account_id, txn_date;

--30. Using LEAD(), show each transaction next to the amount of the NEXT transaction on the same account, and calculate the difference between them.
select
account_id,
transaction_id,
txn_date,
txn_type,
amount as current_amount,
lead(amount, 1) over (
partition by account_id
order by txn_date asc, transaction_id asc
) as next_amount,
amount - lead(amount, 1) over (
partition by account_id
order by txn_date asc, transaction_id asc
) as amount_difference
from transactions 
order by account_id, txn_date;

--31. Using a running-total window function, show every account's transactions in date order with a cumulative (running) amount.
select
account_id,
transaction_id,
txn_date,
txn_type,
amount,
sum(amount) over(
partition by account_id
order by txn_date asc, transaction_id asc
) as running_total
from transactions
order by account_id, txn_date;

--32.Find duplicate customer records - customers who share the exact same first_name, last_name and dob.
with duplicate_customers as (
select
customer_id,
first_name,
last_name,
dob,
count(*) over (
partition by first_name, last_name, dob
)
as duplicate_count
from customers
)

select
customer_id,
first_name,
last_name,
dob,
duplicate_count
from duplicate_customers
where duplicate_count > 1
order by last_name, first_name, customer_id;


--33. Write ONE query that finds customers missing a city or email (NULL or blank), and a SECOND query that finds orphaned accounts (customer_id with no matching customer row).
select 
customer_id,
first_name,
last_name,
email,
city
from customers
where email is null 
or trim(email) = ''
or city is null 
or trim(city) = '';

--Orphaned accounts
select customer_id from accounts
except
select customer_id from customers;

--or using left join 
select
a.account_id,
a.customer_id,
a.account_type,
a.balance
from accounts a
left join customers c 
on a.customer_id = c.customer_id 
where c.customer_id is null;

--34. Using CASE WHEN, bucket every Active account into 'Low' (< 10,000), 'Medium' (10,000-100,000) or 'High' (> 100,000), then count accounts in each bucket.
with account_category as (
select
account_id,
balance,
case
	when balance < 10000 then 'Low'
	when balance between 10000 and 100000 then 'Medium'
	when balance > 100000 then ' High'
end as balance_bucket
from accounts
where status = 'Active'
)
select 
account_category.balance_bucket,
count(*) as account_count
from account_category
group by balance_bucket 
order by 
case balance_bucket
when 'Low' then 1
when 'Medium' then 2
when 'High' then 3
end;

--35.Write a SAFE transaction block that deducts a 500 maintenance fee from every account with balance > 200,000, inserts a matching 'Fee' row into transactions for each of those accounts, and can be rolled back if anything fails. Always filter UPDATE/DELETE with WHERE.
rollback;

begin;

with eligible_accounts as (
update accounts
set balance = balance - 500.00
where status = 'Active'
and balance > 200000.00
returning account_id
)

insert into transactions (
account_id,
txn_type,
amount,
txn_date
)
select
account_id,
'Fee',
500.00,
current_date::text
from eligible_accounts;

SELECT * 
FROM transactions 
WHERE txn_type = 'Fee' 
AND txn_date = CURRENT_DATE::text;

rollback;


--36. Using NTILE(4), split customers into 4 equal-sized income quartiles ordered by annual_income, then count how many customers fall in each quartile.
with customer_quartile as (
select
customer_id,
annual_income,
ntile(4) over(order by annual_income asc) as quartile
from customers
where annual_income is not null
)
select
quartile,
count(*) as customer_count,
min(annual_income) as min_income,
max(annual_income) as max_income
from customer_quartile 
group by quartile
order by quartile;

--37. Find every customer with a credit_score below 500 who still holds at least one account with a balance above 200,000.
select
c.customer_id,
c.first_name,
c.last_name,
c.credit_score,
from customers c 
where credit_score < 500
and exists (
select 1
from accounts a 
where a.customer_id = c.customer_id 
and a.balance > 200000
);

--38. List every FLAGGED transaction (is_flagged = true) together with the owning customer's name, the branch and the channel used, ordered by amount descending.
select
t.transaction_id,
c.first_name || ' ' || c.last_name as customer_name,
a.branch,
t.channel,
t.amount,
t.txn_date
from transactions t 
inner join accounts a 
on t.account_id  = a.account_id 
inner join customers c
on c.customer_id = a.customer_id 
where t.is_flagged = true
order by amount desc;

--39. Find every customer whose kyc_status is 'Expired' but who still has at least one 'Active' account (a compliance risk).
select
c.customer_id,
c.first_name || ' ' || c.last_name as customer_name,
c.kyc_status,
a.account_id,
a.status as account_status
from customers c 
on c.customer_id  = a.customer_id 
where c.kyc_status = 'Expired' and a.status = 'Active';

--40. Find joint accounts (is_joint_account = true) whose balance is above the AVERAGE balance of all accounts in their own branch (correlated subquery).
select 
a.account_id,
a.branch,
a.balance
from accounts a
where a.is_joint_account = TRUE
and a.balance > (
select avg(sub.balance)
from accounts sub
where sub.branch = a.branch
);
