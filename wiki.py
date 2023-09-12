import requests
from bs4 import BeautifulSoup
import random
import os
import urllib.parse

URL = 'https://en.wikipedia.org/wiki/Special:Random'
URL_DIR = '/home/mefathim-tech-55/Downloads/img_wiki'
MAX_IMG = 20
MAX_LINK = 3

def path_image(url_img, url_dir):
    image_path_url = url_img.rsplit('/', 1)[-1]
    return os.path.join(url_dir, image_path_url)

def fix_url(url):
    if url.startswith('//'):
        return 'https:' + url
    return url

def download_img(url_img, url_dir):
    # וודא שה-URL מתחיל ב-"http://" או "https://"
    if not url_img.startswith(('http://', 'https://')):
        # הוסף תקדם "https:"
        url_img = 'https:' + url_img.lstrip('/')

    response = requests.get(url_img)
    file_path = path_image(url_img, url_dir)

    if response.status_code == 200:
        try:
            with open(file_path, 'wb') as file:
                file.write(response.content)
        except Exception as e:
            print(f"שגיעה בזמן הורדת התמונה: {str(e)}")

def wiki_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # זה יזרוק שגיעה אם הבקשה נכשלת
        html = response.text
        return html
    except Exception as e:
        print(f"שגיעה בזמן גישה לדף: {str(e)}")
    return None

def titles_wiki(html_content):
    if html_content is not None:
        soup = BeautifulSoup(html_content, 'html.parser')
        title = soup.title
        if title is not None:
            title_text = title.string.strip() if title.string else 'untitled'
            return (' ', title_text)
    return None

def random_image(html_content, max_img):
    if html_content is not None:
        soup = BeautifulSoup(html_content, 'html.parser')
        img_tags = soup.find_all('img')
        num_img = len(img_tags)
        if num_img < max_img:
            return [img['src'] for img in img_tags]
        else:
            selected_img = random.sample(img_tags, max_img)
            return [img['src'] for img in selected_img]
    return []

def random_links(html_content, max_link, url, max_img):
    images_url = []
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        all_images = soup.findAll('img', class_="mw-file-element")
        randomly_sampled_images = random.sample(all_images, min(len(all_images), max_img))
        for image in randomly_sampled_images:
            src = image.get('src')
            src = fix_url(src)  # תשים לב לקרוא את הפונקציה fix_url שהוספנו כאן
            if not src.startswith(('http://', 'https://')):
                src = urllib.parse.urljoin(url, src)
            images_url.append(src)
    return images_url

def mk_dir(path):
    try:
        os.mkdir(path)
    except FileExistsError:
        print(f"התיקייה כבר קיימת: {path}")
    except Exception as e:
        print(f"שגיעה בזמן יצירת התיקייה: {str(e)}")

def recursive_wiki_page(depth, max_link, max_img, visited_links, url, url_dir):
    if depth > 0 and url not in visited_links:
        visited_links.add(url)
        html_content = wiki_html(url)
        title = titles_wiki(html_content)
        if title is not None:
            path_dir = url_dir
            path_new_dir = os.path.join(path_dir, title[1])
            mk_dir(path_new_dir)
            img_one_page = random_image(html_content, max_img)  # תשנה ל-max_img
            for one_img in img_one_page:
                path = path_image(one_img, path_new_dir)
                download_img(one_img, path)
            links = random_links(html_content, max_link, url, max_img)  # תוסיף את max_img
            for link in links:
                recursive_wiki_page(depth - 1, max_link, max_img, visited_links, link, path_new_dir)

def main():
    depth = 2
    max_link = 3
    url_dir = URL_DIR
    url = URL
    max_img = MAX_IMG
    visited_links = set()
    recursive_wiki_page(depth, max_link, max_img, visited_links, url, url_dir)

if __name__ == '__main__':
    main()