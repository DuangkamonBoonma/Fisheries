import requests
from bs4 import BeautifulSoup
import re

book_url = "https://www.mebmarket.com/"

BASE_HEADERS = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "accept":"*/*",
    "accept-encoding":"gzip, deflate, br, zstd",
    "accept-language":"th-TH,th;q=0.9,pt;q=0.8",
}

response = requests.get(book_url, headers=BASE_HEADERS)
soup = BeautifulSoup(response.text, "html.parser")
content = soup.find_all(class_ = "button_book_list buy_button btn-add-cart-book-309268 ")
content = str(content)

re_values = r'value="฿([^"]+)"'
re_prices = r'price">([^<]+)</p>'

value_list = re.findall(re_values, content)
price_list = re.findall(re_prices, content)

print("Values found:")
print(value_list)
print("Prices found:")
print(price_list)

with open('output.txt', 'w') as f:
    for value, price in zip(value_list, price_list):
        f.write(f"{value}\t{price}\n")