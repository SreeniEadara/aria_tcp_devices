import socket
import requests

TCP_IP = "127.0.0.1" # localhost
TCP_PORT = 18
TCP_BUF_SIZE = 1024

SHELLY_IP = "192.168.33.1" # default Shelly IP

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.bind((TCP_IP, TCP_PORT))
tcp_socket.listen(1)

def toggle_shelly_http(state:bool):
    state_str = "true" if state else "false"

    # Only returns when GET request is responded to by Shelly
    requests.get("http://" + SHELLY_IP + "/rpc/Switch.Set?id=0&on=" + state_str)

def enable_bluetooth_shelly():
    requests.get('http://192.168.33.1/rpc/BLE.SetConfig?config={"enable":true,"rpc":{"enable":true}}')

while True:
    print("waiting for instruction . . .")
    (connection, address) = tcp_socket.accept()
    print("connected")

    data = connection.recv(TCP_BUF_SIZE)
    print("recieved data")

    data_as_str = data.decode()
    if data_as_str.find("ON") >= 0:
        toggle_shelly_http(True)
    elif data_as_str.find("OFF") >= 0:
        toggle_shelly_http(False)
    else:
        print("no data")
        continue

    print("performed action")
