def Ej1(cadena):
  tamaño = len(cadena)
  counter = 0
  for i in range(tamaño-3):
    if set(cadena[i:i+4]) == {"a","c","b","d"}:
      #print(cadena[i:i+4])
      counter += 1
  print(counter)

print("//-//-//-//-//-//-//-//-//-//-//\nEjercicio 1: \nTest case: abcd\nReturn: 1\n")
cadena = input("Ingrese la cadena: ")
Ej1(cadena)