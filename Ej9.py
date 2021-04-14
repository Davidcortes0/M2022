def crear_desierto(n : int, dunas : list, oasis : list, inicio, final):
	desierto = []
	c_dunas = dunas
	c_oasis = oasis
	for i in range(n-1):
		desierto.append([])
		for j in range(n-1):
			if i == 0:
				if inicio == j:
					desierto[i].append("0")
				else:
					desierto[i].append("x")
			elif i == n-2:
				if final == j:
					desierto[i].append("1")
				else:
					desierto[i].append("x")
			elif [i,j] in c_dunas:
				indice = c_dunas.index([i,j])
				desierto[i].append("#")
				c_dunas.pop(indice)
			elif [i,j] in c_oasis:
				indice = c_oasis.index([i,j])
				desierto[i].append("o")
				c_oasis.pop(indice)
			else:
				desierto[i].append(".")
	
	for i in range(1,n-2):
		for j in range(n-1):
			if j < inicio:
				if desierto[i-1][j] == "x" and desierto[i-1][j+1] == "x":
					desierto[i][j] = "x"
			elif j > inicio:
				if desierto[i-1][j] == "x" and desierto[i-1][j-1] == "x":
					desierto[i][j] = "x"
	
	desierto = desierto[::-1]
	
	for i in range(1,n-2):
		for j in range(n-1):
			if j < final:
				if desierto[i-1][j] == "x" and desierto[i-1][j+1] == "x":
					desierto[i][j] = "x"
			elif j > final:
				if desierto[i-1][j] == "x" and desierto[i-1][j-1] == "x":
					desierto[i][j] = "x"
	
	return desierto

def imprimir(desierto : list):
	print()
	for i in desierto:
		char = ""
		for j in i:
			char += j + " "
		print(char)
	print()

def es_entero(x):
	try:
		x = int(x)
	except ValueError:
		x = -1
	if x != -1:
		return True
	else:
		return False

def caminos(n : int, u : int, inicio: int, final : int, dunas : list, oasis : list):
	if u < n-3:
		if oasis == []:
			return 0
	
	#Caso favorable
	
	desierto = crear_desierto(n, dunas, oasis, inicio, final)
	c_u = u
	
	for i in range(n-1):
		for j in range(n-1):
			casilla = 0
			if desierto[i][j] == "." or desierto[i][j] == "0" or desierto[i][j] == "o":
				if desierto[i][j] == "o":
					c_u = u
				if j == 0:
					if es_entero(desierto[i-1][j]):
						casilla += int(desierto[i-1][j])
					if es_entero(desierto[i-1][j+1]):
						casilla += int(desierto[i-1][j+1])
				elif j == n-2:
					if es_entero(desierto[i-1][j]):
						casilla += int(desierto[i-1][j])
					if es_entero(desierto[i-1][j-1]):
						casilla += int(desierto[i-1][j-1])
				else:
					if es_entero(desierto[i-1][j]):
						casilla += int(desierto[i-1][j])
					if es_entero(desierto[i-1][j+1]):
						casilla += int(desierto[i-1][j+1])
					if es_entero(desierto[i-1][j-1]):
						casilla += int(desierto[i-1][j-1])
				desierto[i][j] = str(casilla)
				c_u -= 1
			if u == 0:
				desierto[i][j] = 0
				
	
	#imprimir(desierto[::-1])
	return int(desierto[n-2][inicio])

def Ej9():
	#tamaño tablero y unidades de agua
	n = int(input("Ingrese n: "))
	u = int(input("Ingrese u: "))
	
	#columna de inicio
	inicio = -1
	inicio = int(input("Ingrese la columna de la casilla de inicio: "))-1
	if not (0 <= inicio < n-1):
		inicio = int(input("Ingrese una columna valida: "))-1
	
	#columna final
	final = -1
	final = int(input("Ingrese la columna de la casilla final: "))-1
	if not (0 <= final < n-1):
		final = int(input("Ingrese una columna valida: "))-1
	
	#dunas
	num_dunas = int(input("ingrese el numero de dunas: "))
	dunas = []
	for i in range(num_dunas):
		d = (-1,-1)
		d = input("Ingrese la fila y columna de la duna {0} separadas por un espacio: ".format(i+1)).split()
		d[0], d[1] = int(d[0])-1, int(d[1])-1
		while not (0 <= d[0] < n-1) or not (0 <= d[1] < n-1) or d in dunas or d == [0,inicio] or d == [n-2,final]:
			d = input("Ingrese una fila y columna valida: ").split()
			d[0], d[1] = int(d[0])-1, int(d[1])-1
		dunas.append(d)
	
	#oasis
	num_oasis = int(input("ingrese el numero de oasis: "))
	oasis = []
	for i in range(num_oasis):
		o = (-1, -1)
		o = input("Ingrese la fila y columna del oasis {0} separadas por un espacio: ".format(i+1)).split()
		o[0], o[1] = int(o[0])-1, int(o[1])-1
		while not (0 <= o[0] < n-1) or not (0 <= o[1] < n-1) or o in dunas or o in oasis or o == [0,inicio] or o == [n-2,final]:
			o = input("Ingrese una fila y columna valida: ").split()
			o[0], o[1] = int(o[0])-1, int(o[1])-1
		oasis.append(o)
	
	num_caminos = caminos(n, u, inicio, final, dunas, oasis)
	
	mod = (10**9) + 7
	print("El numero de caminos es {0} y mod {1} es {2}".format(num_caminos, mod, num_caminos%mod))
	
Ej9()
