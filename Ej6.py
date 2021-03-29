def Ej6(string):
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

print("//-//-//-//-//-//-//-//-//-//-//\nEjercicio 1: \nTest case: 000100110\nReturn: Es formidable\n")
string = str(input("Ingrese la secuencia: "))

if Ej6(string):
	print("Es formidable")
else:
	print("No es formidable")
