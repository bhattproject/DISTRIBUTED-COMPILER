import socket
import threading
from task_manager import TaskManager
from common.protocol import encode_message, decode_message

class ServerConnection:
    def __init__(self, host='0.0.0.0', port=9000):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen()
        self.task_manager = TaskManager()
    
    def handle_client(self, client_socket):
        while True:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            message = decode_message(data)
            # handle request
        client_socket.close()
    
    def run(self):
        print("Server running...")
        while True:
            client_socket, addr = self.server_socket.accept()
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()
