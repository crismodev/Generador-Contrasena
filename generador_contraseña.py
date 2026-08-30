import random
cuantos_caracteres = input("¿Cuantos caracteres quieres?")
cuantos_caracteres = int(cuantos_caracteres)
caracteres = "ABCDabcd0123456789*$%&"
contraseña_completa = ""

for car in range(cuantos_caracteres):
    random_caracteres = random.randint(0, len(caracteres) - 1)
    contraseña_completa = contraseña_completa + (caracteres[random_caracteres])
print(contraseña_completa)