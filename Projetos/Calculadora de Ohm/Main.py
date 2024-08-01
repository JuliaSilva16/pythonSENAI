print("Bem vindo(a) ao programa que calcula as medidas eletricas para assim retornar o resultado de sua escolha ")
print("Insira os números,escolha se irá ser:  ")
print("")
print("Digite 1 para calcular a resistência")
print("Digite 2 para calcular a tensão")
print("Digite 3 para calcular a corrente em circuito")
print("Digite 4 para calcular a resistencia resistor")
print("")

resistencia = 1
tensao = 2
corrente = 3
resistencia_re = 4
sair = 0

opcao = float(input("Escolha uma opção: "))

while opcao != 0:

    if opcao == 1:
        while True:
            try:
                tensao1 = float(input("Digite a tensão (V): "))
                if tensao1 > 0:
                    break
            except ValueError:
                print("Valor inválido. Digite um número utilizando o ponto para separa. Ex:1.0")

        while True:
            corrente = float(input("Digite a corrente elétrica (I) ou (A): "))
            if corrente > 0:
                break
            conta = tensao / corrente
            print(f"A resistência é {conta} ohms ")

    elif opcao == 2:
        while True:
            try:
                resistencia = float(input("Dgite a resistência elétrica (R): "))
                if resistencia > 0:
                    break
            except ValueError:
                print("Valor inválido. Digite um número utilizando o ponto para separa. Ex:1.0")

        while True:
            corrente2 = float(input("Digite a corrente elétrica (I) ou (A): "))
            if corrente2 > 0:
                break
            conta2 = resistencia * corrente2
            print(f"A tensão elétrica é {conta2} volts (V)")


    elif opcao == 3:
        while True:
            try:
                tensao2 = float(input("Digite a tensão elétrica (V): "))
                if tensao2 > 0:
                    break
            except ValueError:
                print("Valor inválido. Digite um número utilizando o ponto para separa. Ex:1.0")

        while True:
            resistencia3 = float(input("Digite a resistencia (R): "))
            if resistencia3 > 0:
                break
            conta3 = tensao2 / resistencia3
            print(f"A corrente elétrica é {conta3} amperes")


    elif opcao == 4:
        while True:
            try:
                tensao4 = float(input("Digite a tensão da fonte: "))
                if tensao4 > 0:
                    break
            except ValueError:
                print("Valor inválido. Digite um número utilizando o ponto para separa. Ex:1.0")

                tensao5 = float(input("Digite a tensão de LED:"))
                if tensao5 > 0:
                    break
            except ValueError:
                print("Valor inválido. Digite um número utilizando o ponto para separa. Ex:1.0")

        while True:
                corrente = float(input("Digite a corrente de LED:"))
                if corrente > 0:
                    break

        conta4 = tensao4 - tensao5
        conta5 = conta4 / corrente
        print(f"A resistência necessária para o resistor é {conta5} ohms")

    else:
        print("Opcão inválida")
        print("")

        print("Digite 1 para calcular a resistência")
        print("Digite 2 para calcular a tensão")
        print("Digite 3 para calcular a corrente em circuito")
        print("Digite 4 para calcular a resistencia resistor")

        opcao = float(input("Escolha uma opção: "))
