import re

def Ej6(secuencias):
	print("Secuencias formidables: ")
	formidables = []
	l = 0
	index = -1
	for i in secuencias:
		val = re.findall("[0,1]+", i)
		if len(val)==1:
			if es_formidable(i):
				l += 1
				print(str(l) + ". " + i)
				formidables.append(i)
#			else:
#				print(i + " no es formidable")
#		else:
#			print("La secuencia " + i + " no es valida")
	if l>0:
		index = int(input("Cual secuencia desea enviar: "))
		while index<1 or l<index:
			index = int(input("Ingrese un numero valido: "))
		return (formidables[index-1],l)
	else:
		return ('',0)
		
def es_formidable(string):
	zero = string.split("1")[::-1]
	len_zero = []
	temp_zero = 0
	flag_zero = True
	
	one = string.split("0")
	len_one = []
	temp_one = 0
	flag_one = True
	
	for i in zero:
		if len(i)>0:
			if len(i)>temp_zero:
				temp_zero = len(i)
			else:
				flag_zero = False
	
	for i in one:
		if len(i)>0:
			if len(i)>temp_one:
				temp_one = len(i)
			else:
				flag_one = False
	
	return flag_zero and flag_one

print("Ejercicio 6:\nTest case:\nInput 1: 000100110 00 10 5 6\nInput 2: 2\nReturn: ('00',3)\n")
string = str(input("Ingrese las secuencias separadas por un espacio : ")).split(" ")
print(Ej6(string))

