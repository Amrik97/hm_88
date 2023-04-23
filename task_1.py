import csv
import os
import re


def get_data():
    # создаем списки для хранения данных
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []

    # создаем список для хранения данных отчета
    main_data = [
        ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]

    # перебираем файлы с данными
    for file_name in ['info_1.txt', 'info_2.txt', 'info_3.txt']:
        # открываем файл и считываем данные
        with open(file_name) as file:
            file_data = file.read()

        # ищем значения параметров с помощью регулярных выражений
        os_prod = re.search(r'Изготовитель системы:\s*(.*)', file_data)
        os_name = re.search(r'Название ОС:\s*(.*)', file_data)
        os_code = re.search(r'Код продукта:\s*(.*)', file_data)
        os_type = re.search(r'Тип системы:\s*(.*)', file_data)

        # добавляем значения параметров в соответствующие списки
        os_prod_list.append(os_prod.group(1))
        os_name_list.append(os_name.group(1))
        os_code_list.append(os_code.group(1))
        os_type_list.append(os_type.group(1))

        # добавляем значения параметров в список данных отчета
        main_data.append([os_prod.group(1), os_name.group(1), os_code.group(1),
                          os_type.group(1)])

    return os_prod_list, os_name_list, os_code_list, os_type_list, main_data


def write_to_csv(file_name):
    # получаем данные
    os_prod_list, os_name_list, os_code_list, os_type_list, main_data = get_data()

    # открываем CSV-файл для записи
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)

        # записываем данные в файл
        for row in main_data:
            writer.writerow(row)

    print(f'Данные записаны в файл {file_name}')


# вызываем функцию для записи данных в CSV-файл
write_to_csv('report.csv')