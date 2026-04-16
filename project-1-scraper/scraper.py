import requests
from bs4 import BeautifulSoup
import openpyxl

# SETUP
base_url = "https://books.toscrape.com/catalogue/page-{}.html"
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Books"
ws.append(["Title", "Price"])

page = 1
# Loop through and extract data
while True:
    url = base_url.format(page)
    response = requests.get(url)

    if response.status_code != 200:
        break

    soup = BeautifulSoup(response.content, "html.parser")
    # Find all books
    books = soup.find_all("article", class_="product_pod")
    for book in books:
        name = book.h3.a.get("title")
        price = book.select_one(".price_color").text
        ws.append([name, price])

    print(f"✅ Scraped page {page}")
    page += 1


# Save the excel file
wb.save("books.xlsx")
print(f"Done! Scraped {page - 1} pages. books.xlsx saved.")
