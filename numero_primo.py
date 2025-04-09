numero = int(input("Digite o número para ser verificado: "))

if numero <= 1:
    print("Números menores ou iguais a 1 não são primos.")
else:
    eh_primo = True

    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            eh_primo = False
            break

    if eh_primo:
        print("O número é primo.")
    else:
        print("O número não é primo.")
