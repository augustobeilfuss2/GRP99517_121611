class Conta:
    def __init__(self, numero, agencia, nome, data_nascimento, valor):
        self.numero=numero
        self.agenda=agencia
        self.nome=nome
        self.data_nascimento=data_nascimento
        self.valor=valor
    
    def deposito(self):
        print("deposito")
        pass
    def saque(self):
        print("saque")
        pass
    def transferencia(self):
        print("transferencia")
        pass
    def extrato(self):
        print("extrato")
        pass



class ContaCorrente(Conta):
    def __init__(self, limite):
        
        self.limite = limite
    
    def pagar(self):
        print("pagar")
    def cobrar(self):        
        print("cobrar")

class Poupanca(Conta):
    def __init__(self, rendimento, valor_projetado,taxa):
        self.rendimento=rendimento
        self.valor_projetado=valor_projetado
        self.taxa= taxa

    def calcularsaldo(self):
        print("calcularsaldo")
        pass
    def resgatar(self):
        print("resgatar")
        pass




def menuCorrente(conta):
    print("escolha uma funcao")
    print("1-pagar")
    print("2-cobrar")
    print("3-deposito")
    print("4-saque")
    print("5-transferencia")
    print("6-extrato")
    print("7-menu")
    opcao=input()
    if opcao == "1":
        conta.pagar()
        return menuPoupanca(conta)
    if opcao == "2":
        print("teste")
        conta.cobrar()
        return menuPoupanca(conta)
    if opcao == "3":
        conta.deposito()
        return menuPoupanca(conta)
    if opcao == "4":
        conta.saque()
        return menuPoupanca(conta)
    if opcao == "5":
        conta.transferencia()
        return menuPoupanca(conta)
    if opcao == "6":
        conta.extrato()
        return menuPoupanca(conta)
#    if opcao == "7":
 #       return menu()

def menuPoupanca(conta):
    print("escolha uma funcao")
    print("1-calcularSaldo")
    print("2-resgatar")
    print("3-deposito")
    print("4-saque")
    print("5-transferencia")
    print("6-extrato")
    print("7-menu")
    opcao=input()
    if opcao == "1":
        conta.calcularsaldo()
        return menuPoupanca(conta)
    if opcao == "2":
        conta.resgatar()
        return menuPoupanca(conta)
    if opcao == "3":
        conta.deposito()
        return menuPoupanca(conta)
    if opcao == "4":
        conta.saque()
        return menuPoupanca(conta)
    if opcao == "5":
        conta.transferencia()
        return menuPoupanca(conta)
    if opcao == "6":
        conta.extrato()
        return menuPoupanca(conta)
 #   if opcao == "7":
 #       return menu()

