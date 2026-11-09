# Creando la clase Nodo
class Node:
    # Constructor
    def __init__(self, data=None):
        self.data = data
        self.next = None
    def iter(self):
        current = self
        while current:
            value = current.data
            current = current.next
            yield value


# Creando una funcion principal 
def main ():
    # Código de prueba
    # Testear nuestra clase Nodo
    node_01 = Node("eggs")
    node_02 = Node("ham")
    node_03 = Node("bacon")
    # print("🔗 NOODES SIN ENLAZAR 🔗")
    # print(f"Node 01: D:{node_01.data} - N: {node_01.next}")
    # print(f"Node 02: D:{node_02.data} - N: {node_02.next}")
    # print(f"Node 03: D:{node_03.data} - N: {node_03.next}")

    # Enlazando los nnodos
    node_01.next = node_02
    node_02.next = node_03

    #print("🔗 NOODES ENLAZADOS 🔗")
    # print(f"Node 01: D:{node_01.data} - N: {node_01.next}")
    # print(f"Node 02: D:{node_02.data} - N: {node_02.next}")
    # print(f"Node 03: D:{node_03.data} - N: {node_03.next}")

    #list Transversal (recorrido de lista)
    for node_value in node_01.iter():
        print(node_value)
    # for una cantidad determinada de repeticiones 
    # while no se sabe hasta que mamento para 

# Invocando a Main 
if __name__ == "__main__":
    main()