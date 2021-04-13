class vertice:
	def __init__(self, n, inicio, final, pago):
		self.n = n
		self.vecinos = []
		self.inicio = inicio
		self.final = final
		self.pago = pago
		
	def agregar_vecino(self, vertice):
		if vertice not in self.vecinos:
			if self.final <= vertice.inicio:
				self.vecinos.append(vertice)
	
def grafo(vertex : vertice, pago : int, valores: list):
	#print(vertex.n, vertex.pago)
	pago += vertex.pago
	if vertex.vecinos == []:
		valores.append(pago)
		#print(pago)
		pago = 0
	for i in vertex.vecinos:
		pago, vallores = grafo(i, pago, valores)
	return pago, valores

def crear_grafo(lista : list):
	lista.sort(key=lambda x: x.inicio)

	copy = lista

	#enlazar nodos de forma individual
	for i in copy:
		for j in copy:
			if i != j and j not in i.vecinos:
				i.agregar_vecino(j)

	#reverse list
	copy = copy[::-1]

	#crear rutas entre nodos
	for i in lista:
		for j in copy:
			if i != j and j not in i.vecinos:
				i.agregar_vecino(j)
	
	return lista

def maximo(lista : list):
	maximos = []
	for i in lista:
		a, valores = grafo(i, 0, [])
		maximos.append(max(valores))
	return max(maximos)
		
def entero(x):
	try:
		if int(x) == float(x):
			x = int(x)
		else:
			x = -1
	except ValueError:
		x = -1
	return x

def Ej8(): 
	s = t = -1
	while s <= 0:
		s = input("Ingrese la cantidad de segundos del dia: ")
		s = entero(s)
		if s <= 0:
			print("Ingrese una cantidad valida")
	while t <= 0:
		t = input("Ingrese la cantidad de tareas del dia: ")
		t = entero(t)
		if t <= 0:
			print("Ingrese una cantidad valida")
	lista = []
	e = f = p = -1
	for i in range(t):
		e = f = p = -1
		while e < 0 or s <= e:
			e = input("Ingrese el segundo en el que inicia la tarea {0}: ".format(i+1))
			e = entero(e)
			if e < 0 or s <= e:
				print("Ingrese una cantidad valida")
		while f <= 0 or s < f:
			f = input("Ingrese el segundo en el que termina la tarea {0}: ".format(i+1))
			f = entero(f)
			if f <= 0 or s < e:
				print("Ingrese una cantidad valida")
		while p < 0:
			p = input("Ingrese el pago de la tarea {0}: ".format(i+1))
			p = entero(p)
			if p < 0:
				print("Ingrese una cantidad valida")
		lista.append(vertice(i+1, e, f, p))
	lista = crear_grafo(lista)
	m = maximo(lista)
	print("La cantidad maxima del dinero que se puede obtener es: {0}".format(m))

Ej8()

'''
En el año 2023, los empleos fijos son cosa del pasado y TuboFlex™ ha instalado tubos en
cada puesto de trabajo. Con ellos, puedes transportarte fácilmente de un puesto a otro para
completar tareas donde sea.
Tu día laborable consiste en s segundos, y hay n tareas a completar cada día.
La tarea i-ésima empieza en el segundo e_i, termina en el segundo f_i y te pagan p_i euros por 
completarla. 
Solo puedes completar una tarea a la vez y tienes que permanecer la duración
entera de esta para completarla, pero una vez terminada puedes inmediatamente empezar
otra tarea, ya que los tubos son un método de transporte muy rápido.
Quieres elegir las tareas de modo que maximices tus ganancias. ¿Cuál es la cantidad
máxima de dinero que puedes obtener?
'''

