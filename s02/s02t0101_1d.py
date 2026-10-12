#importando el modulo Arrays
from array import array as arr

# Creando un arreglo
#i: entero con signo 
#I: entero sin signo
#f: número decimal
#d: Número decimal doble
#u:caracteres unicode 
my_array = arr('i', [10,22,300,3,7,40,55,80,700,654,34]) #se le asigna tippo de dato y 

#iterando (recorriendo) automaticamente 
# for num in my_array:
#     print(num, end=",")

# print("")    
# #acceso individual a elementos 
# print(my_array[0]) #primer elemento
# print(my_array[1]) #segundo elemento
# print(my_array[2]) #tercer elemento

#tamaño de un arreglo
#length
# print(len(my_array))

#Iteración por indices
for i in range(len(my_array)):
    #print(f"Elemento:{i+1}: {my_array[i]}")
    if my_array[i] %2 == 0:
        print(f"Elemento Num {i+1}: {my_array[i]}")