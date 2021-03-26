def Ej2(k,l,r):
  rta = None
  counter = 0
  for i in range(int(l),int(r)+1):
    for j in range(len(str(i))-1):
      if len(set(str(i)[j:j+2])) == 1:
        #print(set(str(i)[j:j+2]), " -> ", i)
        counter += 1
        if int(k) == counter:
          rta = i
  if rta != None:
    print("El k-esimo numero es {0}".format(rta))
  else:
    print("El k-esimo numero esta fuera del rango")

print("\n//-//-//-//-//-//-//-//-//-//-//\nEjercicio 2: \nTest case: 9 0 100\nReturn: 9\n")
var = tuple(input("Ingrese k,l,r separados por espacios: ").split())
Ej2(*var)