# 1. Модуль взимодействия с пользователем

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

def get_action_find_contact(file):
	choice = input('Введите параметр поиска:  ')
	if not choice in file: 
		choice = input('Параметр поиска введен некорретно, повторите попытку ')
	return choice




