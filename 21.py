# Escribe un programa que solicite por teclado 5 números positivos,
# forzando al usuario a que únicamente introduzca valores positivos.
# A continuación el programa tiene que escribe cuál es el valor más
# pequeño y cuál es el mayor valor de los introducidos por el usuario.


def numMayorMenor(listNum):
    for i in listNum:
        if i < 0:
            return None
    numeroMayor = listNum[0]
    numeroMenor = listNum[0]
    for i in listNum:
        if i > numeroMayor:
            numeroMayor = i
        if i < numeroMenor:
            numeroMenor = i
    return (numeroMayor, numeroMenor)

# ------------------RECOGIDA DATOS----------------------------
listNum = []
for num in range(1, 6):
    print("Introducir numero ", num)
    listNum.insert(num, int(input()))

# -------------------SALIDA DATOS-------------------------
if numMayorMenor(listNum) == None:
    print("Intrdoduce Solo Numeros Positivos.")
else:
    (numeroMayor, numeroMenor) = numMayorMenor(listNum)
    print("El Mayor es ", numeroMayor, ". El Menor es ", numeroMenor, ".")


# --------------------CASOS TEST-------------------------

print("···············CASOS TEST··························")

# Caso Normal

listNum = [1, 2, 3, 4, 5]

(numeroMayor, numeroMenor) = numMayorMenor(listNum)
if numeroMayor == 5 and numeroMenor == 1:
    print("Caso general Ok")
else:
    print("Caso general Fail")

# Caso Negativo
listNum = [1, -2, 3, -4, 5]
if numMayorMenor(listNum) == None:
    print("Caso Negativo OK")
else:
    print("Caso Negativo Fail")

# Caso numeros iguales

listNum = [5, 5, 5, 5, 5]
(numeroMayor, numeroMenor) = numMayorMenor(listNum)
if numeroMayor == 5 and numeroMenor == 5:
    print("Caso igual Ok")
else:
    print("Caso igual Fail")
