#Calculadora Básica: Crie uma função que receba dois números como parâmetros.
# exiba o resultado das operações básicas de adição, subtração, multiplicação e divisão.
#3.1 - Crie uma função que receba dois números como parâmetros para cada uma das operações básicas 7
# citadas acima retornando somente o valor das operações.
#3.2 - Crie uma função que faça um menu para o usuário escolher a opção desejada.

#quer saber se quer adição,subtração,multiplicar,divisão

print("Insira dois números,escolha se quer fazer a conta de adição,subtração,multiplicação,divisão ou todas as contas e logo em seguida será exibido o resultado!")
print("")
def menu_calculadora():
    print("Menu calculadora")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Fazer todas as contas")


def escolha_do_numero():
    while True:
        try:
            escolha_numero = int(input("Digite do 1 ao 5: "))
            if escolha_numero >= 1 and escolha_numero <= 5:
                return escolha_numero
            else:
                print("Digite somente do 1 ao 5!!")
        except ValueError:
            print("INFORMAÇÃO INVÁLIDA")


def solicitacao_numero():
    while True:
        try:
            numero1 = float(input("Digite o primeiro número: "))
            numero2 = float(input("Digite o segundo número: "))
            return numero1, numero2
        except ValueError:
            print("DIGITE APENAS NÚMEROS!!")


def conta_adicao(numero1, numero2):
    resultado_soma = numero1 + numero2
    return resultado_soma


def conta_subtracao(numero1, numero2):
    resultado_subtracao = numero1 - numero2
    return resultado_subtracao


def conta_multiplicacao(numero1, numero2):
    resultado_multiplicacao = numero1 * numero2
    return resultado_multiplicacao


def conta_divisao(numero1, numero2):
    resultado_divisao = numero1 / numero2
    return resultado_divisao


def exibir(escolha_do_numero,numero1, numero2):
    if  escolha_do_numero == 1:
        print(f"A soma dos números {numero1} + o número {numero2} = {conta_adicao(numero1, numero2)}")

    elif escolha_do_numero == 2:
        print(f"A subtração dos números {numero1} - o número {numero2} = {conta_subtracao(numero1, numero2)}")

    elif escolha_do_numero == 3:
        print(f"A multiplicação dos números {numero1} * pelo número {numero2} = {conta_multiplicacao(numero1, numero2)}")

    elif escolha_do_numero == 4:
        print(f"A divisão dos números {numero1} / número {numero2} = {conta_divisao(numero1, numero2)}")

    else:
        print(f"A soma dos números {numero1} + o número {numero2} = {conta_adicao(numero1, numero2)}")
        print(f"A subtração dos números {numero1} - o número {numero2} = {conta_subtracao(numero1, numero2)}")
        print(f"A multiplicação dos números {numero1} * pelo número {numero2} = {conta_multiplicacao(numero1, numero2)}")
        print(f"A divisão dos números {numero1} / número {numero2} = {conta_divisao(numero1, numero2)}")


menu_calculadora()

numero_calculadora = escolha_do_numero()
n1, n2 = solicitacao_numero()

exibir(numero_calculadora,n1,n2)