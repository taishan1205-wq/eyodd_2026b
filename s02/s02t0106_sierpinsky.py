from array import array as arr

#parametros de mi programa 
rows = 10
columns = 2*rows - 1

#funcion par imprimir matriz
def print_matrix(input_matrix): #lo de los parentesis es un argumento
    for row in input_matrix:
        print(list(row))

#creando la reticula bidimencional 2D
matrix = []
#construllendo el grid (regilla)
for _ in range(rows):
    new_row = arr('i',[0] * columns) #creando una fila de ceros
    matrix.append(new_row)

#validando la construccion del grid
print(f"Cantidad de filas: {len(matrix)}")
print(f"Cantidad de columnas: {len(matrix[0])}")


#CALCULANDO EL CENTRO DE LA PRIMERA FILA 
center = columns // 2 #doble // se hace divicion entera 

#estableciendo el centro en 1 
matrix[0][center]=1
#print_matrix(matrix) #imprimiendo la matriz
# se calcula el rsto de la matriz siguiendo la logica 
# del sierpinsky Gasket

for row in range(1, rows):
    for col in range(0,columns):
        left_upper_cell = 0
        right_uppert_cel = 0

        #si la columna donde estamos es mayor a 0
        if col > 0:
            left_upper_cell = matrix[row-1][col-1]

        #si la columna esta un elemento antes del borde derecho 
        if col > columns - 1:
            right_uppert_cel = matrix[row-1][col+1]
        #Guardando el arreglo
        if left_upper_cell != right_uppert_cel:
            matrix[row][col] = 1
        else:
            matrix[row][col] = 0
print()
print_matrix(matrix)