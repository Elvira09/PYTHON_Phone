# 3. Модуль записи в файл и извлечения данных из файла
import create_data
import user_interface
import json

# # запись данных 
def write_data():   # можно позже добавить дату внесения записи
    database = create_data.contact()
    with open('PHONE/database_lower.csv', 'a') as file:
        for key,val in database.items():
            file.write('{}: {}\n'.format(key,val))
        file.write('\n')

    with open('PHONE/database_line.csv', 'a') as file1:
        file1.write('\n')
        for key,val in database.items():
            if key != 'comment':
                file1.write('{}: {} - '.format(key,val))
            else: 
                file1.write('{}: {} '.format(key,val))

    with open('PHONE/database.xml', 'a', encoding='utf-8') as file2:
        file2.write('\n')
        for key, val in database.items():
            file2.write('{}: {}\n'.format(key,val))

    with open("PHONE/database.json", "a") as file3:
        file3.write('\n')
        for key, val in database.items():
            file3.write('{}: {}\n'.format(key,val))         
# f = write_data()


# просмотр всех данных из файла
def view_database():
    with open('PHONE/database.json', 'r') as file:
        lines = file.read()
    print(lines)
# f = view_database()

# поиск контакта 
def find_contact():
    file = open('PHONE/database_line.csv', 'r')
    contact = []
    find = user_interface.get_action_find_contact()
    for line in file:
        if find in line:
            contact.append(line.split('-'))
    if contact == []:
        print('Поиск не дал результата')
    contact = '\n'.join(sum(contact, []))
    return contact
# print(find_contact())

# # НЕ ДОРАБОТАНО  
# изменение контакта
def change_contact():
    with open ('PHONE/database_line.csv', 'r') as file:
        old_data = file.read()
    with open ('PHONE/database_lower.csv', 'r') as file:
        old_data = file.read()
    with open ('PHONE/database.xml', 'r') as file:
        old_data = file.read()
    with open ('PHONE/database.json', 'r') as file:
        old_data = file.read()

    old = input('Введите позицию для изменения: ')
    new = input('Введите новые данные: ')
    new_data = old_data.replace(old, new)

    with open ('PHONE/database_line.csv', 'w') as file:
        file.write(new_data)
    with open ('PHONE/database_lower.csv', 'w') as file:
        file.write(new_data)
    with open ('PHONE/database.xml', 'w') as file:
        file.write(new_data)
    with open ('PHONE/database.json', 'w') as file:
        file.write(new_data)

    # if change_contact != []:
    #     choice = user_interface.get_action_change_contact()
    #     if choice == 1:
    #         result = create_data.get_name()
    #     elif choice == 2:
    #         result = create_data.get_surname()
    #     elif choice == 3:
    #         result = create_data.get_phone()
    #     elif choice == 4:
    #         result = create_data.get_mail()
    #     elif choice == 5:
    #         result = create_data.get_comment()
   
    # return change_contact
# print(change_contact())


# # СОЗДАТЬ ФУНКЦИЮ ПО УДАЛЕНИЮ КОНТАКТА  
# def delet_contact():



