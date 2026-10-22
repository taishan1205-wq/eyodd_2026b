from array import array as arr

#parametros de mi programa 
rows = 8
columns = 2*rows - 1

#creando la reticula bidimencional 2D
matrix = []
#construllendo el grid (regilla)
for _ in range(rows):
    new_row = arr('i',[0] * columns) #creando una fila de ceros
    matrix.append(new_row)

#validando la construccion del grid
print(f"Cantidad de filas: {len(matrix)}")
print(f"Cantidad de columnas: {len(matrix[0])}")

for row in matrix:
    print(list(row))