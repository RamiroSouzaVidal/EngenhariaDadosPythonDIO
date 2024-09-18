class Banco:
    def __init__(self):
        self.agencia = "0001"
        self.usuarios = {}
        self.contas = {}

        # Criar um usuário e uma conta de exemplo na inicialização
        self.criar_usuario("João Silva Santos", "98576645632", "Rua dos Milagres, 1234", "10/05/1978")
        self.criar_conta_corrente("98576645632", "0001")

    def criar_usuario(self, nome, cpf, endereco, data_nascimento):
        if cpf in self.usuarios:
            print("Cadastro falhou! CPF já cadastrado.")
            return

        self.usuarios[cpf] = {
            'nome': nome,
            'endereco': endereco,
            'data_nascimento': data_nascimento
        }
        print(f"Usuário {nome} criado com sucesso!")

    def criar_conta_corrente(self, cpf, numero_conta):
        if cpf not in self.usuarios:
            print("Cadastro falhou! Usuário não encontrado.")
            return

        if numero_conta in self.contas:
            print("Cadastro falhou! Número da conta já existe.")
            return

        self.contas[numero_conta] = {
            'cpf': cpf,
            'saldo': 0,
            'limite': 500,
            'extrato': "",
            'numero_saques': 0,
            'LIMITE_SAQUES': 3
        }
        print(f"Conta corrente {numero_conta} criada com sucesso!")

    def sacar(self, numero_conta, valor):
        conta = self.contas.get(numero_conta)
        if not conta:
            print("Falha na operação! Conta não encontrada.")
            print(f"Contas disponíveis: {list(self.contas.keys())}")  # Depuração
            return

        saldo = conta['saldo']
        limite = conta['limite']
        numero_saques = conta['numero_saques']
        LIMITE_SAQUES = conta['LIMITE_SAQUES']

        if valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif valor > limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif numero_saques >= LIMITE_SAQUES:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            conta['saldo'] -= valor
            conta['extrato'] += f"Saque: R$ {valor:.2f}\n"
            conta['numero_saques'] += 1
            print("Saque realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    def depositar(self, numero_conta, valor):
        conta = self.contas.get(numero_conta)
        if not conta:
            print(f"Contas disponíveis: {list(self.contas.keys())}")  # Depuração
            return

        if valor > 0:
            conta['saldo'] += valor
            conta['extrato'] += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    def extrato(self, numero_conta):
        conta = self.contas.get(numero_conta)
        if not conta:
            print("Falha na operação! Conta não encontrada.")
            print(f"Contas disponíveis: {list(self.contas.keys())}")  # Depuração
            return

        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not conta['extrato'] else conta['extrato'])
        print(f"\nSaldo: R$ {conta['saldo']:.2f}")
        print("==========================================")

def menu():
    banco = Banco()
    
    while True:
        opcao = input("""
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [c] Criar Usuário
        [n] Criar Conta Corrente
        [q] Sair

        => """)
        
        if opcao == 'd':
            numero_conta = input("Número da conta: ")
            valor = float(input("Informe o valor do depósito: "))
            banco.depositar(numero_conta, valor)
            
        elif opcao == 's':
            numero_conta = input("Número da conta: ")
            valor = float(input("Informe o valor do saque: "))
            banco.sacar(numero_conta, valor)
            
        elif opcao == 'e':
            numero_conta = input("Número da conta: ")
            banco.extrato(numero_conta)
        
        elif opcao == 'c':
            nome = input("Nome: ")
            cpf = input("CPF: ")
            endereco = input("Endereço: ")
            data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
            banco.criar_usuario(nome, cpf, endereco, data_nascimento)
        
        elif opcao == 'n':
            cpf = input("CPF do usuário: ")
            numero_conta = input("Número da conta corrente: ")
            banco.criar_conta_corrente(cpf, numero_conta)
        
        elif opcao == 'q':
            break
        
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    menu()
