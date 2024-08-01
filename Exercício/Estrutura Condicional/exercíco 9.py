#Utiliza a biblioteca datetime para mostrar o ano, mes e dia da semana
#pegar o horário atual e dar uma saudação para o usuário.
# Use o exemplo da imagem anexada.

import datetime
while True:
    try:
        tempo_agora = datetime.datetime.now()
        semana = tempo_agora.hour.strftime("%A")
        mes = tempo_agora.strftime("%B")
        print("")
        print("Bem vinda(o) a bibblioteca datetime!")
        escolha = int(input("Digite 1,2 e 3 para exibir as seguintes informações: (1) para dia,mês e ano , (2) para horas, (3) para dia da semana: "))

        if escolha == 1:
            if "Januery" == mes:
                traducao_mes ="Janeiro"

            elif "February" == mes:
                traducao_mes ="Fevereiro"

            elif "March" == mes:
                traducao_mes ="Março"

            elif "April" == mes:
                traducao_mes ="Abril"

            elif "May" == mes:
                traducao_mes ="Maio"

            elif "June" == mes:
                traducao_mes ="Junho"

            elif "July" == mes:
                traducao_mes ="Julho"

            elif "August" == mes:
                traducao_mes ="Agosto"

            elif "September" == mes:
                traducao_mes ="Setembro"

            elif "October" == mes:
                traducao_mes ="Outubro"

            elif "November" == mes:
                traducao_mes ="Novembro"

            elif "December" == mes:
                traducao_mes ="Dezembro"
            print(f"O dia é {tempo_agora.day} do mês de {traducao_mes} de {tempo_agora.year} ")
            break

        elif escolha == 2:
            if tempo_agora.hour >= 5 and tempo_agora.hour <= 12:
                print("Bom dia!")

            elif tempo_agora.hour >= 12 and tempo_agora.hour <= 18:
                print("Boa tarde!")

            elif tempo_agora.hour >= 18 and tempo_agora.hour <= 24:
                print("Boa noite!")

            elif tempo_agora.hour >=24 and tempo_agora.hour <= 5:
                print("Boa madrugada")

            print(f"A hora agora é {tempo_agora.hour}:{tempo_agora.minute} e {tempo_agora.second} segundos")
            break

        elif escolha == 3:
            if "Monday" == semana:
                traducao_semana = "Segunda"

            elif "Tuesday" == semana:
                traducao_semana = "Teça-feira"

            elif "Wednesday" == semana:
                traducao_semana = "Quarta-feira"

            elif "Thursday" == semana:
                traducao_semana = "Quinta-feira"

            elif "Friday" == semana:
                traducao_semana = "Sexta-feira"

            elif "Saturday" == semana:
                traducao_semana = "Sábado"

            elif "Sunday" == semana:
                traducao_semana = "Domingo"

            print(f"O dia da semana hoje é {traducao_semana} . ")
            break
        else:
            print("Informação inválido")
    except ValueError:
        print("Informação inválida")