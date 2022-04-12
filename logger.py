# 3. Модуль записи в файл и извлечения данных из файла
import create_data

# ДОДЕЛАТЬ:
    # запись данных в JSON 
    # def write_data_json():

# # запись данных 
def write_data():   # можно позже добавить дату внесения записи
    database = create_data.contact()
    with open('PHONE/database_lower.csv', 'a') as file:
        file.write('\n')
        for key,val in database.items():
            file.write('{}: {}\n'.format(key,val))
    with open('PHONE/database_line.csv', 'a') as file1:
        file1.write('\n')
        for key,val in database.items():
            file1.write('{}: {} - '.format(key,val))
    with open('PHONE/database.xml', 'a', encoding='utf-8') as file2:
        file2.write('\n')
        for key, val in database.items():
            file2.write('{}: {}\n'.format(key,val))              
# f = write_data_csv()


# просмотр всех данных из файла
def view_database():
    with open('PHONE/database_lower.csv') as file:
        lines = file.read()
    print(lines)
# f = view_database()




