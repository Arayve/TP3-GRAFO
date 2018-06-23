from grafo import Grafo
import heapq

def reconstruir_camino(padre,hasta):
	aux = hasta
	camino=[]
	camino.append(aux)
	while True:
		tupla=padre[aux]
		if tupla is None:
			return camino
		aux = tupla[1]
		camino.append(aux)

def camino_minimo(grafo, desde, hasta):
	if  not grafo.pertenece_vertice(desde) and not grafo.pertenece_vertice(hasta):
		return None
	dist={}
	padre={}
	for v in grafo.obtener_todos_vertice():
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
grafo1=Grafo(True)
grafo1.agregar_vertice("A")
grafo1.agregar_vertice("B")
grafo1.agregar_vertice("C")
grafo1.agregar_vertice("D")
grafo1.agregar_vertice("E")
grafo1.agregar_arista("A","B",5)
grafo1.agregar_arista("A","D",8)
grafo1.agregar_arista("B","C",2)
grafo1.agregar_arista("C","E",1)
grafo1.agregar_arista("D","E",1)
print(camino_minimo(grafo1,"A","E"))