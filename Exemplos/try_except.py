#O while repete tudo que está dentro dele
while True:
    #O try vai tenat executar esse bloco de código
    try:
        idade = int(input("Digite sua idade: "))
        if idade > 0 and idade < 100:
            print("Idade:",idade)
            #O breack sai do while
            break
        else:
            print("idade invalida")
    except ValueError:
        #Caso der erro executa aqui
        print("Digite sua idade em número. Exemplo: 26")