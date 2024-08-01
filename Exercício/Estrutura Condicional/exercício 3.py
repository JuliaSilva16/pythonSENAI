# Solicite o ano de nascimento de uma pessoa, calcule a idade e verifica se a pessoa é maior ou menor de idade.
# Exiba uma mensagem correspondente.

print("Você irá digitar o seu ano de nascimento e o sisema irá falar se você é meior ou menor de idade!")
print("")

while True:
    try:
        ano_nascimento = int(input("Digite o seu ano de nascimento: "))
        if ano_nascimento >= 1804 and ano_nascimento <= 2023:
            break
        else:
            print("ano invalido")

    except ValueError:
        print("Informação inválida")

while True:
    try:
        ano_presente = int(input("Digite o ano presente.Ex:2020: "))
        if ano_presente >= 1804 and ano_presente <= 2024:
            break
        else:
            print("idade inválida")

    except ValueError:
        print("Informação inválida")

idade = ano_presente - ano_nascimento

if idade >= 1 and idade <= 17 :
    print(f"Você tem {idade} anos de idade, então você é menor de idade!")
elif idade >= 18 and  idade <= 220:
    print(f"Você tem {idade} ano de idade, entâo você é maior de idade!")
