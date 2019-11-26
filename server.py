from containers import Server, Configs

if __name__ == "__main__":
     Configs.config.override({
         "Host":"127.0.0.1",
         "Port":"5555"
     })
     socket_server = Server.socket_server()
     socket_server.run()