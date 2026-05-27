from historico import Historico

class conta:
    def __init__(self, titular, numero, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = 1000
        self.historico = Historico()

    def depositar(self):
        valor = float(input("Valor a ser adicionado na conta: "))
        self.saldo += valor
        print("Deposito realizado com sucesso.")
        self.historico.adicionar_transacao(f'Deposito de {valor}')

    def sacar(self):
        if self.saldo > 0:
            valor = float(input("Valor de deseja sacar: "))
            self.saldo -= valor
            print("Saque realizado com sucesso.")
            self.historico.adicionar_transacao(f'Saque de {valor}')
        elif self.saldo > 1000:
            while print("Erro."):
                return

    def extrato(self):
        print("Titular: ", self.titular)
        print("Numero: ", self.numero)
        print("Saldo: ", self.saldo)
        print("Limite: ", self.limite)

    # destino: conta que vai receber, valor: valor da tranferencia
    def tranfere(self, destino, valor):
        if self.saldo >= valor:  # verifica se a conta pussui saldo suficiente
            self.saldo -= valor  # remove o valor da conta que enviou
            destino.saldo += valor  # adiciona o dinheiro na conta destino
            return True
            self.historico.adicionar_transacao(f"Transferência de R$ {valor:.2f} para a conta {destino.numero}"
        )
            destino.historico.adicionar_transacao(
            f"Transferência recebida de R$ {valor:.2f} da conta {self.numero}"
        )

        else:
            return False
