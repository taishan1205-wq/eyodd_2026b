''' 
escribir un programa que calcule la suma 
de los "n" números naturales.
Por ejemplo si n=100 el programa
calculará la suma del 1 al 100
'''

#importamos biblioteca time (sirve para calcular el tiempo)
import time

#función que suma los primeros n número naturales 

def sum_of_n (n):
    total_sum = 0
    #suamndo los "n" numeros
    #Ciclo for
    for number in range(1, n+1):
        total_sum = total_sum + number
    return total_sum

#variable para guardar 
# el data set
dataset = [] #[(n,time_laps,sum), ]
#generando el contenido de dataset
for repetition in range(1,11):

    #⏱️tomo el tiempo 1 (inicial)
    timestamp_01 = time.time()  #toda funcion se invoca con parentesis
    
    #sumo los "n" números
    n = repetition*500
    result = sum_of_n(n)
    
    #⏱️tomando el tiempo final 
    timestamp_02 = time.time()
    
    #calculamos el tiempo
    elapsed_time = round((timestamp_02-timestamp_01) * 1e6,2)
    
    #agreasgr la tripleta de los datos al dataset
    dataset.append( (n,elapsed_time,result) )

for tup in dataset:
    print(tup)

# μs