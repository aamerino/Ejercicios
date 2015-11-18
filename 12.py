print("Introducir numero A")
primerNumero = int(input())
print("Introducir numero B")
segundoNumero = int(input())

if primerNumero%2 == 0 and segundoNumero%2 == 0 and primerNumero < 50 and segundoNumero > 100 and segundoNumero < 500:
	suma = primerNumero + segundoNumero
	print("La suma es" , suma)
else:
	print("Error")
