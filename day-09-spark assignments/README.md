# Spark Capstone Fix the Slow Pipeline

Cleans a messy orders/customers/products dataset, answers six business questions, and speeds up a deliberately de-optimized Spark job with
before/after proof from the Spark UI for every fix.

## Part A Data Cleaning Accounting

Started with 1,020,025 order rows. Removed 20,025 exact duplicate orders, leaving 1,000,000. Removed 15,022 orders with a missing, zero, or negative amount, leaving 984,978. Removed 4,859 orders with an unparseable timestamp, leaving 980,119. Set aside 9,892 orphan order (customer_id notfound in customers) into their own output rather than deleting them, leaving 970,227 final clean orders.

On the customer side, started with 10,300 rows, deduped down to 10,000 by keeping each customer's latest signup_date.

## Part B Business Questions

All six answers are written as CSVs in out/: revenue and order count per country (b1, done in both the DataFrame API and SQL the two plans came out identical), top 10 customers by revenue (b2), revenue per category (b3), average order value per signup-year cohort (b4), monthly revenue trend for 2025 (b5), and the best-selling category per country (b6).

## Part C Performance Before/After

C1, broadcast join. Before: SortMergeJoin, shuffling about 18.5 MiB on the orders side and 519.2 KiB on the customers side. After: forcing F.broadcast() on the customers table switched it to a BroadcastHashJoin, eliminating the shuffle on that side entirely. Screenshots: c1_before.png, c1_after.png.

C2, shuffle partitions. Before: the default 200 shuffle partitions produced 200 tasks for a groupBy with only 8 real country values, most of them empty; the query took 2m 46.6s. After: setting shuffle partitions to 24 (3x our 8 cores) dropped it to 24 tasks and 20.0s, about 8x faster.
Screenshots: c2_before.png, c2_after.png.

C3, skew. Before: with AQE off, the final HashAggregate showed peak memory ranging from 256 KiB (median) up to 2.2 MiB (max), since NP's 60%
share of rows landed in one task. After: turning AQE back on coalesced the mostly-empty partitions, collapsing that spread into a single 70ms/2.2MiB entry. Screenshots: c3_before.png, c3_after.png.

C4, cache. Before: two aggregations on the same filtered/joined DataFrame each re-read and re-processed orders.csv and products.csv from
scratch. After: caching the base DataFrame with .cache() + .count() made the second aggregation hit InMemoryTableScan instead, skipping 9 stages and 55 tasks entirely. Screenshots: c4_before.png, c4_after.png.

C5, UDF vs native. Before: the Python UDF's second run took about 25.8s, with a BatchEvalPython step visible in the plan. After: replacing it with F.when/.otherwise dropped the second run to about 4.4s (~5.9x faster), with no Python step in the plan at all. Counts matched exactly between both versions. Screenshots: c5_before.png, c5_after.png.

## On a 5-node cluster instead of my laptop

The driver would run on one node while the actual work spreads across the other four, so partition counts matter even more — my C2 choice of 24(based on 8 local cores) would need to scale to the cluster's total core count instead. Broadcasting (C1) would still help, but the safe broadcast size threshold would need checking against each executor's memory, not just "is it small." AQE (C3) would matter more, not less, since real skew across physical machines costs actual network transfer, not just local memory pressure. Caching (C4) would need to account for MEMORY_AND_DISK behavior across nodes, and deploy mode (cluster vs client) would decide whether the driver itself lives inside the cluster or on my own machine.

## Challenges Faced

Getting .write.csv() and the Python UDF to work at all on Windows took far longer than any actual Spark logic — a missing winutils.exe, a nearly full C: drive breaking shuffle writes, and finally Windows' fake "python3" Store-alias silently swallowing every UDF worker process. None of it was Spark being hard it was Windows getting in the way of Spark.

## Project Files

capstone.ipynb — main notebook, run top to bottom on a fresh kernel.
out/ — the six Part B CSVs plus orphan_orders/.
screenshots/ — c1_before.png
through c5_after.png, 10 files.
README.md — this file.

## Setup

Install dependencies with pip install pyspark. Generate the data with python make_data.py, which creates data/orders.csv, customers.csv, and
products.csv. On Windows, if a write fails with a Shell.checkHadoopHome error, install winutils.exe/hadoop.dll and set HADOOP_HOME.

## How to Run

Open capstone.ipynb and run all cells top to bottom. Keep the Spark UI tab (localhost:4040) open while running Part C if you want to inspect the
plans yourself.
