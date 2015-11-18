#Escribe un programa que pida por teclado una cantidad de dinero y que a 
#continuación muestre la descomposición de dicho importe en el menor número de 
#billetes y monedas de 100, 50, 20, 10, 5, 2 y 1 	euro. En el caso de que alguna 
#moneda no intervenga en la descomposición no se tiene que visualizar nada en la 
#pantalla. Para una cantidad de 2236 euros la salida que generaría el 
#programa sería:

def calcularBilletes (cantidadDinero , billete):
	#calcula el numero de billetes.
	numBilletes = cantidadDinero//billete
	#devuelve la cantidad restante despues de calcular la cantidad billetes. 
	return numBilletes , (cantidadDinero - (numBilletes * billete))

#
cantidadDinero = int(input())

billetes100 , cantidadDinero = calcularBilletes(cantidadDinero , 100)
billetes20 , cantidadDinero = calcularBilletes(cantidadDinero , 20)
billetes10 , cantidadDinero = calcularBilletes(cantidadDinero , 10)
billetes5 , cantidadDinero = calcularBilletes(cantidadDinero , 5)
billetes1 , cantidadDinero = calcularBilletes(cantidadDinero , 1)

print (billetes100 ,"billetes de 100 euros\n" , billetes20 , 
	"billete de 20 euros\n" ,  billetes10 , "billete de 10 euros\n" , 
	billetes5 , "billete de 5 euros\n" , billetes1 , "moneda de 1 euro"  )