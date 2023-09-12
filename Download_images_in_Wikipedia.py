import urllib.parse
import requests
import random
import os
from bs4 import BeautifulSoup


def path_image(url_img, dir_path):
    # Create a path and a name for the image we are saving
    image_name = url_img.rsplit('/', 1)[1]
    file_path = os.path.join(dir_path, image_name)
    return file_path


def get_title(url):
    # Create a title for the page
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.title.string.replace(' - Wikipedia', '')
        return title


def download_img(img_url, path):
    response = requests.get(img_url)
    if response.status_code == 200:
        try:
            with open(path, 'wb') as file:
                file.write(response.content)
        except Exception as e:
            # Error while downloading the image
            print(f": {str(e)}")


def get_random_image(url, max_wanted_img):
    # Gets a random URL of the image
    images_url = []
    response = requests.get(url)
    if response.status_code == 200:
        # Gets access to read text
        soup = BeautifulSoup(response.text, "html.parser")
        # Finds all the tags of the images
        all_images = soup.findAll('img', class_="mw-file-element")
        randomly_sampled_images = random.sample(all_images, min(len(all_images), max_wanted_img))
        for image in randomly_sampled_images:
            # If url is incorrect, change it to correct
            src = image.get('src')
            if src.startswith('//'):
                src = "https:" + src
            elif src.startswith('/'):
                src = urllib.parse.urljoin(url, src)
            images_url.append(src)
        return images_url


def random_urls(url, max_wanted_urls, visited_links):
    # Receives random links from the same page
    links_url = []
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        all_urls = soup.find_all('a', href=True)
        randomly_sampled_urls = random.sample(list(set(all_urls) - visited_links), min(len(all_urls), max_wanted_urls))
        for link in randomly_sampled_urls:
            reference = link.get('href')
            if reference.startswith("/wiki"):
                links_url.append(urllib.parse.urljoin(url, reference))
        return links_url


def crawl_wiki(url, directory, depth, width, image_width, visited_links: set):
    visited_links.add(url)
    # Returns a list of URLs ready for download
    image_link = get_random_image(url, image_width)
    path_title = get_title(url)
    current_directory = f"{directory}/{path_title}"
    os.makedirs(current_directory, exist_ok=True)
    for link in image_link:
        file_path = path_image(link, current_directory)
        download_img(link, file_path)
    page_link = random_urls(url, width, visited_links)
    for link in page_link:
        if depth > 0:
            crawl_wiki(link, directory, depth - 1, width, image_width, visited_links)


def main():
    crawl_wiki('https://en.wikipedia.org/wiki/Special:Random', '/home/mefathim-tech-55/Downloads/img_wiki', 2, 2, 20,
               set())


if __name__ == "__main__":
    main()
