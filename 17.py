"""Escribe 	un programa que calcule y escriba la suma de los números pares por un lado, y de los impares por otro, de los números comprendidos entre dos número introducidos por teclado."""

print("Introducir primer numero")
primerNumero = int(input())
print("Introducir segundo numero")
segundoNumero = int(input())

sumaPares= 0
sumaImpares= 0

while primerNumero <= segundoNumero:
	if primerNumero %2 == 0:
		sumaPares = primerNumero + sumaPares
	else:
		sumaImpares = primerNumero + sumaImpares
	primerNumero += 1

print ("Suma Pares:" , sumaPares)

print ("Suma Impares:" , sumaImpares) 

