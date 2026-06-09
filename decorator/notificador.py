from abc import ABC, abstractmethod


class Notificador(ABC):
    @abstractmethod
    def enviar(self, mensagem: str) -> None:
        pass

class NotificadorEmail(Notificador):
    def enviar(self, mensagem: str) -> None:
        print(f'Enviando EMAIL: {mensagem}')