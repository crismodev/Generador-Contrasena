import secrets
cuantos_caracteres = input("¿Cuantos caracteres quieres en tu contraseña?: ")
try:    
    caracteres_int = (int(cuantos_caracteres))
    caracteres = "ABCDabcd0123456789*$%&"
    caja_caracteres = ""
    if caracteres_int < 1:
        print ("La contraseña debe tener por lo menos 1 caracter")
    elif caracteres_int > 100:
        print ("La contraseña no puede tener mas de 100 caracteres")
    else:
        print("----GENERANDO CONTRASEÑA----")
        for car in range (caracteres_int):
            numeros = secrets.randbelow(len(caracteres))
            caja_caracteres = caja_caracteres + (caracteres[numeros])
        print(caja_caracteres)
except:
    print(f"{cuantos_caracteres} No es un caracter valido")
    exit()
