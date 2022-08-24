import vk_api, json
from vk_api.longpoll import VkEventType, VkLongPoll
from toks import *
from news_agregator import *


vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)


# Функция, которая добавляет кнопку в диалог с ботом
def get_button(text, color):
    return {
        "action": {
            "type": "text",
            "payload": "{\"button\": \"" + "1" + "\"}",
            "label": f"{text}"
        },
        "color": f"{color}"
    }


keyboard = {
    "one_time": False,
    "buttons": [[get_button('Получить новости', 'positive')]]
}
keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))



def sender(id, text):
    vk_session.method('messages.send', {'user_id': id, 'message': text, 'random_id': 0, 'keyboard': keyboard})


# Функция, которая отправляет поток новостей
def main():

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                msg = event.text.lower()
                id = event.user_id

                if msg == 'привет':
                    sender(id, 'Здравствуйте')

                if msg == "получить новости":
                    get_wall_posts()
                    for i in range(COUNT):
                        sender(id, urlslist[i])
                        sender(id, text_list[i])




while True:
    main()
