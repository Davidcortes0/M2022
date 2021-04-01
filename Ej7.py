import re

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
	
monster_force = input("Ingrese la fuerza de los mounstros separados por un espacio: ").split()
validate(monster_force)
bubbleSort(monster_force)
print(mazmorra(monster_force))

