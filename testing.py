from classes import *

numero= input("numero")
agencia= input("agencia")
nome= input("nome")
data_nascimento= input("data-nascimento")
valor= input("valor")
conta=Conta(numero,agencia,nome,data_nascimento,valor)
def addUser():
    numero= input("numero")
    agencia= input("agencia")
    nome= input("nome")
    data_nascimento= input("data-nascimento")
    valor= input("valor")
    conta=Conta(numero,agencia,nome,data_nascimento,valor)
    contas= contas.append(conta)


bool= input("operar na 1-corrente ou 2-poupanca")

if bool == "1" or bool == "2":
    if bool =="1":
        limite=input("limite da conta:")
        corrente=ContaCorrente(limite)
        
        menuCorrente(corrente)
        
        pass

    if bool =="2":
        rendimento=input("rendimento:")
        valorProjetado=input("valorProjetado:")
        taxa=input("taxa:")
        poupanca=Poupanca(rendimento, valorProjetado, taxa)
        menuPoupanca(poupanca)

        pass
else:
    print("valor invalido")
