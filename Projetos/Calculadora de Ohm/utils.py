print("Bem vindo(a) ao programa que calcula as medidas eletricas para assim retornar o resultado de sua escolha ")
print("Insira os números,escolha se irá ser:  ")
print("")

def menu():
    print("Digite 1 para calcular a resistência")
    print("Digite 2 para calcular a tensão")
    print("Digite 3 para calcular a corrente em circuito")
    print("Digite 4 para calcular a resistencia resistor")
    print("")

resistencia = 1
tensao = 2
corrente = 3
resistencia_resistor = 4
sair = 0


def solicitacao_opcao():
    while True:
        try:
            opcao = int(input("Escolha uma opção: "))
            return opcao
        except ValueError:
            print("Digite apenas números.Ex: 1.")


def resultado_opcao(opcao):
    while opcao != 0:
        break
    while sair == 0:
        break


def solicitacao_resistencia(opcao):
    if opcao == 1:
        while True:
            try:
                tensao = float(input("Digite a tensão (V): "))
                if tensao > 0:
                    break
            except ValueError:
                print("Valor inválido. Digite um número utilizando o ponto para separa. Ex:1.0")

        while True:
            corrente = float(input("Digite a corrente elétrica (I) ou (A): "))
            if corrente > 0:
                break


def solicitacao_tensao(opcao):
    if opcao == 2:
        while True:
            try:
                resistencia = float(input("Dgite a resistência elétrica (R): "))
                if resistencia > 0:
                    break
            except ValueError:
                print("Valor inválido. Digite um número utilizando o ponto para separa. Ex:1.0")

        while True:
            corrente = float(input("Digite a corrente elétrica (I) ou (A): "))
            if corrente > 0:
                break


def solicitacao_corrente(opcao):

    if opcao == 3:
        while True:
            try:
                tensao = float(input("Digite a tensão elétrica (V): "))
                if tensao > 0:
                    break
            except ValueError:
                print("Valor inválido. Digite um número utilizando o ponto para separar. Ex:1.0")

        while True:
            try:
                resistencia = float(input("Digite a resistencia (R): "))
                if resistencia > 0:
                    break
            except ValueError:
                print("Valor inválido. Digite um número utilizando o ponto para separar. Ex:1.0")


def solicitacao_resistenciado_do_resistor(opcao):

    if opcao == 4:
        while True:
            try:
                tensao1 = float(input("Digite a tensão da fonte: "))
                if tensao > 0:
                    break
            except ValueError:
                print("Valor inválido. Digite um número utilizando o ponto para separa. Ex:1.0")

                tensao = float(input("Digite a tensão de LED:"))
                if tensao > 0:
                    break
            except ValueError:
                print("Valor inválido. Digite um número utilizando o ponto para separa. Ex:1.0")

        while True:
                corrente = float(input("Digite a corrente de LED:"))
                if corrente > 0:
                    break


def conta_resistencia(tensao, corrente):
    return tensao / corrente



def conta_tensao(resistencia, corrente):
    return resistencia * corrente



def conta_corrente(tensao, resistencia):
     return tensao / resistencia



def conta_resistenciado_do_resistor(tensao, corrente):
    return (tensao - tensao) / corrente


def exibicao_resultado(opcao):
    print("resultado:")
    if opcao ==1:
        print("Resistência elétrica")
        tensao = solicitacao_resistencia()
        corrente = solicitacao_corrente()
        print(conta_resistencia(tensao, corrente))


    elif opcao == 2:
        print("Tensao elétrica")
        resistencia = solicitacao_resistencia()
        corrente = solicitacao_corrente()
        print(conta_tensao(resistencia, corrente))


    elif opcao == 3:
        print("Corrente elétrica ")
        tensao = solicitacao_tensao()
        resistencia = solicitacao_resistencia()
        print(conta_corrente(tensao, corrente))


    elif opcao == 4:
        print("Resistencia do resistor")
        tensao = solicitacao_tensao()
        resistencia_resistor = solicitacao_resistenciado_do_resistor()
        corrente = solicitacao_corrente()
        print(conta_resistencia_resistor(tensao, resistencia_resistor, corrente))


menu()
escolha_opcao = solicitacao_opcao()
exibicao_resultado(escolha_opcao)
