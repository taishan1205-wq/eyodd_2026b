''' 
escribir un programa que calcule la suma 
de los "n" números naturales.
Por ejemplo si n=100 el programa
calculará la suma del 1 al 100
'''

#importamos biblioteca time (sirve para calcular el tiempo)
import time

#tomando el tiempo inicial
timestamp_01 = time.time()  #toda funcion se invoca con parentesis

#Programa q calculá la suma de los "n" números naturales 

n = 100
total_sum = 0
#range nos proporciona un tren de datos (genera números)
#Ciclo for
for number in range(1, n+1):
    total_sum = total_sum + number
    #total_sum <- 0+1
    #total_sum =1
    #total_sum<- 1+

print(F"La suma de 1 hasta {n} es: {total_sum}")

#tomando el tiempo final 
timestamp_02 = time.time()

#impresión del tiempo de ejecución
print(f"Tiempo de ejecución: {(timestamp_02-timestamp_01) * 1e6 :.2f} μs")