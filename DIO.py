import sys
from time import sleep


extrato = 0
limite_saques = 3
quantidade_saques = 0
quantidade_depositos = 0
saque = 0
deposito = 0
menu = """ 
Olá! Seja bem vindo!
O que podemos fazer por você hoje?
***************MENU***************
1-Sacar
2-Extrato
3-Depósito
4-Sair
**********************************
"""

while True :
    opcao = input(menu)

    if int(opcao) == 1 :
        while True :
            saque = input("Insira o valor que deseja sacar:\nR$ ")

            if quantidade_saques < limite_saques :
                if extrato > int(saque) :
                    if int(saque) > 500 :
                        print("O limite do saque é de R$500.00. Escolha um valor dentro do limite.")
                    elif int(saque) <= 0 :
                        print("Por favor, digite um valor válido.")
                    else :
                        print("\nAguarde...")
                        sleep(1)
                        print("Saque realizado com sucesso!\nRetire seu dinheiro no local indicado.")
                        quantidade_saques += 1
                        extrato -= int(saque)
                        break
                else :
                    print("Saldo insuficiente para realizar a operação.")
                    break
            else :
                print("Infelizmente só são permitidos 3 saques diários. Você excedeu o limite.")
                break

    elif int(opcao) == 2 :
        if quantidade_saques > 0 or quantidade_depositos > 0 :
            print(f"""
       ********************EXTRATO BANCÁRIO******************** 

       Valor do saldo em conta: R${extrato}
       Quantidade de saques realizados: {quantidade_saques}
       Quantidade de depósitos realizados: {quantidade_depositos}

       ********************************************************
       """)
        else :
            print(f"""
            ********************EXTRATO BANCÁRIO******************** 

            Não foram realizadas movimentações.
            Valor do saldo em conta: R${extrato}

            ********************************************************
            """)

    elif int(opcao) == 3 :
        while True :
            deposito = input("Qual valor deseja depositar?\nR$ ")
            if int(deposito) < 0 :
                print("Por favor, digite um valor válido.")
            else :
                print("""
        ***************************************ATENÇÃO***************************************
        Por favor, confira se seus dados e o valor do depósito estão corretamente preenchidos 
        no envelope antes de inseri-lo
        *************************************************************************************""")
                sleep(3)
                print("""
        Por favor, insira o envelope no local indicado.""")
                sleep(3)
                print("""
        Depósito realizado com sucesso!""")
                extrato += int(deposito)
                quantidade_depositos += 1
                break

    elif int(opcao) == 4 :
        print("Obrigado e volte sempre!")
        sys.exit()

    else :
        print("Opção inválida. Tente novamente.")
