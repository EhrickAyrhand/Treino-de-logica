texto = str(input("Digite a palavra para ser verificada: "))
texto_invertido = texto[::-1]
def palindromo (texto_invertido, texto):
    if texto_invertido == texto:
        print(f"A palavra {texto} é um Palindromo!")
    else:
        print(f"A palavra {texto} não é um Palindromo!")

palindromo(texto_invertido, texto)