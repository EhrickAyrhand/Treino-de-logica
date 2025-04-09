sequencia = int(input("Diga quantas sequências de Fibonacci você quer: "))

def fibonacci(sequencia):
    a, b = 0, 1  # Começo da sequência de Fibonacci
    for n in range(sequencia):
        print(a, end=" ")
        a, b = b, a + b  # Atualiza os valores de a e b para o próximo número na sequência

fibonacci(sequencia)
