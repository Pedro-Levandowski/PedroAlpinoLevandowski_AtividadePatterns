from notificador import NotificadorEmail
from notificador_decorator import SMSDecorator, SlackDecorator

if __name__ == "__main__":
    notificador_1 = NotificadorEmail()
    notificador_2 = SlackDecorator(NotificadorEmail())
    notificador_3 = SlackDecorator(SMSDecorator(NotificadorEmail()))

    notificador_1.enviar('Olá')
    print('')
    notificador_2.enviar('Promoção')
    print('')
    notificador_3.enviar('Sistema fora')
