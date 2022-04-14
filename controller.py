# Контроллер

import user_interface
import logger
import create_data


def button_click():
    action = user_interface.get_action()

    if action == 1:
        result = logger.write_data()
    elif action == 2:
        result = logger.find_contact()
    elif action == 3:
        print('!НЕ ДОДЕЛАНО')
        result = logger.change_contact()
    elif action == 4:
        result = print('!НЕ ДОДЕЛАНО: вставить модуль def delet_contact() - удаление контакта') 
    elif action == 5:
        result = logger.view_database() 
    
    # user_interface.view_data(result)

