import textwrap


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
        
    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_nascimento, endereco):
        super().__init__(endereco) # chama o __init__ da classe Cliente
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento

class Extrato:
    def __init__(self):
        self.transacoes = []
    
    def adicionar_transacao(self, descricao):
        self.transacoes.append(descricao)
    
    def mostrar(self, saldo):
        print("\n==========EXTRATO==========")
        if not self.transacoes:
            print("Não foram realizadas transações")
        else:
            for transacao in self.transacoes:
                print(transacao)
        print(f"\nSaldo atual: R${saldo:.2f}")
        print("==============================\n")

class Conta:
    def __init__(self, numero, agencia, cliente):
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente # objeto do tipo Cliente ou PessoaFisica
        self.saldo = 0.0
        self.extrato = Extrato()
        self.limite = 500.0
        self.saques_diarios = 0
        self.limite_saques = 3
    
    def depositar (self, valor):
        if valor >0:
            self.saldo += valor
            self.extrato.adicionar_transacao(f"Depósito: R${valor:.2f}")
            print(f"Depósito de R${valor:.2f} realizado com sucesso")
        else:
            print("Valor inválido para depósito")

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente")
            return False
        elif valor > self.limite:
            print("Valor excede o limite por saque")
            return False
        elif self.saques_diarios >= self.limite_saques:
            print("Limite de saques diários atingido")
            return False
        else:
            self.saldo -= valor
            self.saques_diarios +=1
            self.extrato.adicionar_transacao(f"Saque: R${valor:.2f}")
            print(f"Saque de R${valor:.2f} realizado com sucesso")
            return True
        
    def mostrar_extrato(self):
         self.extrato.mostrar(self.saldo)

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero=numero, agencia="0001", cliente=cliente)

class Banco:
    def __init__(self):
        self.clientes = []
        self.contas = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def buscar_cliente_por_cpf(self, cpf):
        for cliente in self.clientes:
            if isinstance(cliente, PessoaFisica) and cliente.cpf == cpf:
                return cliente
        return None

    def criar_conta_para_cliente(self, cpf):
        cliente = self.buscar_cliente_por_cpf(cpf)
        if cliente:
            numero_conta = len(self.contas) + 1
            conta = Conta.nova_conta(cliente=cliente, numero=numero_conta)
            cliente.adicionar_conta(conta)
            self.contas.append(conta)
            print(f"Conta criada com sucesso para {cliente.nome}. Número da conta: {numero_conta}")
            return conta
        else:
            print("Cliente não encontrado.")
            return None

    def listar_contas(self):
        for conta in self.contas:
            print("=" * 40)
            print(f"Agência: {conta.agencia}")
            print(f"Número da Conta: {conta.numero}")
            print(f"Titular: {conta.cliente.nome}")
            print("=" * 40)


def menu():
    print("\n=========== MENU ===========")
    print("[u] Novo Usuário")
    print("[c] Criar Conta")
    print("[d] Depositar")
    print("[s] Sacar")
    print("[e] Extrato")
    print("[l] Listar Contas")
    print("[q] Sair")
    return input("Escolha uma opção: ").lower()



def main():
    banco = Banco()

    while True:
        opcao = menu()

        if opcao == "u":
            cpf = input("CPF: ")
            if banco.buscar_cliente_por_cpf(cpf):
                print("Cliente já cadastrado.")
                continue

            nome = input("Nome: ")
            nascimento = input("Data de nascimento (dd-mm-aaaa): ")
            endereco = input("Endereço: ")

            cliente = PessoaFisica(nome=nome, cpf=cpf, data_nascimento=nascimento, endereco=endereco)
            banco.adicionar_cliente(cliente)
            print("Cliente criado com sucesso!")

        elif opcao == "c":
            cpf = input("CPF do cliente: ")
            banco.criar_conta_para_cliente(cpf)

        elif opcao == "d":
            cpf = input("CPF do titular: ")
            cliente = banco.buscar_cliente_por_cpf(cpf)
            if cliente and cliente.contas:
                valor = float(input("Valor do depósito: "))
                cliente.contas[0].depositar(valor)
            else:
                print("Cliente ou conta não encontrada.")

        elif opcao == "s":
            cpf = input("CPF do titular: ")
            cliente = banco.buscar_cliente_por_cpf(cpf)
            if cliente and cliente.contas:
                valor = float(input("Valor do saque: "))
                cliente.contas[0].sacar(valor)
            else:
                print("Cliente ou conta não encontrada.")

        elif opcao == "e":
            cpf = input("CPF do titular: ")
            cliente = banco.buscar_cliente_por_cpf(cpf)
            if cliente and cliente.contas:
                cliente.contas[0].mostrar_extrato()
            else:
                print("Cliente ou conta não encontrada.")

        elif opcao == "l":
            banco.listar_contas()

        elif opcao == "q":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida.")
    

# Chamada da função principal
if __name__ == "__main__":
    main()

