#importando el modulo Arrays
from array import array as arr

# Creando un arreglo
array_01 = arr('i', [3,8,5,1,6])

#iterando (recorriendo) automaticamente 
for data in array_01:
    print(data, end=",")

print("")    