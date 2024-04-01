import pyfiglet
import time
import ipinfo
import os
import socket
os.system('color 4')
def get_local_ip():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print(local_ip)
text = 'GatechIp'
result = pyfiglet.figlet_format(text, font='slant')
while True:
    print(result)
    print('Command:')
    print('1.Search by IP')
    print('2.Find out your IP')
    com  = int(input('Number of command:'))
    if com == 1:
        # Получаем IP-адрес из командной строки
        try:
            ip_address = str(input('Enter your IP:'))
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
            a = (f"{key}: {value}")
            print(a)
            if a == 'bogon: True':
                print('This IP is local!!!')
            else:
                None
        
        time.sleep(10)
        os.system('cls')
    else:
        get_local_ip()
        time.sleep(10)
        os.system('cls')
        
