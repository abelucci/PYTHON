import random

numero_secreto = random.randint(1, 10)

intento = int(input("Adiviná el número (1-10): "))

if intento == numero_secreto:
    print("¡Adivinaste!")
else:
    print(f"No era {intento}, era {numero_secreto}.")
