import socket
import requests

TCP_IP = "127.0.0.1" # localhost
TCP_PORT = 18
TCP_BUF_SIZE = 1024

SHELLY_IP = "192.168.33.1" # default Shelly IP

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.bind((TCP_IP, TCP_PORT))
tcp_socket.listen(1)

def toggle_shelly(state:bool):
    state_str = "true" if state else "false"

    # Only returns when GET request is responded to by Shelly
    requests.get(("http://" + SHELLY_IP + "/rpc/Switch.Set?id=0&on=" + state_str))

while True:
    print("waiting for connection . . .")
    (connection, address) = tcp_socket.accept()
    print("connected")

    data = connection.recv(TCP_BUF_SIZE)
    print("recieved data")

    data_as_str = data.decode()
    if data_as_str.find("ON") >= 0:
        toggle_shelly(True)
    elif data_as_str.find("OFF") >= 0:
        toggle_shelly(False)
    else:
        print("no data")
        continue

    connection.send("DONE")
    connection.close()

    print("closed connection")
