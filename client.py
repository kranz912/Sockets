from containers import Client, Configs

if __name__ == "__main__":
     Configs.config.override({
         "Host":"127.0.0.1",
         "Port":"5555"
     })

     socket_client = Client.socket_client()
     socket_client.send('test')