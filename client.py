import socket

host = 'localhost'
port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))
print("Conectado ao servidor!")

while True:
    mensagem = input("Você: ")
    if mensagem.lower() == 'sair':
        print("Encerrando o chat...")
        break

    client_socket.send(mensagem.encode())

    resposta = client_socket.recv(1024).decode()
    if resposta.lower() == 'sair':
        print("Servidor encerrou a conversa.")
        break
    print("Servidor:", resposta)

client_socket.close()
