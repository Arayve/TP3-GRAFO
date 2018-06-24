from grafo import Grafo

def print_test(mensaje, ok):

	if ok:
		print(mensaje + "...OK")
	else:
		print(mensaje + "...ERROR")

grafo_vacio = Grafo(True)

print("PRUEBAS GRAFO VACIO")

print_test("Se creo grafo", grafo_vacio != None)
print_test("Grafo esta vacio", grafo_vacio.cantidad_vertice() == 0)
print_test("Grafo borrar vertice devuelve False", grafo_vacio.borrar_vertice("A") == False)
print_test("Grafo adyacentes al vertice devuelve None", grafo_vacio.adyacentes_vertice("A") == None)
print_test("Grafo borrar arista devuelve None", grafo_vacio.borrar_arista("A", "B") == None)
print_test("Grafo pertenece vertice devuelve False", grafo_vacio.pertenece_vertice("A") == False)
print_test("Grafo peso arista devuelve None", grafo_vacio.peso_arista("A", "B") == None)
#print_test("Grafo obtener vertice aleatorio devuelve None", grafo_vacio.obtener_vertice_aleatorio() == None)
print_test("Grafo obtener todos los vertices devuelve lista vacia", len(grafo_vacio.obtener_todos_vertices()) == 0)

print("\nPRUEBAS GRAFO DIRIGIDO AGREGAR Y BORRAR")

grafo = Grafo(True)

print_test("Se creo grafo", grafo != None)
print_test("Se agrego vertice", grafo.agregar_vertice("A"))
print_test("Grafo largo es 1", grafo.cantidad_vertice() == 1)
print_test("Grafo obtener vertice", grafo.pertenece_vertice("A"))
print_test("Grafo obtener adyacentes es lista vacia", len(grafo.adyacentes_vertice("A")) == 0)
print_test("Grafo obtener vertice aleatorio devuelve unico vertice", grafo.obtener_vertice_aleatorio() == "A")
print_test("Grafo obtener todos los vertices devuelve lista con 1 elemento", len(grafo.obtener_todos_vertices()) == 1)
print_test("Grafo borrar vertice devuelve True", grafo.borrar_vertice("A"))
print_test("Grafo largo es 0", grafo.cantidad_vertice() == 0)
print_test("Grafo obtener vertice devuelve False", grafo.pertenece_vertice("A") == False)

print("")

claves1 = ("A", "B", "C", "D")

print_test("Se agrego vertice A", grafo.agregar_vertice(claves1[0]))
print_test("Se agrego vertice B", grafo.agregar_vertice(claves1[1]))
print_test("Se agrego vertice C", grafo.agregar_vertice(claves1[2]))
print_test("Se agrego vertice D", grafo.agregar_vertice(claves1[3]))
print_test("Grafo largo es 4", grafo.cantidad_vertice() == 4)
print_test("Grafo agregar arista (A, B) devuelve True", grafo.agregar_arista("A", "B", 1))
print_test("Grafo agregar arista (B, C) devuelve True", grafo.agregar_arista("B", "C", 1))
print_test("Grafo agregar arista (C, D) devuelve True", grafo.agregar_arista("C", "D", 1))
print_test("Grafo largo es 4", grafo.cantidad_vertice() == 4)
#print_test("Grafo obtener todos los vertices", )






