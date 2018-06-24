from grafo import Grafo
from cola import Cola
from pila import Pila
import heapq

def reconstruir_camino(padre,hasta):
	aux = hasta
	camino=[]
	pila=Pila()
	pila.apilar(aux)
	while True:
		tupla=padre[aux]
		if tupla is None:
			break
		aux = tupla[1]
		pila.apilar(aux)
	while not pila.esta_vacia():
		camino.append(pila.desapilar())
	return camino
def camino_minimo(grafo, desde, hasta):
	if  not grafo.pertenece_vertice(desde) and not grafo.pertenece_vertice(hasta):
		return None
	dist={}
	padre={}
	for v in grafo.obtener_todos_vertices():
		dist[v]= float('inf')
	dist[desde]= 0
	padre[desde]=None
	heap=[]
	heapq.heappush(heap,(dist[desde],desde))
	while len(heap) != 0:
		v=heapq.heappop(heap)#v es una tupla
		for w in grafo.adyacentes_vertice(v[1]):
			if dist[v[1]]+grafo.peso_arista(v[1],w)< dist[w]:
				padre[w]=v
				dist[w]=dist[v[1]]+grafo.peso_arista(v[1],w)
				heapq.heappush(heap,(dist[w],w))

	return reconstruir_camino(padre,hasta)

def orden_topologico(grafo):
	"""Solo funciona para grafo dirigido"""
	visitados=set()
	lista=[]
	cola = Cola()
	orden={}
	for v in grafo.obtener_todos_vertices():
		orden[v]=0
	for v in grafo.obtener_todos_vertices():
		for w in grafo.adyacentes_vertice(v):
			orden[w]=1
	for v in grafo.obtener_todos_vertices():
		if(orden[v]==0):
			cola.encolar(v)
	while not cola.esta_vacia():
		v = cola.desencolar()
		visitados.add(v)
		if not v in lista:
			lista.append(v)
		for w in grafo.adyacentes_vertice(v):
			if not w in visitados:
				orden[w]=0#creo que es inecesario
				cola.encolar(w)
	return lista
def arbol_tendido_minimo(grafo):
	"""Recibe un grafo no dirigido y conexo.Devuelve un grafo no dirigido"""
	grafo_aux=Grafo(False)
	padre={}
	heap=[]
	visitados=set()
	v=grafo.obtener_vertice_aleatorio()
	grafo_aux.agregar_vertice(v)
	visitados.add(v)
	for w in grafo.adyacentes_vertice(v):
		padre[w]=v
		peso=grafo.peso_arista(v,w)
		heapq.heappush(heap,(peso,w))
	while len(heap) != 0:
		tupla=heapq.heappop(heap)
		if tupla[1] in visitados:
			continue
		grafo_aux.agregar_vertice(tupla[1])
		visitados.add(tupla[1])
		grafo_aux.agregar_arista(padre[tupla[1]],tupla[1],tupla[0])
		for w in grafo.adyacentes_vertice(tupla[1]):
			padre[w]=tupla[1]
			peso=grafo.peso_arista(tupla[1],w)
			heapq.heappush(heap,(peso,w))
	return grafo_aux
def _viajante(grafo,origen,vertice,lista,heap,cant):
	if lista[-1] == origen:
		if len(lista) == grafo.cantidad_vertice()+1:
			heapq.heappush(heap,(cant,lista))
		return
	for w in grafo.adyacentes_vertice(vertice):
		lista_aux=lista[:]
		lista_aux.append(w)
		nueva_cant=cant+grafo.peso_arista(vertice,w)
		_viajante(grafo,origen,w,lista_aux,heap,nueva_cant)
	return
def viajante(grafo, origen):#fuerza bruta , grafo dirigido y pesado
	if  not grafo.pertenece_vertice(origen):
		return None
	heap = []
	for w in grafo.adyacentes_vertice(origen):
		lista=[]
		lista.append(origen)
		lista.append(w)
		cant = grafo.peso_arista(origen,w)
		_viajante(grafo,origen,w,lista,heap,cant)
	if heap==[]:
		return None
	tupla=heapq.heappop(heap)
	return tupla[1]

"""
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
print(camino_minimo(grafo1,"A","E"))
print(orden_topologico(grafo1))

grafo2=Grafo(False)
grafo2.agregar_vertice("A")
grafo2.agregar_vertice("B")
grafo2.agregar_vertice("C")
grafo2.agregar_vertice("D")
grafo2.agregar_vertice("E")
grafo2.agregar_vertice("F")
grafo2.agregar_arista("A","B",5)
grafo2.agregar_arista("A","D",8)
grafo2.agregar_arista("B","C",2)
grafo2.agregar_arista("C","E",1)
grafo2.agregar_arista("D","E",3)
grafo2.agregar_arista("A","F",4)
grafo2.agregar_arista("E","F",100)
arbol_minimo=arbol_tendido_minimo(grafo2)
print(arbol_minimo)

grafo3=Grafo(True)
grafo3.agregar_vertice("A")
grafo3.agregar_vertice("B")
grafo3.agregar_vertice("C")
grafo3.agregar_vertice("D")
grafo3.agregar_arista("A","B",3)
grafo3.agregar_arista("A","C",1)
grafo3.agregar_arista("C","D",4)
grafo3.agregar_arista("C","B",2)
grafo3.agregar_arista("B","D",3)
grafo3.agregar_arista("D","A",1)
print(viajante(grafo3,"A"))
"""
grafo4=Grafo(True)
grafo4.agregar_vertice("A")
grafo4.agregar_vertice("B")
grafo4.agregar_vertice("C")
grafo4.agregar_vertice("D")
grafo4.agregar_vertice("E")
grafo4.agregar_vertice("F")
grafo4.agregar_vertice("G")
grafo4.agregar_vertice("H")
grafo4.agregar_arista("A","C",1)
grafo4.agregar_arista("A","B",2)
grafo4.agregar_arista("B","C",2)
grafo4.agregar_arista("B","D",2)
grafo4.agregar_arista("D","E",2)
grafo4.agregar_arista("E","G",3)
grafo4.agregar_arista("E","F",2)
grafo4.agregar_arista("C","D",1)
grafo4.agregar_arista("D","F",1)
grafo4.agregar_arista("F","G",1)
grafo4.agregar_arista("G","H",1)
grafo4.agregar_arista("H","A",2)
print(viajante(grafo4,"A"))