"""
2. Задание на закрепление знаний по модулю json. Есть файл orders
в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий
его заполнение данными.

Для этого:
Создать функцию write_order_to_json(), в которую передается
5 параметров — товар (item), количество (quantity), цена (price),
покупатель (buyer), дата (date). Функция должна предусматривать запись
данных в виде словаря в файл orders.json. При записи данных указать
величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json()
с передачей в нее значений каждого параметра.

ПРОШУ ВАС НЕ УДАЛЯТЬ ИСХОДНЫЙ JSON-ФАЙЛ
ПРИМЕР ТОГО, ЧТО ДОЛЖНО ПОЛУЧИТЬСЯ

{
    "orders": []
}


вам нужно подгрузить JSON-объект
и достучаться до списка, который и нужно пополнять
а потом сохранять все в файл
"""

import json

filename = 'orders.json'


def write_order_to_json(item, quantity, price, buyer, date):
    with open(filename, encoding="utf-8") as f_n:
        dict_j = json.loads(f_n.read())

    dict_j['orders'].append(
        {'item': item, 'quantity': quantity, 'price': price,
         'buyer': buyer, 'date': date})

    with open(filename, "w", encoding="utf-8") as f_n:
        json.dump(dict_j, f_n, indent=4, separators=(',', ': '),
                  ensure_ascii=False)

    print(f'Данные добавлены в {filename}')


write_order_to_json('Компьютер', '1', '567', 'Жерновой',
                    '30.04.2023')
write_order_to_json('Ноутбук', '1', '432', 'Стругацкий',
                    '22.04.2023')
