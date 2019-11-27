from containers import Server,Client,Configs
from multiprocessing import Process
from threading import Thread
if __name__ == "__main__":
     Configs.config.override({
          "Host":"127.0.0.1",
          "Port":"5555"
     })

     socket_server = Server.socket_server()
     socket_client = Client.socket_client()

     Thread(target=socket_server.run).start()
     Thread(target=socket_client.run).start()



