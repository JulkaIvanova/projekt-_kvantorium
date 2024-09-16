import socket
import random
from socetFuncs import *
import os
import subprocess
import webbrowser
socet = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# ip = "127.0.0.1"
port = 9090
host_name = socket.gethostname()
ip = 'localhost'
adres = (ip, port)
socet.bind(adres)
socet.listen(1)
while True:
    print("Ожидание подключения...")    
    connection, client_adress = socet.accept()
    try:        
        print(f"Подключенно к {client_adress}")
        while True:            
            incommig_data = recive(connection, 1024)
            if incommig_data == "shut_down":                
                send(connection, "shut_down")
                break
            elif incommig_data == "system":                
                send(connection, "Отправьте команду cmd")
                cmd = recive(connection, 1024)                
                resalt = os.system(command=cmd)
                if resalt == 0:                    
                    send(connection, "Команда выполнена успешна")
                else:                    
                    send(connection, "Ошибка")

            elif incommig_data == "check_output":                
                send(connection, "Отправьте команду cmd")
                cmd = recive(connection, 1024)
                try:
                    send(connection,
                         subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True).decode(encoding="utf-8",
                                                                                                   errors="ignore"))
                except:
                    send(connection, "Ошибка")
            elif incommig_data == 'balance':
                webbrowser.open_new('https://rutube.ru/video/c6cc4d620b1d4338901770a44b3e82f4/')
                send(connection, 'Успешно')
            elif incommig_data == 'clicker':
                webbrowser.open_new('https://julkaivanova.github.io/Clicer.github.io/')
                send(connection, 'Успешно')
            elif incommig_data == 'random':
                memes=['https://i.pinimg.com/564x/d1/4d/d4/d14dd4abb33386cc0eae8fffae1ca9f6.jpg','''https://i.pinimg.com/564x/94/4b/b6/944bb65a20985c75692fac8233b73a95.jpg'''
                    ,'https://i.pinimg.com/564x/b3/9d/fa/b39dfabc24a161ec75b10cf45d5b56af.jpg','https://i.pinimg.com/736x/36/c2/70/36c27032516d03a62333bc4227c1f223.jpg',
                       '''https://i.pinimg.com/564x/4d/3c/bb/4d3cbb99a42dde333a1353fc838d388d.jpg''']
                send(connection, 'Успешно')

                random_memes=random.randint(0,len(memes)-1)
                webbrowser.open_new(memes[random_memes])




            else:                
                print(f"сообщение от клиенента: {incommig_data}")
                send(connection, input("Введите сообщение: "))    
    finally:
        connection.close()        
        print("Соединение закрыто")
