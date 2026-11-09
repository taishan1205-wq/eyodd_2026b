# Importando nodo
from S02T0201_linked_list import Node

# 1 Creo funcion principal
def main():
    # 2 coloco el cofigo ejecutable 
    test_node = Node("Prueba")

    print(f"Valor del nodo: {test_node.data}")

# Evaluo el valor de __name__
 if __name__ == "__main__":
    main()