import random

numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio)

print("        Seja bem vinda(o) ao EnigmaSolver aonde o jogo de adivinhação é mais divertido!!")
print("")
print("                Antes de se iniciar o jogo devesse saber as seguintes intruções:")
print("")
print("1-O jogo irá escolher um número e não será mostrado.")
print("2- Os números serão sorteados de 0 a 100.")
print("3- A cada chute feito,será informado se o número é maior ou menor que o número sorteado misterioso.")
print("")

while True:
    try:
        instru = int(input("Após essas intruções,digite o número 1 para começar: "))
        print("")
        if instru == 1:
            break
        else:
            print("⚠️ Número invalido, tente novamente.Digite novamente o número 1 para iniciar ⚠️  ")
    except ValueError:
        print("⚠️ Informação inválida. Digite o número corretamente ⚠️")

print("")

while True:
    try:
        solicitacao = int(input("Digite o número que você acha que é o número misterioso: "))
        if solicitacao >= 1 and solicitacao <= 100:
            break
        else:
            print("⚠️ Número invalido, tente novamente ⚠️")
            print(" ↳ Digite novamente o número que você considera o número misterioso entre o 1 e o 100. ")
    except ValueError:
        print("⚠️ Informação inválida. Digite o número corretamente ⚠️ ")

print("")

while solicitacao != 0:
        while True:
            if numero_aleatorio == solicitacao:
                print("Número misterioso correto.Você ganhou!!")
                print("")
                while True:
                    try:
                        finalizacao = int(input("Para continuar o jogo basta digitar 1 ou 0 para sair: "))
                        if  solicitacao == 0 or solicitacao == 1:
                            break
                        else:
                            print("⚠️ Número invalido, tente novamente⚠️  ")
                            print(" ↳ Digite novamente o número 1 para iniciar ou 0 para sair. ")
                    except ValueError:
                        print("⚠️ Informação inválida. Digite o número corretamente (1 ou 0) ⚠️ ")

            elif numero_aleatorio > solicitacao:
                print("O número misterioso é 𝐦𝐚𝐢𝐨𝐫 que o número digitado.Tente novamente!")
                print("")
            elif numero_aleatorio < solicitacao:
                print("O número misterioso é 𝐦𝐞𝐧𝐨𝐫 que o número digitado.Tente novamente!")
                print("")
            else:
                print("Obrigada(o) por jogar")

                while True:
                    try:
                        instru = int(input("Bem vinda(0) de volta ,digite o número 1 para começar: "))
                        print("")
                        if instru == 1:
                            break
                        else:
                            print("⚠️ Número invalido, tente novamente.Digite novamente o número 1 para iniciar ⚠️  ")
                    except ValueError:
                        print("⚠️ Informação inválida. Digite o número corretamente ⚠️")
            while True:
                try:
                    solicitacao = int(input("Digite o número que você acha que é o número misterioso: "))
                    if solicitacao >= 1 and solicitacao <= 100:
                        break
                    else:
                        print("⚠️ Número invalido, tente novamente ⚠️")
                        print(" ↳ Digite novamente o número que você considera o número misterioso entre o 1 e o 100. ")
                except ValueError:
                    print("⚠️ Informação inválida. Digite o número corretamente ⚠️ ")
