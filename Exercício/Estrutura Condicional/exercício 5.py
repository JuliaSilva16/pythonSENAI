#Solicite ao usuário um número de 1 a 7(representando um dia da semana).
#Exiba o nome correspondente ao dia (por exemplo, 1 para "Domingo", 2 para "Segunda-feira", etc.).
print("")
print("Digite um número de 1 a 7 para saber o dia da semana equivalente!")
print("")

while True:
    try:
        solicitacao_semana = int(input("Digite o número de 1 a 7: "))
        if solicitacao_semana >= 1 and solicitacao_semana <= 7:
            break
        else:
            print("Dia inválido")
    except ValueError:
        print("informação inálida")

if solicitacao_semana == 1:
    print("O número 1 é equivalente á DOMINGO!")
elif solicitacao_semana == 2:
    print("O número 2 é equivalente á SEGUNDA-FEIRA!")
elif solicitacao_semana == 3:
    print("O número 3 é equivalente á TERÇA-FEIRA!")
elif solicitacao_semana == 4:
    print("O número 4 é equivalente á QUARTA-FEIRA!")
elif solicitacao_semana == 5:
    print("O número 5 é equivalente á QUINTTA-FEIRA!")
elif solicitacao_semana == 6:
    print("O número 6 é equivalente á SEXTA-FEIRA!")
elif solicitacao_semana == 7:
    print("O  número 7 é equivalente á SÁBADO!")
