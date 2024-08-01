#Solicite ao usuário um número de 1 a 12(representando um mês do ano)
#Exiba o nome correspondente ao mês (por exemplo, 1 para "Janeiro", 2 para "Fevereiro", etc.).
print("")
print("Digite um número de 1 a 12 para saber o mês do ano equivalente !")
print("")

while True:
    try:
        solicitacao_mes = int(input("Digite o número de 1 a 12: "))
        if solicitacao_mes >= 1 and solicitacao_mes <= 12:
            break
        else:
            print("mês inválido")
    except ValueError:
        print("informação inálida")

if solicitacao_mes == 1:
    print("O número 1 é equivalente á JANEIRO!")
elif solicitacao_mes == 2:
    print("O número 2 é equivalente á FEVEREIRO!")
elif solicitacao_mes == 3:
    print("O número 3 é equivalente á MARÇO!")
elif solicitacao_mes == 4:
    print("O número 4 é equivalente á ABRIL!")
elif solicitacao_mes == 5:
    print("O número 5 é equivalente á MAIO!")
elif solicitacao_mes == 6:
    print("O número 6 é equivalente á JUNHO!")
elif (solicitacao_mes== 7):
    print("O  número 7 é equivalente á JULHO!")
elif solicitacao_mes == 8:
    print("O número 8 é equivalente á AGOSTO!")
elif solicitacao_mes == 9:
    print("O número 9 é equivalente á SETEMBRO!")
elif solicitacao_mes == 10:
    print("O número 10 é equivalente á OUTUBRO!")
elif solicitacao_mes == 11:
    print("O número 11 é equivalente á NOVEMBRO!")
elif solicitacao_mes == 12:
    print("O número 12 é equivalente á DEZEMBRO!")