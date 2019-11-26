from dependency_injector import providers, containers
from base.base_server import Base_Server

class Configs(containers.DeclarativeContainer):
    config = providers.Configuration('config')

class Server(containers.DeclarativeContainer):
    socket_server = providers.Singleton(Base_Server,Configs.config)

