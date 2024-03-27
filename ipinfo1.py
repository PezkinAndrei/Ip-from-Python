import ipinfo
import os
from time import *
os.system('color 4')
while True:
    # Получаем IP-адрес из командной строки
    try:
        ip_address = str(input('Введите IP адрес:'))
    except IndexError:
        ip_address = None
     
    # Вставьте свой токен доступа сюда
    access_token = ''
     
    # Создаем объект для работы с сервисом IPinfo
    handler = ipinfo.getHandler(access_token)
     
    # Получаем информацию об IP-адресе
    details = handler.getDetails(ip_address)
     
    # Выводим полученные данные
    for key, value in details.all.items():
        print(f"{key}: {value}")
    sleep(10)
    os.system('cls')
    

