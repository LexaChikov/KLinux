from random import randrange
from config import user_token, group_token

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

# token = input('Token: ')

vk = vk_api.VkApi(token=group_token)
longpoll = VkLongPoll(vk)


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': randrange(10 ** 7), })


def get_user_info(user_id):
    user_info = vk.method('users.get', {'user_id': user_id})
    # print(user_info)
    name = user_info[0]['first_name']
    return name


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:

        if event.to_me:
            request = event.text
            name = get_user_info(event.user_id)

            if request == "hi":
                write_msg(event.user_id, f"Хай, {name}")

            elif request == "bye":
                write_msg(event.user_id, f"Пока(( {name}")
            else:
                write_msg(event.user_id, f"{name}. Bot Не понял вашего ответа...")
