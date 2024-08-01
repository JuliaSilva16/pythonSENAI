# Conversor de Temperatura: Crie uma função que receba um valor de temperatura em graus Celsius como parâmetro.
# retorne o valor convertido para Fahrenheit e Kelvin.

# "()"/parametro  solicita de fora-dentro fica o "apelido",simplificação

print("Você irá digitar a temperatura em graus celsius e será convertido para Fahrenheit e Kelvin!")
print("")
def receber_valor():
    while True:
        try:
            receber_temperatura= float(input("Digite o valor da tremperatura de graus Celsius (apenas o número): "))
            return receber_temperatura
        except ValueError:
            print("Digite apenas números.Ex: 70.")

def convertor_Fahrenheit(temperatura):
    Fahrenheit = temperatura * 1.8 + 32
    return Fahrenheit

def convertor_Kelvin(temperatura):
    Kelvin = temperatura + 273.15
    return Kelvin

def exibir(Kelvin,Fahrenheit):

    print("A temperatura em Fahrenheit fica a seguinte:", Fahrenheit)
    print("A temperatura em Kelvin fica a seguinte:", Kelvin)


grau_celsius = receber_valor()


exibir(convertor_Kelvin(grau_celsius),convertor_Fahrenheit(grau_celsius))

