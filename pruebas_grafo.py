from grafo import Grafo

def print_test(mensaje, ok):

	if ok:
		print(mensaje + "...OK")
	else:
		print(mensaje + "...ERROR")

grafo = Grafo(True)

print("PRUEBAS GRAFO VACIO")

print_test("Se creo grafo", grafo != None)
print_test("Grafo esta vacio", grafo.cantidad_vertice() == 0)
print_test("Grafo borrar vertice devuelve False", grafo.borrar_vertice("A") == False)
print_test("Grafo adyacentes al vertice devuelve None", grafo.adyacentes_vertice("A") == None)
print_test("Grafo borrar arista devuelve None", grafo.borrar_arista("A", "B") == None)
print_test("Grafo pertenece vertice devuelve False", grafo.pertenece_vertice("A") == False)
print_test("Grafo peso arista devuelve None", grafo.peso_arista("A", "B") == None)
#print_test("Grafo obtener vertice aleatorio devuelve None", grafo.obtener_vertice_aleatorio() == None)
print_test("Grafo obtener todos los vertices devuelve lista vacia", len(grafo.obtener_todos_vertices()) == 0)
