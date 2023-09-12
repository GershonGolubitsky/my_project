import sys
import csv
from tqdm import tqdm
import requests

HN_GENERAL = 'https://hacker-news.firebaseio.com/v0/'
HN_ITEM = 'item/{}.json?print=pretty'
HN_TOP_STORIES = 'topstories.json?print=pretty'


def get_top_stories():
    responce = requests.get(HN_GENERAL + HN_TOP_STORIES)
    if responce.status_code == 200:
        return responce.json()


def get_story_info(story_id):
    responce = requests.get(HN_GENERAL + HN_ITEM.format(story_id))
    if responce.status_code == 200:
        return responce.json()


def get_all_stories_info(stories_id):
    info = []
    for story_id in stories_id[:5]:
        story_info = get_story_info(story_id)
        info.append(story_info)
    return info


def save_info(stories_info, file):
    keys = stories_info[0].keys()
    with open(file, 'w') as file:
        dict_writer = csv.DictWriter(file, keys, extrasaction='ignore')
        dict_writer.writeheader()
        dict_writer.writerows(stories_info)

def main():
    if len(sys.argv) < 2:
        raise ValueError('No file secified')
    file = sys.argv[1]

    stories_id = get_top_stories()
    stories_info = get_all_stories_info(stories_id)
    save_info(stories_info, file)
main()
