import requests
from toks import *


group_name = 'DOMAIN_NAME'

cur_id = []
post_ids = []
text_list = []
urlslist = []
#количество получаемых постов 1-100
COUNT = 10


def get_wall_posts():
    url = f"https://api.vk.com/method/wall.get?domain={group_name}&count={COUNT}&access_token={tok2}&v=5.131"
    req = requests.get(url)
    src = req.json()
    # print(req.text)

    posts = src["response"]["items"]
    # Получаем текс, ID постов, ID группы и заносим их в список
    for post in posts:
        post_ids.append(post["id"])
        cur_id.append(post["owner_id"])
        text_list.append(post["text"])

    # формируем ссылки на посты
    for i in post_ids:
        originalUrl = 'https://vk.com/wall' + str(cur_id[0]) + '_' + str(i)
        urlslist.append(originalUrl)

    return urlslist





