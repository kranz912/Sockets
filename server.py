import socket
from base_server import Server

class Socket_Server(Server):

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((Server.HOST, Server.HOST))
        s.listen()

        conn, addr = s.accept()
        Server.run(conn,addr)