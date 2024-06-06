import socket

TCP_IP = "127.0.0.1" # localhost
TCP_PORT = 18
TCP_BUF_SIZE = 1024

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.connect((TCP_IP, TCP_PORT))
tcp_socket.send(bytes("ON", encoding="utf-8"))

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.connect((TCP_IP, TCP_PORT))
tcp_socket.send(bytes("OFF", encoding="utf-8"))

print("sent message")
