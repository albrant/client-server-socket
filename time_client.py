from socket import socket, AF_INET, SOCK_STREAM

CLIENT_SOCK = socket(AF_INET, SOCK_STREAM)
CLIENT_SOCK.connect(('localhost', 8888))
TIME_BYTES = CLIENT_SOCK.recv(1024)
print(f"Текущее время: {TIME_BYTES.decode('utf-8')}")
TEXT = CLIENT_SOCK.recv(1024)
print(f"Получено сообщение от сервера: {TEXT.decode('utf-8')}")
CLIENT_SOCK.close()