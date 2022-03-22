#coding=UTF-8
import socket
from threading import Thread

def recebe():
    while True:
        resp = client.recv(1024).decode()
        print(f'Resposta: {resp}')


# SERVER = socket.gethostbyname(socket.gethostname())
SERVER = "localhost"
PORT = 50000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    print('>> CHAT SÍNCRONO CLIENTE x SERVIDOR <<')
    client.connect((SERVER, PORT))
    print('Conectado!')
    

    while True:
        msg = input('Mensagem: ')
        client.send(msg.encode())
        
        if msg == '':
            break
        t = Thread(target=recebe)
        t.start()
        
        

    client.close()
except Exception as e: 
    print(e)
    exit()

