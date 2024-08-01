import random

numero_aleatorio = random.randint(1, 5)
print(numero_aleatorio)

print("        Seja bem vinda(o) ao GameParImpar aonde o jogo do opar e ímpar é mais divertido!!")
print("")
print("               Antes de se iniciar o jogo devesse saber as seguintes intruções:")
print("")
print("1- Os números validos serão de 1 a 5.")
print("2- O usúario deverá escolher se é par ou ímpar.")
print("2- Irá ser solicitado para que o usúario escolha o seu número de 1 a 5.")
print("3- Logo em seguida será mostrado o vencedor. ")
print("")
while True:
    try:
        instru = int(input("Após essas intruções,digite o número 1 para começar: "))
        print("")
        if instru == 1:
            break
        else:
            print("⚠️ Número invalido, tente novamente.Digite novamente o número 1 para iniciar ⚠️")
    except ValueError:
        print("⚠️ Informação inválida. Digite o número corretamente ⚠️")

print("")

while True:
    try:
        escolha_par_impar = int(input("Para escolher ser par ou ímpar, digite 1 para par ou digite 2 para ímpar: "))
        if escolha_par_impar == 1 or escolha_par_impar == 2:
            break
        else:
            print("⚠️ Número invalido, tente novamente.Digite novamente o número 1(par) ou 2(impar) ⚠️")
    except ValueError:
        print("⚠️ Informação inválida. Digite o número corretamente ⚠️")

while True:
    try:
        escolha = int(input("Digite o número de 1 a 5 para jogar: "))
        print(f"O seu número foi {escolha} e o número do sistema foi {numero_aleatorio}")
        if escolha < 1 or escolha > 5:
            print("⚠️ Número invalido, tente novamente.Digite novamente do 1 a 5 ⚠️ ")
        else:
            break
    except ValueError:
        print("⚠️ Informação inválida. Digite o número corretamente ⚠️")

print("")
soma = escolha + numero_aleatorio
resto = soma % 2

while instru == 1:
    if escolha_par_impar != 1:  #impar
        if resto != 0:
            print(f"O número {soma} é impar, você ganhou!!")
        else:
            print(f"O número {soma} é par,você perdeu!!")

    else:  #par
        if resto != 0:
            print(f"O número {soma} é impar,você perdeu!!")
        else:
            print(f"O número {soma} é par, você ganhou!!")
    break

while escolha != 0:
    while True:
        if escolha == numero_aleatorio:
            print("Número misterioso correto.Você ganhou!!")
            print("")
        while True:
            try:
                finalizacao = int(input("Para continuar o jogo basta digitar 1 ou 0 para sair: "))
                if finalizacao == 0:
                    escolha = 0
                    break
                else:
                    print("⚠️ Número invalido, tente novamente.Digite novamente o número 1 para iniciar ⚠️")
            except ValueError:
                print("⚠️ Informação inválida. Digite o número corretamente ⚠️")
