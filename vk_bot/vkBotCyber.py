from vk_api.longpoll import VkEventType, VkLongPoll
import vk_api
from datetime import datetime
import random

token = 'твой токен'
vk_session = vk_api.VkApi(token=token)
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('Сообщение пришло в : ' + str(datetime.strftime(datetime.now(),'%H:%M:%S')))
            print('Текст сообщения: ' + str(event.text))
            print(event.user_id)
            responde = event.text.lower()
            if event.from_user and not (event.from_me):
                if responde != '1':
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Текст вывода бота', 'random_id': 0})
