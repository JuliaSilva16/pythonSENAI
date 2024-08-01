#solicite um número ao usuário e verifica se o número é positivo ou negativo e exiba uma mensagem positivo ou negativo.
print("Digite um número para saber se ele é positivo ou negativo!")
print("")
while True:
    try:
        solicitacao_numero = float(input("Digite o número: "))
        if solicitacao_numero >= 0:
            print(f"O número {solicitacao_numero} é positivo")

        elif solicitacao_numero < 0:
            print(f"O número {solicitacao_numero} é negativo")
        break
    except ValueError:
        print("Digite apenas números ou digite sem a virgula. Exemplo: 16.17")

