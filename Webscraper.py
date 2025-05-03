import requests
from bs4 import BeautifulSoup

# Step 1: Send a request to the website
url = "http://books.toscrape.com/"
response = requests.get(url)

# Step 2: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Step 3: Find all book containers (each book is inside <article class="product_pod">)
books = soup.find_all("article", class_="product_pod")

# Step 4: Loop through each book and extract its title
print("Book Titles:\n")
for book in books:
    title = book.h3.a["title"]  # title is stored in the 'title' attribute of the <a> tag
    print(title)
