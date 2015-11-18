print("Introducir numero A")
primerNumero = int(input())
print("Introducir numero B")
segundoNumero = int(input())
print("Introducir numero C")
tercerNumero = int(input())

print ("Números introducidos: " , primerNumero , "\t" , segundoNumero , "\t" , tercerNumero)
if primerNumero + segundoNumero == tercerNumero:
    print("Se cumple que N3 = N1 + N2")
elif segundoNumero + tercerNumero == primerNumero:
	print("Se cumple que N1 = N2 + N3")
elif primerNumero + tercerNumero == segundoNumero:
	print("Se cumple que N2 = N1 + N3")
else:
	print("Los números no cumplen la condición")