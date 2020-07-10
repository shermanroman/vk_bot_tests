from vk_api.longpoll import VkEventType, VkLongPoll
import vk_api
from datetime import datetime
import random

#login, password = '89834178758', 'Supersherman1995qwe'
#vk_session = vk_api.VkApi(login, password)
#vk_session.auth()

token = '015bb3aaf3e01e27cf95859dc2d3f02da595a42e93859985b10a01b8292c3db5f599f5ad628cff49b7604'
vk_session = vk_api.VkApi(token=token)
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('Сообщение пришло в : ' + str(datetime.strftime(datetime.now(),'%H:%M:%S')))
            print('Текст сообщения: ' + str(event.text))
            print("Сообщение пришло от: " + str(event.user_id) + "\n")
            responde = event.text.lower()
            if event.from_user and not (event.from_me):
                if responde == 'привет':
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'О, супер! Так держать. Если напишешь "ты молодец", то заслужишь похвалу', 'random_id': 0})
                elif responde == 'ты молодец':
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Супер! Ты заслужил похвалу! Если напишешь "пока", то я попращаюсь с тобой в ответ', 'random_id': 0})
                elif responde == 'пока':
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Счастливо! Увидимся в следующих версиях!', 'random_id': 0})
                else:
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Привет, друг! Попробуй написать "привет"', 'random_id': 0})
