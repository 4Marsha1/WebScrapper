from bs4 import BeautifulSoup
import requests

BASE_URL = 'https://www.zyte.com'

def fetch_data(path): 
    print(f'{BASE_URL}{path}')
    html_text = requests.get(f'{BASE_URL}{path}').text
    soup = BeautifulSoup(html_text, 'lxml')
    posts = soup.find_all('div', class_='oxy-post')
    data = []
    for post in posts:
        date = post.find('div', class_='oxy-post-image-date-overlay').text.strip()
        title = post.find('a', class_='oxy-post-title').text.strip()
        link =  BASE_URL + post.find('a', class_='oxy-post-title')['href']
        author = post.find('div', class_='oxy-post-meta-author oxy-post-meta-item').text.strip().replace('By ', '')
        data.append({'date': date,'title': title,'author': author,'link': link })

    with open('data/posts.json', 'a') as f:
        for index, post in enumerate(data): 
            title = post['title'].replace('–', '-').replace('’',"'")
            date = post['date']
            author = post['author']
            link = post['link']

            page_num = path.split('/')
            if(len(page_num)<3 and index==0): 
                f.write('[\n')
            f.write("{") 
            f.write(f'"title": "{title}",\n')
            f.write(f'"author": "{author}",\n')
            f.write(f'"date": "{date}",\n')
            f.write(f'"link": "{link}"\n')
            if(len(page_num)>2 and page_num[3]=='26' and index==len(data)-1): 
                f.write('}\n')
            else: f.write("},\n")
            if(len(page_num)>2 and page_num[3]=='26' and index==len(data)-1): 
                f.write(']\n')
    
    next_page = soup.find('a', class_='next')
    if next_page == None: 
        pass
    else: 
        fetch_data(next_page['href'])

if __name__ == '__main__':
    fetch_data('/blog')
