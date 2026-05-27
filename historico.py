from datetime import datetime

class Historico:
    def __init__(self):
        self.dataab = datetime.now().strftime("%d/%m/%Y %H:%M")
        self.transferencia_re = []

    def adicionar_transacao(self, des):
        self.transferencia_re.append(des)

    def mostar_data(self):
        print(f'Data de abertura da conta: {self.dataab}')

        for i in self.transferencia_re:
            print(i)