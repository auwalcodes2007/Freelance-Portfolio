import requests
from bs4 import BeautifulSoup
import openpyxl

# Fetch the page and parse HTML
url = "https://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Find all books
books = soup.find_all("article", class_="product_pod")

# Create Excel Workbook
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Books"
ws.append(["Title", "Price"])

# Loop through and extract data
for book in books:
    name = book.h3.a.get("title")
    price = book.select_one(".price_color").text
    ws.append([name, price])

# Save the excel file
wb.save("books.xlsx")
print("Done! books.xlsx has been saved.")
