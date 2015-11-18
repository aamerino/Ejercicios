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
    if comprobarPositivo(primerNumero) and comprobarPositivo(segundoNumero):
	    suma = primerNumero + segundoNumero
	    print ("La suma de los dos números es:", suma)
    else:
    	print ("No se calcula la suma porque alguno de los números o los dos no son positivos")

else:
	print ("No se calcula la suma porque alguno de los números o los dos no son positivos")
