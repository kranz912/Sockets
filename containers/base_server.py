import socket



class Server(object):
    """
        Base Server class
    """
    Host ='127.0.0.1'
    PORT ='5555'

    

    def run(conn,addr):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((Server.HOST, Server.HOST))
        s.listen()
        conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    conn.sendall(data)
        




