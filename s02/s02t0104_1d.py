# Eliminacion 
#
#
from array import array as arr
#importando una funcion de otro archivo 
from s02t0102_1d import print_array

my_array = arr('i', [2,10,15,20,10])

print("-------Antes de la eliminación-------")
print_array(my_array)

#eliminación
try:
    my_array.remove(10) # solo elimina la primera ocurrencia del numero a eliminar 
except:
    print("⚠️ Elemento no encontrado !!!")

number_to_remove = 10
while number_to_remove in my_array:
    my_array.remove(number_to_remove)
# for i in range(len(my_array)):
#     if my_array [i] == number_to_remove:
#         my_array.remove(number_to_remove)
#     break
print("-------Después de la eliminación-------")
print_array(my_array)
