def comprobarInteger(numero):
	try: 
		int(numero)
		return True
	except ValueError:
		return False
def comprobarPositivo(numero):
	if numero > 0 :
		return True
	else:
		return False

print("Introducir numero A")
primerNumero = int(input())
print("Introducir numero B")
segundoNumero = int(input())


if comprobarInteger(primerNumero) and comprobarInteger(segundoNumero):
	if comprobarPositivo(primerNumero):
		if comprobarPositivo(segundoNumero):
			suma = primerNumero + segundoNumero
			print ("La suma de los dos números es:", suma)
		else:
		    print ("No se calcula la suma porque el segundo número es negativo.")
	else:
		if comprobarPositivo(segundoNumero):
			print ("No se calcula la suma porque el primer número es negativo.")
		else:
		    print ("No se calcula la suma porque los dos números son negativos.")
else:
	print ("No se calcula la suma porque alguno de los números o los dos no son positivos")
