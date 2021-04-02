def Ej2(k,l,r):
  rta = None
  counter = 0
  for i in range(int(l),int(r)+1):
    for j in range(len(str(i))-1):
      if not len(set(str(i)[j:j+2])) == 1:
        counter += 1
        if int(k) == counter:
          rta = i
  if rta != None:
    print("El k-esimo numero es {0}".format(rta))
  else:
    print("El k-esimo numero esta fuera del rango")

print("Ejercicio 3: \nTest case: 2 10 20\nReturn: 12\n")
var = tuple(input("Ingrese k,l,r separados por espacios (respectivamente): ").split())
if var[1]<=var[2]:
	Ej2(*var)
else:
	print("Ingrese un intervalo valido")

'''
Un número es variado si no tiene dos dígitos iguales consecutivos en su representación en
base 10. Dados tres enteros k, l y r, encontrad el k-ésimo número variado en el intervalo [l, r]
o decid que no existe.
'''
