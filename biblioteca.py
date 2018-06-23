from grafo import Grafo
import heapq

def reconstruir_camino(padre,hasta):
	pos=0
	aux = hasta
	camino=[]
	while padre[aux]:
		aux=padre[aux]



def camino_minimo(grafo, desde, hasta):
	if  not grafo.pertence_vertice(desde) and not grafo.pertence_vertice(hasta):
		return None
	dist={}
	padre={}
	for v in grafo.obtener_todos_vertice():
		dist[v]= float('inf')
	dist[desde]= 0
	padre[desde]=None
	heap=[]
	heappush(heap,(dist[desde],desde))
	while len(heap) != 0:
		v=heappop(h)
		for w in grafo.adyacentes_vertice(v):
			if dist[v]+grafo.peso_arista(v,w)< dist[w]:
				padre[w]=v
				dist[w]=dist[v]+grafo.peso_arista(v,w)
				heappush(heap,(dist[w],w))

