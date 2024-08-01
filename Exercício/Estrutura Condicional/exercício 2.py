#2 - Solicite duas notas de um aluno e calcule a média.
# Se a média for maior ou igual a 70, o aluno está aprovado.Caso  contrário, está reprovado.
print("Insira sua nota para saber se você foi aprovado ou reprovado:")
print("")
while True:
    try:
        nota1 = float(input("Digite a primeira nota: "))
        if nota1 >= 0 and nota1 <= 100:
            break
        else:
            print("Nota invalida")

    except ValueError:
        print("Informação inválida")

while True:
    try:
        nota2 = float(input("Digite a segunda nota: "))
        if 0 <= nota2 <= 100:
            break
        else:
            print("Nota inválida")

    except ValueError:
        print("Informação inválida")

media_de_nota = (nota1 + nota2) / 2

if 70 <= media_de_nota <= 100:
    print(f"Você foi aprovado com sua nota de {media_de_nota}")
elif 0 <= media_de_nota <= 70:
    print(f"Você foi reprovado com sua nota de {media_de_nota}")