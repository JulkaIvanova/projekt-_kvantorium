import socket
def send(socet, text):    
    socet.send(text.encode(encoding="utf-8", errors="ignore"))

def recive(socet, size):    
    return socet.recv(size).decode(encoding="utf-8", errors="ignore")