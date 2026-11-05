"""
Generators 
Los generadores son funciones que pueden pausar su ejecución
cuando se invoca una funcion generadora devuelve un objeto ineredor (aka iterador)

el codigo dentro de la funcion no se ejecuta de inmediato, 
solo se compila 
La función solo se ejecuta unicamente cuando iteras sobre el generador 
"""

def my_generator():
    yield 1 # yield significa producir
    yield 2
    yield 3
    yield 4
    
#se invoca funcion generadora
my_iterator = my_generator()

#se itera manualmente osbre el iterador 
# print(next(my_iterator)) # imprime 1
# print(next(my_iterator)) # imprime 2
# print(next(my_iterator)) # imprime 3
# print(next(my_iterator)) # imprime 4

#los iteradores se pueden iterar con un for 
for value in my_iterator:
    print(value)