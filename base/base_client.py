import socket

class Base_Client(object):
    """ 
        Base Client class
  
    """
    def __init__(self, client):
        self._client = client

    def run(self):
        msg = None
        while True:
            print("message :")
            msg = input()
            self._client.send(msg)