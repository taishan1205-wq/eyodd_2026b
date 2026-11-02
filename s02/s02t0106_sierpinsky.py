from array import array as arr
from enum import Enum

#borra pantalla con caracterea ANSI
def clear_screen():
    print("\033[2J\033[H", end="")

#encapsulando los valores de ANSI en un enumerado
# codigo de colores en ANSI
class AnsiColor(Enum):
    red = "\033[91m"
    yellow = "\033[93m"
    cyan = "\033[96m"
    reset = "\033[0m"


#funcion par imprimir matriz
def print_matrix(input_matrix): #lo de los parentesis es un argumento
    for row in input_matrix:
        print(list(row))

#funcion para generar triangulo
def generate_triangle(rows = 1):
    #parametros de mi programa 
    #rows = 15
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
            # es decir un lemento esta despues del borde izq
            if col > 0:
                left_upper_cell = matrix[row-1][col-1]

            #si la columna esta un elemento antes del borde derecho 
            if col < columns - 1:
                right_uppert_cel = matrix[row-1][col+1]
            #Guardando el arreglo
            if left_upper_cell != right_uppert_cel:
                matrix[row][col] = 1
            else:
                matrix[row][col] = 0
    # regresando la matriz
    return matrix

#dibuja la matriz
def draw_matrix (input_matrix, symbol="*"):
    for row in input_matrix:
        for value in row:
            if value == 1:
                print(AnsiColor.cyan.value + symbol + AnsiColor.reset.value, end="")
            else:
                print(AnsiColor.red.value + " ", end="")
        print()

# metodo principal 
def main():
    # genera el triangulo de Sierpinsky
    matrix = generate_triangle(5)
    # Limpia la pantalla antes de dibujar la matriz
    clear_screen ()
    # Dubuja la matriz en pantalla 
    draw_matrix(matrix, symbol="■")

if __name__ == "__main__":
    main()