#Calculadora IMC: Crie uma função que receba dois parâmetros que serão o peso e a altura de uma pessoa e retorne seu IMC.
#IMC = peso / (altura x altura)
#Depois crie outra função que receba um numero como parâmetro que será o IMC e retorne a classificação.

print("Digiteseu peso e sua altura para saber seu IMC! ")
print("")


def solicitacao_altura():
    while True:
        try:
            altura = float(input("Digite sua altura em metros: "))
            return altura
        except ValueError:
            print("INFORMAÇÃO INVÁLIDA,UTILIZE PONTO PARA DIVIDIR ALTURA.EX: 1.69")


def solicitacao_peso():
    while True:
        try:
            peso = float(input("Digite seu peso em kg: "))
            return peso
        except ValueError:
            print("INFORMAÇÃO INVÁLIDA,UTILIZE PONTO PARA DIVIDIR O PESO.EX: 80.50")


def conta_IMC(peso, altura):
    resu_imc = peso / (altura * altura)
    return resu_imc


def classificacao(resu_imc):
    if resu_imc <= 18.5:
        print(f"Seu IMC é de {resu_imc}")
        print("Você está abaixo do peso")

    elif resu_imc > 18.5 and resu_imc <= 24.9:
        print(f"Seu IMC é de {resu_imc}")
        print("Você está no peso ideal")

    elif resu_imc > 25 and resu_imc <= 29.9:
        print(f"Seu IMC é de {resu_imc}")
        print("Você está no com sobrepeso")

    elif resu_imc > 30 and resu_imc <= 34.9:
        print(f"Seu IMC é de {resu_imc}")
        print("Você está com obesidade grau 1")

    elif resu_imc > 35 and resu_imc <= 39.9:
        print(f"Seu IMC é de {resu_imc}")
        print("Você está com obesidade grau 2")
    elif resu_imc > 40:
        print(f"Seu IMC é de {resu_imc}")
        print("Você está com obesidade grau 3")


altura2 = solicitacao_altura()
peso2 = solicitacao_peso()

classificacao(conta_IMC(peso2, altura2))

