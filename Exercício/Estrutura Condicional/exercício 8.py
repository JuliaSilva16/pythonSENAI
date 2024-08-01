#Solicite ao usuário o valor de sua renda anual bruta e, em seguida, calcule.
#Exiba o desconto do Imposto de Renda de acordo com a tabela progressiva de 2024.
#Tebela:
# Faixa de Renda Anual Bruta           Alíquota
#Até R$ 56.072,00                         0%
#De R$ 56.072,01 a R$ 238.532,00         7,50%
#De R$ 238.532,01 a R$ 522.400,00         15%
#De R$ 522.400,01 a R$ 987.600,00        22,50%
#Acima de R$ 987.600,00                  27,50%

print("")
print("Você irá inserir valor da renda anual bruta para calcular e te informará quanto de desconto do imposto de renda!")
print("")

while True:
    try:
        valor_renda_anual = float(input("Digite o valor da renda anual bruta: R$ "))
        break
    except ValueError:
        print("Informação inválida")

if valor_renda_anual <= 56072.00:
    print("Você tem 0% de desconto do imposto de renda!")

elif valor_renda_anual >= 56072.01 and valor_renda_anual <= 238532.00:
    desconto = (7.50/ 100) * valor_renda_anual
    print(f"Você tem 7,50%  de desconto.Então o desconto sai de R$ {desconto} do imposto de renda!")

elif valor_renda_anual >= 238532.01 and valor_renda_anual <= 522400.00:
    desconto = (15 / 100) * valor_renda_anual
    print(f"Você tem 15 % de desconto. Então o desconto sai de R$ {desconto} do imposto de renda!")

elif valor_renda_anual >= 522400.01 and valor_renda_anual <= 987600.00:
    desconto = (22.50 / 100) * valor_renda_anual
    print(f"Você tem 22,50% de desconto.Então o desconto sai de R$ {desconto} do imposto de renda!")

elif valor_renda_anual > 987600.00:
    desconto = (27.50 / 100) * valor_renda_anual
    print(f"Você tem 27,50% de desconto. Então o desconto sai de R$ {desconto} do imposto de renda!")