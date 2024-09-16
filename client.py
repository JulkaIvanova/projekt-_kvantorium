import socket
from socetFuncs import *

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = "127.0.0.1"
port = 9090
adress = (ip, port)
sock.connect(adress)
try:    
    while True:
        send_data = input("Введите сообщение: ")        
        send(sock, send_data)
        incomming_data = recive(sock, 1024)        
        if incomming_data == "shut_down":
            send_data = "shut_down"            
            send(sock, send_data)
            break        
        else:
            print(f"сообщение от сервера: {incomming_data}")
finally:
    sock.close()    
    print("соединение закрыто")