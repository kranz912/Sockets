import socket

class Base_Server(object):
    """
        Base Server class
    """

    def __init__(self, config):
        self._config = config

    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self._config.get('Host'), int(self._config.get('Port'))))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    conn.sendall(data)
            
    def send(self,msg):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self._config.get('Host'), int(self._config.get('Port'))))
            s.send(b'Hello, world')
            data = s.recv(1024)
        print('Received', repr(data))