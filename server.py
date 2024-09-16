import socket
from socetFuncs import *
import os
import subprocess
import webbrowser
socet = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# ip = "127.0.0.1"
port = 9090
host_name = socket.gethostname()
ip = socket.gethostbyname_ex(host_name)[-1][-1]
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
                    send(connection, subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True).decode(encoding="utf-8", errors="ignore"))
                except:                    
                    send(connection, "Ошибка")

            else:                
                print(f"сообщение от клиенента: {incommig_data}")
                send(connection, input("Введите сообщение: "))    
    finally:
        connection.close()        
        print("Соединение закрыто")