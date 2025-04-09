numero = int(input("Digite o numero para descobrir o fatorial: "))

def fatorial(numero):
    resultado = 1
    for n in range(1, numero + 1):
        resultado *= n  # Multiplica o número atual ao resultado acumulado
        print(resultado)
    return resultado
print(f"O fatorial de {numero} é: {fatorial(numero)}")


