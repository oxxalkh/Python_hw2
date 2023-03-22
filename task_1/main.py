import re
import csv

"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт,
осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
info_3.txt и формирующий новый «отчетный» файл в формате CSV.

Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
с данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно
получиться четыре списка — например, os_prod_list, os_name_list,
os_code_list, os_type_list. В этой же функции создать главный список
для хранения данных отчета — например, main_data — и поместить в него
названия столбцов отчета в виде списка: «Изготовитель системы»,
«Название ОС», «Код продукта», «Тип системы». Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data
(также для каждого файла);

Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;

Пример того, что должно получиться:

Изготовитель системы,Название ОС,Код продукта,Тип системы

1,LENOVO,Windows 7,00971-OEM-1982661-00231,x64-based

2,ACER,Windows 10,00971-OEM-1982661-00231,x64-based

3,DELL,Windows 8.1,00971-OEM-1982661-00231,x86-based

Обязательно проверьте, что у вас получается примерно то же самое.

ПРОШУ ВАС НЕ УДАЛЯТЬ СЛУЖЕБНЫЕ ФАЙЛЫ TXT И ИТОГОВЫЙ ФАЙЛ CSV!!!
"""

"""
os_prod_reg = re.compile(r'Изготовитель системы:\s*\S*')
os_prod_list.append(os_prod_reg.findall(data)[0].split()[2])

"""


def get_data():
    file_list = ['info_1.txt', 'info_2.txt', 'info_3.txt']
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    for file in file_list:
        with open(file, encoding='cp1251') as f_n:
            subject = f_n.read()
        os_prod_reg = re.compile(r'Изготовитель системы:\s*\S*')
        os_prod_list.append(os_prod_reg.findall(subject)[0].split()[2])
        os_name_reg = re.compile(r'Название ОС:\s*\S*')
        os_name_list.append(os_name_reg.findall(subject)[0].split()[2])
        os_code_reg = re.compile(r'Код продукта:\s*\S*')
        os_code_list.append(os_code_reg.findall(subject)[0].split()[2])
        os_type_reg = re.compile(r'Тип системы:\s*\S*')
        os_type_list.append(os_type_reg.findall(subject)[0].split()[2])

    main_data = [
        ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
    for i in range(len(os_prod_list)):
        main_data.append([os_prod_list[i], os_name_list[i], os_code_list[i],
                          os_type_list[i]])
    return main_data


def write_to_csv(file_name):
    with open(file_name, 'w') as f_n:
        wr_csv = csv.writer(f_n, delimiter=',')
        data = get_data()
        for i in data:
            wr_csv.writerow(i)


write_to_csv('test.csv')
