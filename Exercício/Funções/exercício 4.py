#4 - Classificador de triangulo: Crie uma função que receba três números como parâmetros que serão os lados de um triângulo
#retorne se ele é equilátero, isósceles ou escaleno.
#Equilátero se todos os lados possuem a mesma medida.
#Isósceles se dois lados possuem a mesma medida.
#Escaleno se todos os lados possuem medidas diferentes.

print("Digite os tês números dos lados dos triângulos para saber se ele é equilátero, isósceles ou escaleno!")
print("")

def numero_dos_lados():
    while True:
        try:
            lado1 = float(input("Digite o primeiro lado: "))
            lado2 = float(input("Digite o segundo lado: "))
            lado3 = float(input("Digite o terceiro lado: "))
            return lado1, lado2, lado3
        except ValueError:
            print("INFORMAÇÃO INVÁLIDA")


def definicao_triangulos(lado1, lado2, lado3):

    if lado1 == lado2 and lado2 == lado3:
        print("O triângulo é equilátero!")

    elif lado1 == lado2 and lado2 != lado3 or lado2 == lado3 and lado3 != lado1 or lado1 == lado3 and lado3 != lado2:
        print("O triângulo é isósceles")

    else:
        print("O triângulo é escaleno")



lado1, lado2, lado3 = numero_dos_lados()
definicao_triangulos(lado1, lado2, lado3)
