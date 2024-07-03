import socket
import requests
import threading
import queue
from time import sleep, localtime

TCP_IP = "127.0.0.1" # localhost
TCP_PORT = 18
TCP_BUF_SIZE = 1024

SHELLY_IP = "192.168.33.1" # default Shelly IP
SHELLY_KEEPALIVE_INTERVAL_SECONDS = 120

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.bind((TCP_IP, TCP_PORT))
tcp_socket.listen(1)

def toggle_shelly_http(state:bool):
    state_str = "true" if state else "false"

    # Only returns when GET request is responded to by Shelly
    requests.get("http://" + SHELLY_IP + "/rpc/Switch.Set?id=0&on=" + state_str)

    print()
    print(str(localtime().tm_hour).zfill(2) + ":" + str(localtime().tm_min).zfill(2))
    state_str = "ON" if state else "OFF"
    print("SHELLY OUTPUT SET: " + state_str)

toggle_queue = queue.Queue(0)

def worker():
    while True:
        toggle_shelly_http(toggle_queue.get())
        toggle_queue.task_done()
threading.Thread(target=worker, daemon=True).start()

def keepalive_shelly():
    while True:
        state_bool = requests.get("http://192.168.33.1/rpc/Switch.GetStatus?id=0").json()['output']
        state_str = "ON" if state_bool else "OFF"
        
        print()
        print(str(localtime().tm_hour).zfill(2) + ":" + str(localtime().tm_min).zfill(2))
        print("SHELLY OUTPUT STATE: " + state_str)
        sleep(SHELLY_KEEPALIVE_INTERVAL_SECONDS)
threading.Thread(target=keepalive_shelly, daemon=True).start()

(connection, address) = tcp_socket.accept()

while True:
    data = connection.recv(TCP_BUF_SIZE)

    if data == b'':
        break
    data_as_str = data.decode()
    if data_as_str.find("ON") >= 0:
        toggle_queue.put(True)
    if data_as_str.find("OFF") >= 0:
        toggle_queue.put(False)

# Wait for all tasks on queue to be completed
toggle_queue.join()
