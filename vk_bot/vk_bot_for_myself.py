from vk_api.longpoll import VkEventType, VkLongPoll
import vk_api
from datetime import datetime
import random

login, password = '89834178758', 'Supersherman1995qwe'
vk_session = vk_api.VkApi(login, password)
vk_session.auth()
