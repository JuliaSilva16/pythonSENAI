#Solicite ao usuário três números inteiros e mostre o maior deles.
print("")
print("Digite três números inteiros para saber quem será o maior deles!")
print("")

while True:
    try:
        numero1 = int(input("Digitre o primeiro número inteiro: "))
        break

    except ValueError:
        print("Informação inválida")

while True:
    try:
        numero2 = int(input("Digite o segundo número inteiro : "))
        break

    except ValueError:
        print("Informação inválida")

while True:
    try:
        numero3 = int(input("Digite o terceiro número interito:"))
        break
    except ValueError:
        print("Informação inválida")

if numero1 > numero2 and numero2 > numero3:
    print(f" O primerio número { numero1} é o MAIOR!")
elif numero1 < numero2 and numero2 > numero3:
    print(f"O Segundo número  {numero2} é o MAIOR! ")
elif numero1 > numero2 and numero2 > numero3:
    print(f"O terceiro número {numero3} é o MAIOR!")