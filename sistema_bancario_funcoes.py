import textwrap


def menu(): 
    menu = """\n
    ============MENU===========
    [d]\t Depositar
    [s]\t Sacar
    [e]\t Extrato
    [u]\t Novo Usuário
    [c]\t Criar conta
    [l]\t Listar contas
    [q]\t Sair
    =====> """
    return input(textwrap.dedent(menu))

def depositar(saldo, deposito, extrato, /):
    if deposito > 0:
        saldo += deposito
        print("Seu saldo atual é de: " + str(saldo)) 
        extrato += f"Depósito de R${deposito:.2f} realizado.\n"
        print(f"Depósito de R${deposito} realizado com sucesso.")
    else:
        print("Operação falhou! O valor informado é inválido")
    return saldo, extrato
    
def sacar(*, saldo, saque, extrato, limite, numero_saques, limite_saques):
    if saque > limite:
        print("O Limite máximo por saque é de R$500,00")
    elif saque > saldo:
        print(f"Você não tem saldo suficiente, seu saldo atual é de apenas R${saldo}")
    elif numero_saques >= limite_saques:
        print("Você excedeu o máximo de 3 saques diários")
    else: 
        saldo -= saque
        numero_saques += 1
        print("Seu saldo atual é de " + str(saldo))  
        extrato += f"Saque de R${saque:.2f} realizado.\n"
        print(f"Saque de R${saque} realizado com sucesso.") 
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    if extrato == "":
        print("Não foram realizadas transações")
    else: 
        print("\n=============EXTRATO================")
        print(extrato)
        print(f"\nSeu saldo é de R${saldo:.2f}.")
        print("====================================\n")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Já existe usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endreço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome" : nome, "data_nascimento" : data_nascimento, "cpf" : cpf, "endereco" : endereco})
    print("==== Usuário criado com sucesso! ====")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia" : agencia, "numero_conta" : numero_conta, "usuario" : usuario }

    print("\n Usuário não encontrado")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
        Agência:\t{conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main(): 

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":

            deposito = float(input("Insira o valor de depósito: "))
            saldo, extrato = depositar(saldo, deposito, extrato)
            

        elif opcao == "s":
            saque = float(input("Insira o valor a ser sacado: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                saque=saque,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques, 
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "u":
            criar_usuario(usuarios)

        elif opcao == "c":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)


        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "l":
            listar_contas(contas)


        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada")

# Chamada da função principal
main()