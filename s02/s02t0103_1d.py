# 
#
#
from array import array as arr
#importando una funcion de otro archivo 
from s02t0102_1d import print_array

my_array = arr('i', [2,10,15,20])

print("-------Antes de la inserción-------")
print_array(my_array)

#inserción
my_array.insert(1,90)

print("-------Después de un apend-------")
my_array.append(1000)
print_array(my_array)   

print("-------simular un apend con insert-------")
my_array.insert(len(my_array), 9000)
print_array(my_array)   

#print("-------Después de la inserción-------")
#print_array(my_array)   
