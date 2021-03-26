def base_change(num, base, rest):
	next_num = int(num/base)
	mod_num = num%base
	rest += str(mod_num)
	if next_num >= base:
		rest = base_change(next_num, base, rest)
	if next_num < base:
		rest += str(next_num)
	#print(str(num) + "/" + str(base) + "=" + str(next_num) + "." + str(mod_num))
	return rest

def list_to_base(n):
	lista = []
	for i in range((3**n)):
		lista.append(str(base_change(i,3,"")))
	return lista

def stack_sep(lista):
	bloques = []
	subbloque = []
	for i in lista:
		if str(1) in str(i):
			subbloque.append(i)
		else:
			if subbloque != []:
				bloques.append(subbloque)
			bloques.append([i])
			subbloque = []
	return bloques


def long(bloques):
	length = ""
	for i in bloques:
		length += str(len(i)) + " "
	return length
	
def Ej4(n):
  base_tres = list_to_base(n)
  bloques = stack_sep(base_tres)
  #print(bloques)
  print(long(bloques))

print("\n//-//-//-//-//-//-//-//-//-//-//\nEjercicio 4: \nTest case: 2\nReturn: 1 1 1 3 1 1 1\n")
n = int(input("Ingrese el exponente: "))
Ej4(n)