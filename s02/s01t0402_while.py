''' 
escribir un programa que calcule la suma 
de los "n" números naturales.
Por ejemplo si n=100 el programa
calculará la suma del 1 al 100
usando un ciclo while
'''
#importamos biblioteca time (sirve para calcular el tiempo)
import time

# creación de variables para
# el problema 
n = 100
the_sum = 0

#tomando el tiempo 1
timestamp_01 = time.time()

#iniciando la suma
#mientras=while
while(n > 0):
    the_sum = the_sum + n #100 + 99 + 98
    n = n-1
#tomamos el tiempo 2
timestamp_02 = time.time()

#imprimimos la solucion
print(f"La suma es {the_sum}")

#calculamos el tiempo
elapsed_time = round((timestamp_02-timestamp_01) * 1e6,2)
print(f"Tiempo de ejecución: {elapsed_time} μs")