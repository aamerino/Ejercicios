print("Introducir numero A")
primerNumero = int(input())
print("Introducir numero B")
segundoNumero = int(input())

if (primerNumero > segundoNumero):
	print("el primer número ", primerNumero ," es mayor que el segundo " , segundoNumero)
elif segundoNumero > primerNumero:
	print("el primer número ", primerNumero ," es menor que el segundo ", segundoNumero)
else:
	print("los dos números son iguales" ,primerNumero)
