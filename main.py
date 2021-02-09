import requests
from bs4 import BeautifulSoup
from pprint import pprint
DESIRED_HUBS = ['дизайн', 'фото', 'web', 'python']

def find_posts():
    response = requests.get('https://habr.com/ru/all/')
    soup = BeautifulSoup(response.text, 'html.parser')
    posts = soup.find_all('article', class_="post post_preview")
    post_list = []
    for post in posts:
        preview = post.find_all('div', class_='post__text')
        previews_text = list(map(lambda hub: hub.text.strip().lower(), preview))
        for preview_text in previews_text:
            if any(dh in preview_text for dh in DESIRED_HUBS):
                dt = post.find('span', class_='post__time').text.strip()
                link = post.find('a', class_='post__title_link')
                link_link = link.attrs.get('href')
                link_text = link.text.strip()
                post_list.append([dt, link_text, link_link])
                break
    pprint(post_list)
if __name__ == '__main__':
    find_posts()
