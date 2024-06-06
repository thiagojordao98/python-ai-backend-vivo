from datetime import datetime

class Banco:
    def __init__(self):
        self.saldo = 0
        self.extrato = []
        self.limite_saques = 3
        self.saques_realizados = 0

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            data_atual = datetime.now().strftime("%d/%m/%Y às %H:%M:%S")
            self.extrato.append(f"Depósito: +R${valor:.2f} em {data_atual}")
            print(f"Depósito de R${valor:.2f} em {data_atual} realizado com sucesso!")
        else:
            print("Valor de depósito inválido. Tente novamente.")

    def saque(self, valor):
        if self.saques_realizados >= self.limite_saques:
            print("Operação falhou! Limite de saques diários atingido.")
        elif valor > self.saldo:
            print("Operação falhou! Saldo insuficiente para realizar o saque.")
        elif valor > 500:
            print("Operação falhou! Valor máximo para saque é de R$500.00.")
        else:
            self.saldo -= valor
            data_atual = datetime.now().strftime("%d/%m/%Y às %H:%M:%S")
            self.extrato.append(f"Saque: -R${valor:.2f} em {data_atual}")
            self.saques_realizados += 1
            print(f"Saque de R${valor:.2f} em {data_atual} realizado com sucesso!")

    def mostrar_extrato(self):
        print("---- Extrato ----")
        for operacao in self.extrato:
            print(operacao)
        data_atual = datetime.now().strftime("%d/%m/%Y às %H:%M:%S")
        print(f"Saldo atual em {data_atual} é R${self.saldo:.2f}")
        print("-----------------")
        
    def salvar_extrato(self):
        with open('extrato.txt', 'w') as file:
            file.write("---- Extrato ----\n")
            for operacao in self.extrato:
                file.write(operacao + '\n')
            data_atual = datetime.now().strftime("%d/%m/%Y às %H:%M:%S")
            file.write(f"Saldo atual em {data_atual} é R${self.saldo:.2f}\n")
            file.write("-----------------\n")
        print("Extrato salvo em 'extrato.txt' com sucesso!")

def main():
    banco = Banco()
    
    while True:
        print("\nEscolha uma opção:")
        print("1 - Depósito")
        print("2 - Saque")
        print("3 - Extrato")
        print("4 - Salvar Extrato")
        print("5 - Sair")

        opcao = input("Opção: ")

        if opcao == '1':
            valor = float(input("Digite o valor para depósito: "))
            banco.deposito(valor)
        elif opcao == '2':
            valor = float(input("Digite o valor para saque: "))
            banco.saque(valor)
        elif opcao == '3':
            banco.mostrar_extrato()
        elif opcao == '4':
            banco.salvar_extrato()
        elif opcao == '5':
            print("Obrigado pela preferência! Volte sempre!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
