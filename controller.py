# Контроллер

import user_interface
import logger
import create_data


def button_click():
    action = user_interface.get_action()

    if action == 1:
        result = logger.write_data()
    elif action == 2:
        result = print('!НЕ ДОДЕЛАНО: вставить модуль  def find_contact() - \
            по поиску контакта') # create_data.find_contact() нужно сделать модуль с поиском и выбором контакта
    elif action == 3:
        result = print('!НЕ ДОДЕЛАНО: вставить модуль def change_contact() - \
            по изменению контакта') # create_data.change_contact() написать модуль по изменению контакта
    elif action == 4:
        result = print('!НЕ ДОДЕЛАНО: вставить модуль def delet_contact() - \
            по удалению контакта') # create_data.delet_contact() написать модуль по удалению контакта
    elif action == 5:
        result = logger.view_database() # показывает все контакты
    
    user_interface.view_data(result)

