"""Lee por teclado 5 números enteros positivos, y escribe cuál es el mayor de los números introducidos. """

def comprobarNumeros(listNum):
	numeroMayor = listNum[1]
	for num in listNum:
		if(num > numeroMayor):
			numeroMayor= num
	return (numeroMayor)

listNum=[]

for num in range (1 , 6):
	print("Introducir numero")
	listNum.insert(num , int(input()))

print("El mayor numero es:" , comprobarNumeros(listNum))

#########CASOS TEST##############
listNum=[1,2,3,4,5]

if comprobarNumeros(listNum) == 5:
	print("Caso normal OK")
else:
	print("Caso normal Fail")