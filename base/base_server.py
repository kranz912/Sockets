import socket

class Base_Server(object):
    """
        Base Server class
    """

    def __init__(self, config):
        self._config = config
        self.run(self._config)

    def run(self,config):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((config.get('Host'), int(config.get('Port'))))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    conn.sendall(data)
            




