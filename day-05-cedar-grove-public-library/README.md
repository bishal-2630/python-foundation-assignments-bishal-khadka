# Topics Covered

During Day 5,I learned how to process, clean, analyze, and enrich real-world checkout data using Python, Pandas, and public web APIs. The main concepts covered include:

Data Loading and Date Parsing with pd.read_csv
Data Cleaning and Missing Value Imputation (fillna, notnull)
Boolean Indexing and Data Filtering
Grouping and Aggregating Data (groupby, mean, sum)
Fetching Remote Data with requests
Exception Handling (try / except) for Network Resilience
Normalizing and Transposing API Responses (.reset_index, .T)
DataFrame Merging and Joins (pd.merge)

# Exercises

Exercise 01: Data Loading & Parsing (exercise-01-load-data.py)
Exercise 02: Return Rate & Late Fee Cleaning (exercise-02-clean-checkouts.py)
Exercise 03: Genre Late Fee Analysis (exercise-03-genre-analysis.py)
Exercise 04: Real Public API Lookup (exercise-04-real-public-api.py)
Exercise 05: Late Fees by Author (exercise-05-late-fees-by-author.py)

# How to Run

python exercise-01-load-data.py

# Example

python exercise-02-clean-checkouts.py

# What I Learned

During Day 5, I learned how to handle messy dataset scenarios such as missing values and unparsed dates. I practiced creating derived columns, aggregating financial figures across categories, and making live HTTP requests to the Open Library API to fetch external metadata dynamically. I also gained hands-on experience joining secondary DataFrames back onto primary transaction logs using Pandas merges.

# Challenges Faced

Working with external APIs presented new challenges, particularly handling missing fields, non-standard text encodings (such as Cyrillic author names), and potential request failures. Building a fallback mechanism using try / except helped ensure the pipeline remained resilient. I also had to get comfortable managing DataFrame indexes—specifically resetting index labels into standard columns before executing merges.

# Key Takeaways

Learned to parse dates directly during CSV loading.

Imputed missing numeric values with .fillna(0) and generated boolean flags with .notnull().

Used .groupby() along with .mean() and .sum() to extract categorical insights.

Integrated live web data into analysis pipelines using requests.

Implemented resilient fallback patterns to protect against network failures.

Merged distinct DataFrames on shared keys using pd.merge().
