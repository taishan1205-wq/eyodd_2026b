''' 
escribir un programa que calcule la suma 
de los "n" números naturales.
Por ejemplo si n=100 el programa
calculará la suma del 1 al 100
'''

#importamos biblioteca time (sirve para calcular el tiempo)
import time

#crear una marca de tiempo
timestamp_01 = time.time()  #toda funcion se invoca con parentesis

#Programa q calculá la suma de los "n" números naturales 

n = 100
sum = 0
#range nos proporciona un tren de datos 
#Ciclo for
for number in range(1, n+1):
    print(str(number) + " ")