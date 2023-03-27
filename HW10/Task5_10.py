"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess
import chardet

domains = ['yandex.ru', 'youtube.com']

for site in domains:
    args = ['ping', site]
    subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
    i = 0
    for line in subproc_ping.stdout:
        if i <= 10:
            print(line)
            result = chardet.detect(line)
            enc_line = line.decode(result['encoding']).encode('utf-8')
            print(enc_line.decode('utf-8'))
            i += 1
        else:
            print('')
            break
