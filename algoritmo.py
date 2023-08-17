from classes import *
agencia = Agencia()

def criar_cliente():
    nome = str(input("Digite o nome do cliente: "))
    email = str(input("Digite o email do cliente: "))
    CPF = float(input("Digite o CPF do cliente: "))
    RG = float(input("Digite o RG do cliente: "))
    telefone = float(input("Digite o telefone do cliente: "))
    renda = float(input("Digite a renda do cliente: "))    
    depinicial = float(input("Digite o depósito inicial do cliente: ")) 
    saldo = ()
    cli = nome, email, CPF, RG, telefone, renda, depinicial, saldo
    agencia.novo_cliente(nome)
    return cli

def excluir():
    cliente= str(input("Digite o nome do cliente a ser excluído: "))
    agencia.excluir_cliente(cliente)


def main():
    tam = 30
    while True:
            try:

                print(f"+{'-'*tam}+")
                print(f"|{'BEM VINDO AO SOFTWARE DO BANCO':^{tam}}")
                print(f"+{'-'* tam}+")
                print("O que deseja fazer? \n [1] Cadastrar cliente \n [2] Excluir cliente \n [3] Alterar cliente \n [4] Transferencia \n [5] Depositar \n [6] Sacar \n [7] Consultar saldo \n [8] Agencia \n [9] Sair")
                escolha1 = int(input("> "))
                if escolha1 == 1:
                    print("Você está prestes a criar um novo cliente, insira as informações solicitadas.")
                    criar_cliente()
                    escolha2 = int(input("O que deseja fazer? \n [1] Voltar ao menu \n [2] Adicionar outro cliente \n [3 Fechar o software] \n > "))
                    if escolha2 == 1:
                        main()
                    elif escolha2 == 2:
                        criar_cliente()
                    elif escolha2 == 3:
                            break

                elif escolha1 == 2:
                    print("Você está prestes a excluir um cliente, insira as informações solicitadas.")
                    excluir()

                elif escolha1 == 5:
                    nome_cliente = input("Digite o nome do cliente: ")
                    valor_deposito = float(input("Digite o valor a depositar: "))
                    cliente_encontrado = None

                    for cliente in Agencia._clientes:
                        if cliente.nome == nome_cliente:
                            cliente_encontrado = cliente
                            break

                        if cliente_encontrado:
                            cliente_encontrado.depositar(valor_deposito)
                        else:
                            print("Cliente não encontrado.")

                elif escolha1 == 6:
                    nome_cliente = input("Digite o nome do cliente: ")
                    valor_saque = float(input("Digite o valor a sacar: "))
                    cliente_encontrado = None

                    for cliente in Agencia._clientes:
                        if cliente.nome == nome_cliente:
                            cliente_encontrado = cliente
                            break

                    if cliente_encontrado:
                        cliente_encontrado.sacar(valor_saque)
                    else:
                        print("Cliente não encontrado.")

                elif escolha1 == 7:
                    nome_cliente = input("Digite o nome do cliente: ")
                    cliente_encontrado = None

                    for cliente in Agencia._clientes:
                        if cliente.nome == nome_cliente:
                            cliente_encontrado = cliente
                            break

                    if cliente_encontrado:
                            cliente_encontrado.consultar_saldo()
                    else:
                            print("Cliente não encontrado.")
                    
                elif escolha1 == 9:
                    break
                    
            except Exception:
                print('Problema: Digito não correspondente')  
