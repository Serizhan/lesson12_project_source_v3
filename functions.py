import json
from json import JSONDecoder


def upload_posts():
    try:
        with open('posts.json', 'r') as file:
            profiles = json.loads(file.read())
        return profiles
    except JSONDecoder:
        return "Файл не удается преобразовать"


def search_post(s):
    result = []
    for post in upload_posts():
        if s.lower() in post['content']:
            result.append(post)
    return result


def load_post(post):
    new_posts = upload_posts()
    new_posts.append(post)
    with open('posts.json', 'w') as outfile:
        json.dump(new_posts, outfile, ensure_ascii=False)
    return


def is_filename_allowed(filename):
    check_list = {'png', 'jpg', 'jpeg'}
    file_check = filename.split(".")[-1]
    if file_check in check_list:
        return True
    return False
