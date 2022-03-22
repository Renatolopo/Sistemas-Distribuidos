from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread


def accept_conexoes():
    # Esse loop aguarda requerimentos de possíveis clientes
    while True:
        #  Primeiramente o objeto socket deve aceitar um determinado requerimento
        client, client_address = SERVER.accept()
        print(f"{client_address} Conectado\n")
        # O mẽtodo accept devolve um objeto socket que é a conexao
        # e o endereco do cliente que está fazendo a conexao
        enderecos[client] = client_address  # armazena o endereço do cliente no dicionário de endereços
        Thread(target=trata_client, args=(client,)).start()


def trata_client(client):  # Recebe o socket do cliente como argumento
    # Lida com uma única conexão de cliente.
    # Recebendo o nome que meu cliente pretende usar para a conexão através do socket 'client' que foi retornado pelo accept
    name = client.recv(1024).decode("utf8")
    client.send(bytes(name + " está online!", "utf8"))
    msg = f"{name} entrou no chat!"
    broadcast(bytes(msg, "utf8"))
    clients[client] = name  # armazena o nome do cliente no dicionário de nomes (clients)

    while True:
        # loop infinito de comunicacao
        try:
            msg = client.recv(1024)  # recebendo uma mensagem do cliente
            # se uma mensagem não contém instruções para sair, simplesmente transmitimos 
            # a mensagem para outros clientes conectados
            if msg != bytes("{quit}", "utf8"):
                try:
                    broadcast(msg, name+": ")
                except:
                    continue
            else:
                client.close()
                del clients[client]
                broadcast(bytes("%s saiu do chat" % name, "utf8"))
                break
        except:
            client.close()
            del clients[client]
            # broadcast(bytes("%s saiu do chat" % name, "utf8"))
            broadcast(f"{name} saiu do chat".encode("utf8"))
            break


def broadcast(msg, prefix=""):
    # Envia a mensagem para todos os cliente conectados
    # Passamos um prefixo para broadcast () em nossa função trata_client(),
    # fazemos isso para que as pessoas possam ver exatamente quem é o remetente de uma mensagem específica

    for sock in clients:
        sock.send(bytes(prefix, "utf8") + msg)


# Definindo as constantes
clients = {}    # Dicionário responsável por armazenar os clientes
enderecos = {}  # Dicionário responsável por armazenar os enderecos

# Definindo o HOST
HOST = "localhost"

# Definindo número de porta
PORT = 50000

# Tupla (Endereço, Porta)
ADDR = (HOST, PORT)

"""
Criando um objeto socket:
Em que a primeira constante (AF_INET) representa a família do endereco, 
já a segunda constante representa um SOCKET STREAM ou um DATAGRAM (socket.SOCK_DGRAM),
O atributo AF_INET indica que é um protocolo de endereco de  IP
O atributo SOCKET_STREAM que foi passado, indica que é um protocolo de transferencia TCP
A combinacão dos dois atributos indica que está sendo criado um servidor do tipo TCP/IP
"""
SERVER = socket(AF_INET, SOCK_STREAM)

"""Após criado o servidor por meio de um socket, vinculamos a um 
endereco e numero de porta"""
SERVER.bind(ADDR)

"""Iniciando o servidor e aceitando requisicoes"""

def main():
    SERVER.listen(5)
    print("Aguardando conexão...")
    ACCEPT_THREAD = Thread(target=accept_conexoes)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()


if __name__ == "__main__":
    main()