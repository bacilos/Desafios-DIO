menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES =3

while True:

    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("Insira o valor de depósito: "))
        saldo += deposito
        print("Seu saldo atual é de: " +str(saldo)) 
        extrato += f"Depósito de R${deposito:.2f} realizado.\n"
        print(f"Depósito de R${deposito} realizado com sucesso.")


    elif opcao == "s":
        saque = float(input("Insira o valor a ser sacado: "))
        if saque > 500:
            print("O Limite máximo por saque é de R$500,00")
        elif saque > saldo:
            print(f"Você não tem saldo suficiente, seu saldo atual é de apenas R$"+str(saldo))
        elif numero_saques >= LIMITE_SAQUES:
            print("Você excedeu o máximo de 3 saques diários")
        else: 
            saldo -= saque
            numero_saques += 1
            print("Seu saldo atual é de " +str(saldo))  
            extrato += f"Saque de R${saque:.2f} realizado.\n"
            print(f"Saque de R${saque} realizado com sucesso.")  
        


    elif opcao == "e":
        if (extrato == ""):
            print("Não foram realizada transações")
        else: 
            print("\n=============EXTRATO================")
            print(extrato)
            print(f"\n Seu saldo é de R${saldo:.2f}.")
            print("====================================\n")
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")