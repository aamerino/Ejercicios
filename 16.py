"""Escribe	un programa que escriba en pantalla los 30 primeros números naturales (del 1 al 30), así como su media aritmética."""

i = 0
suma = 0 

while i < 31:
	print (i)
	suma = suma + i
	i += 1
	
media = suma/i
print ("Media arimetica" , media)