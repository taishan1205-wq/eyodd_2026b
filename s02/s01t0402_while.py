''' 
escribir un programa que calcule la suma 
de los "n" números naturales.
Por ejemplo si n=100 el programa
calculará la suma del 1 al 100
usando un ciclo while
'''
#importamos biblioteca time (sirve para calcular el tiempo)
import time

def sum_of_n (n):
    the_sum = 0
    while(n > 0):
        the_sum = the_sum + n #100 + 99 + 98
        n = n-1
    return the_sum

dataset = []

#generación del contenido de dataset
for repeticion in range(1,11):
    n = repeticion * 500

    timestamp_01 = time.time()
    result = sum_of_n(n)
    timestamp_02 = time.time()

    elapsed_time = round((timestamp_02 - timestamp_01) * 1e6, 2)
    dataset.append((n, elapsed_time, result))

# Impresión del dataset generado
for tup in dataset:
    print(tup)
