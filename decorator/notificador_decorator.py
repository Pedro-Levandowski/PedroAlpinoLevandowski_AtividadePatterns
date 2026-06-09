from notificador import Notificador


class NotificadorDecorator(Notificador):
    def __init__(self, wrapee: Notificador):
        self._wrapee = wrapee

    def enviar(self, mensagem: str) -> None:
        self._wrapee.enviar(mensagem)


class SMSDecorator(NotificadorDecorator):
    def enviar(self, mensagem: str) -> None:
        super().enviar(mensagem)
        print(f"Enviando SMS: {mensagem}")


class SlackDecorator(NotificadorDecorator):
    def enviar(self, mensagem: str) -> None:
        super().enviar(mensagem)
        print(f"Enviando SLACK: {mensagem}")
