
from array import array as arr

#ompresión de una tabla 
#se convierte en una función para mandarlo llamar de manera más eficiente 
def print_table(input_table):
    #imprimiendo caDA ELEMENTO     
    for row in input_table:
        for colomn in row:
            print(colomn, end=",")
        print("\b ")
#dont repit yourself (DRY)
table = [
    arr('i', [1,2,3]),
    arr('i', [4,5,6]),
    arr('i', [7,8,9])
]
print_table(table)

# insercion
row = 1
column = 2
value = 99

#insertar en la columna 2 el valor 99
table[row].insert(column, value)

#imprimiendo mensaje 
print("_______Después de la inserción_______")
print_table(table) #DRY

#insertando una fila completa 
new_row = arr('i', [100,200,300])
pos = 1
table.insert(pos, new_row)

#imprimiendo mensaje 
print("_______Después de la inserción del elemento_______")
print_table(table) #DRY

#eliminando datos 
del table[2]
#imprimiendo mensaje 
print("_______Después de la eliminación de la fila 2 _______")
print_table(table) #DRY