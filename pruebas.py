from grafo import Grafo
import biblioteca

grafo1=Grafo(True)
grafo1.agregar_vertice("A")
grafo1.agregar_vertice("B")
grafo1.agregar_vertice("C")
grafo1.agregar_vertice("D")
grafo1.agregar_vertice("E")
grafo1.agregar_vertice("F")
grafo1.agregar_arista("A","B",5)
grafo1.agregar_arista("A","D",8)
grafo1.agregar_arista("B","C",2)
grafo1.agregar_arista("C","E",1)
grafo1.agregar_arista("D","E",3)
grafo1.agregar_arista("A","F",4)
grafo1.agregar_arista("E","F",100)
print(biblioteca.camino_minimo(grafo1,"A","E"))

print("hola", end = " -> ")
print("hola", end = " -> ")




