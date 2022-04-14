# 1. Модуль взимодействия с пользователем
import create_data

# вывод на консоль
def view_data(data):
	print(data)
	
# получаем действие от пользователя
	# ломается, если введено не целое число или символы
def get_action():
	print('Создать новый контакт: 			нажмите 1\n'
    	'Найти контакт: 				нажмите 2 \n'
        'Изменить контакт: 			нажмите 3\n'
        'Удалить контакт: 			нажмите 4\n'
		'Посмотреть все контакты:  		нажмите 5\n')
	choice = int(input('Выберите вариант: '))
	# print()
	if choice < 1 or choice > 5:
		choice = int(input('Некорректный ввод, сделайте выбор повторно:  '))		
	return choice
# print(get_action())

def get_action_find_contact():
	choice = input('Введите параметр поиска:  ')
	print()
	return choice
# print(get_action_find_contact())

def get_action_change_contact():
	print('Изменить имя: 			нажмите 1\n'
    	'Изменить фамилию: 		нажмите 2 \n'
        'Изменить телефон: 		нажмите 3\n'
        'Изменить электронную почту: 	нажмите 4\n'
		'Изменить комментарий:  		нажмите 5\n')
	choice = int(input('Выберите вариант: '))
	if choice < 1 or choice > 5:
		choice = int(input('Некорректный ввод, сделайте выбор повторно:  '))	
	return choice
# print(get_action_change_contact())
