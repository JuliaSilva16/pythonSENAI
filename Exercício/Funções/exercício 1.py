#Mensagem automática: Crie uma função que receba um nome como parâmetro
# escreva uma saudação baseada na hora atual.

print("Você irá digitar seu nome e recebera uma saudação de acordo com o horário!")
print("")


from datetime import datetime


def solicita_nome(nome):
    while True:
        try:
            nome = input("Qual o seu nome: ")
            if nome.isnumeric():
                print("Digite apenas letras")
            else:
                return nome
        except ValueError:
            print("Digite apenas letras.Ex: Júlia.")

#hora atual/saudação
def definir_saudacao(hora_atual):
    hora_atual == datetime.now().hour

    if hora_atual >= 0 and hora_atual <= 5:
        saudacao ="Boa madrugada"

    elif hora_atual < 12:
        saudacao ="Bom dia"

    elif hora_atual < 19:
        saudacao ="Boa tarde"

    else:
        saudacao ="Boa noite"

    return saudacao

#exibir o "resultado"

print(definir_saudacao(datetime.now().hour),solicita_nome (""), "!!")

