
#Escribe un programa que calcule el área de una finca rectangular en metros cuadrados, así como su perímetro exterior, también en metros.

print("Introducir Base")
base = int(input())
print("Introducir Altura")
altura = int(input())
area = base * altura
perim = 2 * (base * altura)
print("Area " + str(area) + " m2")
print ("Perimetro " + str(perim) + " m")
