numero = int(input("Insira o número para descobrir a tabuada dele: "))

def multiplicacao(numero):
    for n in range(0, 11):  # Vai de 0 até 10
        print(f"{numero} x {n} = {numero * n}")  # Exibe a multiplicação

multiplicacao(numero)  # Chama a função para exibir a tabuada
