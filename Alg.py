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
