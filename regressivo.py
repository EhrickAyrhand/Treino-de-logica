numero = int(input("Digite o numero para a contagem regressiva: "))

def contagem (numero):
    for n in range(0, numero):
        print (f"{n + 1}")

contagem(numero)