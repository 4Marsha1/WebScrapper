from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.nykaa.com/').text
soup = BeautifulSoup(html_text, 'lxml')

cards = soup.find_all('div', class_="e1yocmwb3")
data=[]
for card in cards: 
    text = card.find('span', class_="title-text")
    desc = card.find('span', class_="description")
    if text != None: text=text.text
    if desc !=None: desc = desc.text
    data.append({"title": text, "desc": desc})
print(data)