print("Introducir valor bruto")
valorBruto = int(input())
if valorBruto < 20:
	valorNeto = valorBruto
	print ("Importe final:" , valorNeto)
elif valorBruto > 20 and valorBruto <= 100:
	valorNeto = valorBruto * 0.95
	print ("Importe final:" , valorNeto)
else:
	valorNeto = valorBruto * 0.90
	print ("Importe final:" , valorNeto)