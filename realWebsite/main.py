from bs4 import BeautifulSoup
import requests
import time

print('Enter skills that you are not interested in')
not_interested_skill = input('>')
print('Filtering out...')

def find_jobs(): 
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for index,job in enumerate(jobs): 
        post_date = job.find('span', class_="sim-posted").span.text
        if 'few' in post_date: 
            skills = job.find('span', class_='srp-skills').text.replace(' ', '').strip()
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '').strip()
            more_info = job.header.h2.a['href']
            if not_interested_skill not in skills:
                with open(f'data/{index}.text', 'w') as f:
                    f.write(f"Company name: {company_name}\n")
                    f.write(f"Skills: {skills}\n")
                    f.write(f"More Info: {more_info}\n")
                print(f"File Saved: {index}.txt")

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 0.1
        print(f'Waiting {time_wait} minutes...')
        time.sleep(60*time_wait)