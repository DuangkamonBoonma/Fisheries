import requests
from bs4 import BeautifulSoup
import re

list_url = "https://www4.fisheries.go.th/dof/main"

BASE_HEADERS = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "accept":"*/*",
    "accept-language":"en-US,en;q=0.9",
    "accept-encoding":"gzip, deflate, br, zstd",
}

response = requests.get(list_url, headers=BASE_HEADERS)

soup = BeautifulSoup(response.text, "html.parser")

content = soup.find_all('a') 

title_list = []

for element in content:
    title = element.get('title')
    
    if title:
        title_list.append(title)

print(title_list)
