from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

data=[]
for job in jobs: 
    post_date = job.find('span', class_="sim-posted").span.text
    if 'few' in post_date: 
        company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '').replace('\n','').replace('\r','').replace('\r\n','')
        skills = job.find('span', class_='srp-skills').text.replace(' ', '').replace('\n','').replace('\r','').replace('\r\n','')
        data.append({'company_name': company_name, 'skills': skills})

print(data)