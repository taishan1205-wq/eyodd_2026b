# Creamos una lista de estudiantes
student_list_01 = ['Jordan','Pipen','Curry','Shack',
                'Monroy', 'Arlet', 'Palestina'] # O(1) ----- resp correcta O(1) esta no se toma en cuenta

def random_function(students):
    first = students[0] # O(n) ----- resp correcta O(1)
    total = 0 # O(1) ----- resp correcta O(1)
    new_list = [] # O(1) ----- resp correcta O(1)

    for student in students:
        print("se le suma 1 al total")
        total += 1 # O(1) ----- resp correcta O(n)
        new_list.append(student) # O(n) ----- resp correcta O(n)

    print(new_list) # O(1) ----- resp correcta O(1)
    return total # O(1) ----- resp correcta O(1)

print(f"tamaño de lista: {len(student_list_01)}")
print(random_function(student_list_01))
print("")
# Calcular O(3n + 5) = O(n) ----- resp correcta O(2n) + O(5)= O(2n + 5)= O(n)

#la complejidad de un for siempre es O(n)
# Y si dentro de un for hay otro for es O(n^2)
