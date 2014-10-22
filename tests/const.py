# -*- coding: UTF-8 -*-
import os

class Vars:

    class Login:
        USERNAME = 'tech-testing-ha2-25@bk.ru'
        PASSWORD = os.environ['TTHA2PASSWORD']
        DOMAIN = '@bk.ru'

    class BaseStats:
        NAME = 'Company name'


    class MainStats:
        TITLE = 'Title'
        TEXT = 'Text'
        LINK = 'http://my.mail.ru/apps/indikot'
        IMAGE = os.path.abspath("img.jpg")

    class Time:
        WORK_TIME = u'Рабочее время'
        HOURS_56 = u'Выбрано 56/168 ч'
