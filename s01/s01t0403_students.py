'''
1.- identifico el tamaño de entrada "n"
el tamaño de la entrada es el numero 
de estudiantes:
2.- Es ver cuanto crece el numero de
operaciones en mi algoritmo  conforme
crece el tamaño de la entrada 
3.- agrego las bigO identificadas
teniendo en cuenta la cota superior  asintontica ( la de mayor exponente) 
O(n) + 4*O(1) = O(n + 4) = O(n)
'''



#creando una lista de estudiantes
student_list_01 = ['Jordan', 'Pipen', 'Curry', 'Shack']
student_list_02 = ['Mike', 'Saul', 'Walter', 'Jessy']

#verificando la presencia de un estudiante 
def chek_student(input_student, student_list):
    for student in student_list:
        if input_student == student: # O(n)
            print("✔️Estudiante encontrado.") # O(1)
            return student # O(1)
    # si no encontramos al estudiante 
    print("❌Estudiante no encontradao") # tiene complejidad constante O(1)
    return None # O(1)

#probando algoritmo
chek_student("Walter", student_list_02)

