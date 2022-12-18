from bs4 import BeautifulSoup

with open('index.html','r') as html_file: 
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')

    course_cards = soup.find_all('div', class_='Card')
    data=[]
    for course in course_cards:
        obj={}
        obj['name']=course.h3.text
        obj['price']=course.a.text.split(' ')[-1]
        data.append(obj)
    print(data)