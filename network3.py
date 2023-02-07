import socket
import pickle

class Network:
    def __init__(self, server, port):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.server = "194.87.214.126"
        self.server = server
        self.port = port
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def getP(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(40960).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(data)
            return pickle.loads(self.client.recv(40960))
        except socket.error as e:
            print(e)