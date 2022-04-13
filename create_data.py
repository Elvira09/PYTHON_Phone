# 2. Модуль создания данных
import uuid


import user_interface



def un_id():
    unid = int(uuid.uuid1())
    return unid
# print(un_id()) 

def get_name():
    name = input('Введите имя:  ')
    return name
# print(get_name())

def get_surname():
    surname = input('Введите фамилию:  ')
    return surname
# print(get_surname())

def get_phone(): # можно позже добавить проверку ввода номера
    phone = input('Введите номер телефона:  ')
    return phone
# print(get_phone())

def get_mail(): # можно позже добавить проверку ввода адреса
    mail = input('Введите адрес электронной почты:  ')
    return mail
# print(get_mail())

def get_comment():
    comment = input('Введите комментарий:  ')
    return comment
# print(get_comment())

# объединение внесенных данных в одну карточку контакта 
def contact():
    database = \
	    {
 		'unid': un_id(),    
		'name': get_name(),
		'surname': get_surname(),
		'phone': get_phone(),
		'mail': get_mail(),
		'comment': get_comment()
 	    }
    return database
# print(contact())


# # СОЗДАТЬ ФУНКЦИЮ ПО ИЗМЕНЕНИЮ КОНТАКТА  
# def change_contact():

# # СОЗДАТЬ ФУНКЦИЮ ПО УДАЛЕНИЮ КОНТАКТА  
# def delet_contact():

 # СОЗДАТЬ  ФУНКЦИЮ  ПО ПОИСКУ КОНТАКТА  
def find_contact():
    file = open('PHONE/database_line.csv', 'r')
    lst = []
    for line in file:
        find = user_interface.get_action_find_contact(file)

        if find in line:
            lst.append(line.split('-'))
        # else:
        #     print('Параметр поиска введен некорретно, повторите попытку ')
    ls = '\n'.join(sum(lst, []))
    return ls

print(find_contact())