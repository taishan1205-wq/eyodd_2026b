#importando el modulo
#la biblioteca array y renombrado 
from array import array as arr

def print_array(input):
    for element in input:
        print(element, end=",")
    print("\b")


my_array = arr('i', [2,10,15,20]) #se le asigna tippo de dato y
print_array(my_array)