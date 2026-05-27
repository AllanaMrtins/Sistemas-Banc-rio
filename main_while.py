import os
import time
from Conta import conta
from historico import Historico

def limpar_tela():
    os.system("cls || clear")

def carregar():
    print("\nCarregando", end ="")
    for i in range(5):
        print(".", end="", flush=True)
        time.sleep(0.4)
    print("\n")

def menu():
    lisa_contas = []
    limpar_tela()
    print("=" * 40)
    print("         SISTEMA BANCARIO")
    print("=" * 40)

    qtd = int(input("Quantas contas deseja adicionar: "))
    cont = 0

    while cont < qtd:
        limpar_tela()
        print("=" * 40)
        print(f'        CONTA {cont + 1}')
        
        titular = input("Titular: ")
        numero = int(input("Numero: "))
        saldo = float(input("Saldo: "))

        nova_conta = conta(titular, numero, saldo, Historico)
        lisa_contas.append(nova_conta)
        print("\nConta criada com sucesso!")
        carregar()
        cont += 1

    while True:
        limpar_tela()
        print("=" * 40)
        print("         MENU")
        print("=" * 40)
        print("\n---- MENU ----")
        opcoes = ["1 - Depositar",
                  "2 - Sacar",
                  "3 - Extrato",
                  "4 - Transferir",
                  "5 - Mostar Contas",
                  "6 - Consultar historico",
                  "7 - Consultar historico por conta",
                  "8 - Sair"]
        
        for opcao_menu in opcoes:
            print(opcao_menu)
            time.sleep(0.1)

        print("=" * 40)

        opcao = int(input("Escolha uma opção: "))
        carregar()

        if opcao == 1:
            numero = int(input("Numero da conta: "))
            for c in lisa_contas:
                if c.numero == numero:
                    c.depositar()

        elif opcao == 2:
            numero = int(input("Numero da conta: "))
            for c in lisa_contas:
                if c.numero == numero:
                    c.sacar()

        elif opcao == 3:
            numero = int(input("Numero da conta: "))
            for c in lisa_contas:
                if c.numero == numero:
                    c.extrato()

        elif opcao == 4:
            conta_original = int(input("Conta origem: "))
            destino = int(input("Conta destino: "))
            valor = float(input("Valor da tranferencia: "))

            conta_origem = None  # quer dizer nenhum valor
            conta_destino = None

            for c in lisa_contas:
                if c.numero == conta_original:
                    conta_origem = c
                if c.numero == destino:
                    conta_destino = c

            if conta_origem != None and conta_destino != None:
                result = conta_origem.tranfere(conta_destino, valor)
                if result == True:
                    print("Transferencia realizada.")
                else:
                    print("Saldo insuficiente.")

        elif opcao == 5:
            for c in lisa_contas:
                print("\n--- Contas ---")
                c.extrato()

        elif opcao == 6:
            for c in lisa_contas:
                print("------------")
                print(f'Titular: {titular}')
                print(f'Numero: {numero}')
                print(f'Saldo: {saldo}')

                c.historico.mostar_data()
                
        elif opcao == 7:
            numero = int(input("Numero da conta: "))
            for c in lisa_contas:
                if c.numero == numero:
                    c.historico.mostar_data()

        elif opcao == 8:
            print("Saindo...")
            carregar()
            break
        else:
            print("Opção invalida.")
        input("Pressione ENTER para continuar...")

menu()