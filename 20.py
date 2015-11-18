"""Repite el programa anterior, pero chequeando que el usuario no introduzca números negativos. Si se da esta circunstancia hay que visualizar un mensaje de error, forzando al usuario a que introduzca números positivos."""

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
	while numeroOk == False:
		if listNum[num] >= 0:
			numeroOk == True:
		print("Introduce un numero positvo.")


print("El mayor numero es:" , comprobarNumeros(listNum))

#########CASOS TEST##############
listNum=[1,2,3,4,5]

if comprobarNumeros(listNum) == 5:
	print("Caso normal OK")
else:
	print("Caso normal Fail")

