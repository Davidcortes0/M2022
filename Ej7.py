def validate(lista):
    for i in lista:
        try:
            valor = int(i)
        except ValueError:
            lista.remove(i)

def mazmorra(monster_force):
	player_force = 0
	for i in monster_force:
		if player_force >= int(i):
			player_force += 1
	return player_force
	
def bubbleSort(lista):
	n = len(lista)
	for i in range(n):
		for j in range(0, n-i-1):
			if int(lista[j]) > int(lista[j+1]):
				lista[j], lista[j+1] = lista[j+1], lista[j]
				
def Ej7(force_list):
	validate(force_list)
	bubbleSort(force_list)
	print("La fuerza maxima del personaje es: " + str(mazmorra(force_list)))

print("Ejercicio 7: \nTest case: 0 2 0 5\nReturn: 3\n")
monster_force = input("Ingrese la fuerza de cada mounstros separadas por un espacio: ").split()
Ej7(monster_force)

