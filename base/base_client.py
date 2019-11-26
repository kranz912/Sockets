import socket

class Base_Client(object):
    """ 
        Base Client class
  
    """
    def __init__(self, client):
        self._client = client

    def send(self, msg):
        self._client.send(msg)