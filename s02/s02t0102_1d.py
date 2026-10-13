#importando el modulo
#la biblioteca array y renombrado 
from array import array as arr

def print_array(input):
    for element in input:
        print(element, end=",")
    print("\b")


my_array = arr('i', [2,10,15,20]) #se le asigna tippo de dato y
print_array(my_array)

#buscar el elemento 15 en el arreglo
number_to_search = 15
counter = 0
print(f"Se busca {number_to_search} en el arreglo.")
for i in range(len(my_array)):
    if my_array[i] == number_to_search:
        print("🎉Número encontrado")
        #sirve para salir del ciclo for y no seguir buscando
        break
    #incrementamos el contador para saber cuantas veces se ejecuta el ciclo for
    counter += 1
    print("😡 Número no encontrado")