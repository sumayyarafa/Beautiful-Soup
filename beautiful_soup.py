import requests
from bs4 import BeautifulSoup
import csv
import time

all_data=[]
for page_num in range(1,51):
    url=f'https://books.toscrape.com/catalogue/page-{page_num}.html'
    print(f"Scraping page {page_num}.")
    response=requests.get(url)
    if response.status_code!=200:
        print(f'page {page_num} not  found')
        break
    soup=BeautifulSoup(response.content,'html.parser')
    all_books=soup.find_all('article', class_="product_pod")
    for book in all_books:
        title=book.h3.a['title']
        price=book.find('p', class_='price_color').text
        rating=book.p['class'][1]
        all_data.append({"title":title,
                         "price":price,
                         "rating":rating,})
        print(f"page {page_num} scraped successfully.")

time.sleep(2)
with open('all_books.csv', 'w', newline='', encoding='utf-8') as file:
    header = ['title', 'price', 'rating']
    writer=csv.DictWriter(file, fieldnames=header)
    writer.writeheader()
    writer.writerows(all_data)
print(f"\n scraping completed. {len(all_data)} books saved to all_books.csv")
















