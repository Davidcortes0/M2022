def Ej1(cadena):
  tamaño = len(cadena)
  counter = 0
  for i in range(tamaño-3):
    if set(cadena[i:i+4]) == {"a","c","b","d"}:
      #print(cadena[i:i+4])
      counter += 1
  print(counter)

print("Ejercicio 1: \nTest case: abcd\nReturn: 1\n")
cadena = input("Ingrese la cadena: ")
Ej1(cadena)

'''
En una cadena de caracteres, una substring de longitud 4 es un conjunto de 4 caracteres
consecutivos de la string. Una substring de longitud 4 es buena si y sólo si todos sus
caracteres son distintos. Dada una string s que tiene solo las letras minúsculas a, b, c, d,
contad cuantas substrings de longitud 4 buenas tiene.
'''
