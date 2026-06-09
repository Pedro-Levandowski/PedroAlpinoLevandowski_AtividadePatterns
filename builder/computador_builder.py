from builder.computador import Computador


class ComputadorBuilder:

    def __init__(self):
        self.computador = Computador()

    def set_processador(self, processador):
        self.computador.processador = processador
        return self

    def set_ram(self, ram):
        self.computador.ram = ram
        return self

    def set_armazenamento(self, armazenamento):
        self.computador.armazenamento = armazenamento
        return self

    def set_placa_de_video(self, placa_de_video):
        self.computador.placa_de_video = placa_de_video
        return self

    def set_sistema_operacional(self, sistema_operacional):
        self.computador.sistema_operacional = sistema_operacional
        return self

    def build(self):
        return self.computador
