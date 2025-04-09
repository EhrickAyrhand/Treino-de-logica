import random

numero = int(input("Tente adivinha o numero que eu estou pensando: "))
numero2 = random.randrange(0, 10)

if numero == numero2:
    print (f"{numero2}")
    print("parabens")
else:
    print (f"{numero2}")
    print("errou")