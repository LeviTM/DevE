#Algoritmo de busqueda
la=[1,2,3,4,5,6]
ab=4
if ab in la:
	print(f"El numero {ab} esta en la lista")
else:
	print(f"El numero {ab} no esta en la lista")

#Algortimo de Odenacion
#range = genera una secuencia de numeros
#len = establece un rango segun la cantidad de datos en este caso de 0 a 6
li=[8,35,90,1,6,4,120]
b=False
for i in range(len(li)):
	for j in range(0 ,len(li)-i-1):
		if li[j] > li[j+1]:
			li[j] , li[j+1] = li[j+1], li[j]
			b=True
	if not b:
		break
print("Lista ordenada", li)

#Estructuras de Control
#Ejercicios de Practica (if, elif, else, for, and while)
x= 6
if x > 6:
	print("Mayor que 6")
elif x == 6 :
	print("Igual que 6")
else:
	print("Menor que 6")

for i in range(1,10):
	print(i)

c=0
while c < 5:
    print("Cuenta:", c)
    c += 1
#Ejercicio Ramdom
import random
p=1
key= random.randint(1,10)
for i in  range(10):
	p = int(input("Adivina el numero esta entre 1 y 10: "))
	if p == key:
		print("exacto el numero es ",p," Logrado en el intento ",p)
		break
	else:
		print("No es el numero sigue intentando")
		p +=1
else:
	print("Se te terminaron los intentos el numero era: ",key)
	
#Tabla de multiplicar
n = int(input("Ingresa un numero amiguit@: "))
for i in range(1,10):
	print(f"{n} x {i} = {n*i}")
# contador
i = 0
while i <= 10:
    print(i)
    i += 2
#Desafio dice xd 
while True:
	try:
		edad= int(input("Ingresa Tu edad wawita: "))
		if 1 <= edad <= 100 :
			edad=int(edad)
			if edad <= 17:
				print("Aun no cuentas ve a tu casa ratatui")
			else:
				print("Usted puede votar para acuña ❤")
				break
		else:
			print("Ingresa una edad valida oe especial")
	except ValueError:
		print("Ingresa solo numeros oe especial")
