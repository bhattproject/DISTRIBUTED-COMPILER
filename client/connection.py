import socket
from common.protocol import encode_message, decode_message

class ClientConnection:
    def __init__(self, server_ip, server_port=9000):
        self.server_ip = server_ip
        self.server_port = server_port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.server_ip, self.server_port))
    
    def send_request(self, action, data):
        message = encode_message(action, data)
        self.socket.send(message.encode())
        response = self.socket.recv(1024).decode()
        return decode_message(response)
