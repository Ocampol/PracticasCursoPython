#Ejercicio 1
"""numero = int(input("Ingresa un numero: "))
nuevoNumero = int(input("Ingresa un numeros, que sean mayor al anterior: "))
while numero<nuevoNumero:
	numero = nuevoNumero
	nuevoNumero = int(input("Ingresa un numeros, que sean mayor al anterior. Para dejar de hacerlo ingresa un numero menor: "))

print("El programa ha finalizado")
"""

#Ejercicio 2
numero = int(input("Ingresa un numero positivo: "))
acum = 0
while numero >= 0:
	acum = acum + numero
	numero = int(input("Ingresa un numero positivo: "))
print("La suma de los numeros ingresados es: " + str(acum))
print("El programa ha finalizado")


