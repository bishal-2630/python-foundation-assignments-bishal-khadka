# Day 4: File Handling, Error Handling & Logging

## Topics Covered

During Day 4, I learned how to work with files safely and handle errors effectively in Python. The main concepts covered include:

- File reading and writing
- Using `with open(...) as f:`
- Reading and writing text files
- CSV file handling with the `csv` module
- JSON data handling with the `json` module
- `try`, `except`, `else`, and `finally`
- Custom exceptions
- Logging with Python's `logging` module
- Validating user input and data quality
- Handling missing or invalid files and records
- Writing more reliable and robust programs

## Exercises

1. Line & Word Counter
2. Inventory Value from CSV
3. Filtering a JSON Library Catalog
4. Custom Exception for User Registration
5. Order Pipeline with Logging

## How to Run

Open the notebook in VS Code and run each exercise in order:

```bash
Assignment_File_Error_Logging.ipynb
```

Each section includes setup code to generate the sample files needed for the task. After that, you write the solution in the provided function stub and test the results.

## What I Learned

During this assignment, I learned how to read and write files correctly, work with CSV and JSON data, and build safer programs with error handling. I practiced using `try/except` blocks to catch runtime problems, and I used the `logging` module to record useful information and errors while processing data.

I also learned how custom exceptions help improve code clarity and validation. These exercises reinforced the idea that good programs should not only work when inputs are valid, but also handle unexpected data and file issues gracefully.

## Challenges Faced

One of the main challenges was understanding how CSV values are read as strings and how to convert them properly before doing calculations. I also had to pay attention to the difference between valid data and invalid data when processing records in a loop.

Understanding when to use `try/except`, `raise`, and logging was another important learning step. By practicing these patterns in realistic data-processing tasks, I became more confident in writing code that is easier to debug and maintain.

## Key Takeaways

- Learned how to read and write files using Python safely.
- Worked with the `csv` module to process tabular data.
- Worked with the `json` module to read and write structured data.
- Used `try/except` to handle exceptions and invalid input.
- Created custom exceptions for more precise validation.
- Used Python logging to track events and errors.
- Improved my understanding of writing robust, production-ready Python programs.
