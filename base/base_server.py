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
            while True:
                conn, addr = s.accept()
                with conn:
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break
                        print("Message from {} : {}".format(addr, repr(data)))
            
    def send(self,receiver,msg):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((receiver, int(self._config.get('Port'))))
            b_msg = bytes(msg,encoding='utf-8')
            s.send(b_msg)