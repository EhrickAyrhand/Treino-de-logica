# 1. Recebe uma lista de números do usuário (separados por vírgula)
entrada = input("Digite uma lista de números separados por vírgula: ")

# 2. Converte os valores para inteiros e guarda na lista
numeros = [int(x.strip()) for x in entrada.split(",")]

# 3. Ordena a lista usando Bubble Sort
n = len(numeros)

for i in range(n):
    for j in range(0, n - i - 1):
        if numeros[j] > numeros[j + 1]:
            # Troca os elementos
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

# 4. Mostra a lista ordenada
print("Lista ordenada:", numeros)
