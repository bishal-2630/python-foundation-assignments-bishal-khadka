"""
Exercise: Late Fee By Author
Student: Bishal Khadka
Day: 7
"""

import pandas as pd
import requests


checkouts_df = pd.read_csv('day-05-cedar-grove-public-library/checkouts.csv', parse_dates=['checkout_date', 'due_date', 'return_date'])
checkouts_clean = checkouts_df.copy()
checkouts_clean["is_returned"] = checkouts_clean["return_date"].notnull()
checkouts_clean["late_fee"] = checkouts_clean["late_fee"].fillna(0)

BACKUP_BOOK_FACTS = {
    "Pride and Prejudice": {"author": "Jane Austen", "first_publish_year": 1813},
    "To Kill a Mockingbird": {"author": "Harper Lee", "first_publish_year": 1960},
    "The Great Gatsby": {"author": "F. Scott Fitzgerald", "first_publish_year": 1925},
    "The Catcher in the Rye": {"author": "J. D. Salinger", "first_publish_year": 1951},
    "1984": {"author": "George Orwell", "first_publish_year": 1949},
    "Brave New World": {"author": "Aldous Huxley", "first_publish_year": 1932},
    "Frankenstein": {"author": "Mary Shelley", "first_publish_year": 1818},
    "Jane Eyre": {"author": "Charlotte Bronte", "first_publish_year": 1847},
    "Moby Dick": {"author": "Herman Melville", "first_publish_year": 1851},
    "The Hobbit": {"author": "J. R. R. Tolkien", "first_publish_year": 1937},
    "War and Peace": {"author": "Leo Tolstoy", "first_publish_year": 1869},
    "Crime and Punishment": {"author": "Fyodor Dostoevsky", "first_publish_year": 1866},
}

#uses open library API
OPEN_LIBRARY_API = "https://openlibrary.org/search.json"


def get_book_facts(title):
    try:
        response = requests.get(OPEN_LIBRARY_API, params={"q": title})
        response.raise_for_status()
        data = response.json()
        first_doc = data["docs"][0]
        
        return {
            "author": first_doc["author_name"][0],
            "first_publish_year": first_doc["first_publish_year"]
        }
    except (requests.RequestException, KeyError, IndexError):
        return BACKUP_BOOK_FACTS.get(title, {"author": "Unknown", "first_publish_year": None})

records = {}
for title in checkouts_clean["book_title"].unique():
    records[title] = get_book_facts(title)

book_facts_df = pd.DataFrame(records).T 

facts_reset = book_facts_df.reset_index().rename(columns={"index": "book_title"})
checkouts_with_author = checkouts_clean.merge(facts_reset, on="book_title", how="left")

late_fee_by_author = checkouts_with_author.groupby("author")["late_fee"].sum().sort_values(ascending=False)

# Check yourself
assert len(checkouts_with_author) == len(checkouts_clean)
assert late_fee_by_author.is_monotonic_decreasing
print("Looks good -- costliest author:", late_fee_by_author.idxmax())

'''
Output:
Looks good -- costliest author: Aldous Huxley
'''