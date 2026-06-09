class Computador:
    def __init__(self):
        self.processador = "N/A"
        self.ram = "N/A"
        self.armazenamento = "N/A"
        self.placa_de_video = "N/A"
        self.sistema_operacional = "N/A"

    def __str__(self):
        return (f"Processador: {self.processador}\n"
                f"RAM: {self.ram}\n"
                f"Armazenamento: {self.armazenamento}\n"
                f"Placa de vídeo: {self.placa_de_video}\n"
                f"Sistema operacional: {self.sistema_operacional}\n")
