import requests
import pandas as pd
from bs4 import BeautifulSoup
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import re

dof_url = "https://www4.fisheries.go.th/dof/main"

BASE_HEADERS = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "accept":"*/*",
    "accept-language":"en-US,en;q=0.9",
    "accept-encoding":"gzip, deflate, br, zstd",
}

response = requests.get(dof_url, headers=BASE_HEADERS)

soup = BeautifulSoup(response.text, "html.parser")

content = soup.find_all('a') 

title_list = []

for element in content:
    title = element.get('title')
    
    if title and re.search(r'\d+', title):
        title_list.append(title)

with open("output.txt", "w", newline='', encoding='utf-8') as f: 
    for title in title_list:
        f.write(title + "\t")

data = pd.DataFrame({
    'หัวข้อ': ['แผนภูมิโครงสร้างกรมประมง', 'แผนปฏิบัติการเพื่อการบริหารปูม้า', 'แผนพัฒนาบุคลากรกรมประมง', 'นโยบายการกำกับดูแลองค์การที่ดี'],
    'ปี': [2563, 2566, 2566, 2567]
})

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data['หัวข้อ']) 
y = data['ปี'] 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')