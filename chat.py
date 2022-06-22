import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from datetime import datetime
import time
import random

session = vk_api.VkApi(token='af091035c708de6b930568c760eeffe7f76013735c9f2041686ab66b1f14ffac6ca81cc2210d6492cf6b3')
session_api = session.get_api()
longpoll = VkLongPoll(session)

hello_list = ('И тебе привет!',
              'Привет',
              'Доброго времени суток')
film_list=('Тихоокеанский рубеж',
           'Бесславные ублюдки',
           'Поезд в Пусан',
           'Красная жара',
           'Аватар',
           'Мстители: Эра Альтрона',
           'Мгла',
           'Нечто',
           'Дюнкерк',
           'По соображениям совести',
           'Пила',
           'Хэллоуин',
           'Оно',
           'Поворот не туда',
           'Мстители: Финал',
           'Люди в черном',
           'Плохие парни',
           'Цельнометаллическая оболочка',
           'Звездный десант',
           'Варкрафт')
photo_list=('photo110604170_456240782',
           'photo110604170_456240781',
            'photo110604170_456240780',
            'photo110604170_456240606',
            'photo110604170_456240347',
            'photo110604170_456241149',
            'photo110604170_456241172')



while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('Сообщение пришло в: ', event.datetime)
            print('Текст сообщения: ', event.text)
            response=event.text.lower()
            if event.from_user and not event.from_me:
                    if response.find('привет') >= 0 or response.find('здравствуй') >=0 or response.find('хэллоу') >=0 :
                        time.sleep(random.uniform(0.5, 3.0))
                        session.method('messages.send',
                                       {'user_id':event.user_id,
                                        'message':random.choice(hello_list),
                                        'random_id':'0'})
                    elif response.find('как дела') >= 0:
                        session.method('messages.send',
                                       {'user_id':event.user_id,
                                        'message':'',
                                        'random_id':'0',
                                        'sticker_id': '9045'})
                    elif response.find('фото') >= 0:
                        session.method('messages.send',
                                       {'user_id':event.user_id,
                                        'message':'',
                                        'random_id':'0',
                                        'attachment': 'photo110604170_456241655'})
                    elif response.find('музыка') >= 0:
                        session.method('messages.send',
                                       {'user_id':event.user_id,
                                        'message':'',
                                        'random_id':'0',
                                        'attachment': 'audio110604170_456239628'})
                    elif response.find('выбери фильм') >=0:
                        session.method('messages.send',
                                       {'user_id':event.user_id,
                                        'message':random.choice(film_list),
                                        'random_id':'0'})
                    elif response.find('воспоминания') >=0:
                        session.method('messages.send',
                                       {'user_id':event.user_id,
                                        'message':'',
                                        'random_id':'0',
                                        'attachment': random.choice(photo_list)})
