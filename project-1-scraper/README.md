# 📚 Book Scraper — books.toscrape.com

A Python web scraper that collects the title and price of every book
across all 50 pages of books.toscrape.com and exports the data to a
clean Excel file.

## 🚀 What it does
- Loops through all 50 pages automatically
- Extracts book title and price from each page
- Saves 1000 books into a formatted Excel file (books.xlsx)

## 🛠 Tech Stack
- Python 3.x
- Requests
- BeautifulSoup4
- OpenPyXL

## ▶️ How to run

# Install dependencies
pip install -r requirements.txt

# Run the scraper
python scraper.py

## 📁 Output
An Excel file `books.xlsx` with two columns:
| Title | Price |
|-------|-------|
| Book name... | £12.99 |

## 💼 Use Case
Businesses use scrapers like this to monitor competitor pricing,
track product catalogues, or gather market data automatically.

