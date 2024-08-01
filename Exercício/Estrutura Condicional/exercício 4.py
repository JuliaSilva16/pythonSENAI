#Solicite dois números e verifica qual deles é o maior e exiba uma mensagem correspondente.
print("")
print("Digite dois números para saber qual deles é o maior!")
print("")

while True:
    try:
        numero1 = float(input("Digitre o primeiro número: "))
        break
    except ValueError:
        print("Informação inválida")

while True:
    try:
        numero2 = float(input("Digite o segundo número: "))
        break

    except ValueError:
        print("Informação inválida")

if numero1 > numero2:
    print(f"Primeiro número {numero1} é MAIOR que o segundo número {numero2}. ")
else:
    print(f"O Pimeiro número {numero1} é MENOR que o segundo número {numero2}. ")