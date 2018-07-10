from grafo import Grafo
from cola import Cola
import heapq

def reconstruir_camino(padre,hasta):
	aux = hasta
	lista=[]
	lista.append(aux)
	while True:
		v=padre[aux]
		if v is None:
			break
		aux = v
		lista.append(v)
	return lista[::-1]#invierto la lista
def camino_minimo(grafo, desde, hasta):
	if  not grafo.pertenece_vertice(desde) and not grafo.pertenece_vertice(hasta):
		return None,None
	dist={}
	padre={}
	for v in grafo.obtener_todos_vertices():
		dist[v]= float('inf')
	dist[desde]= 0
	padre[desde]=None
	heap=[]
	heapq.heappush(heap,(dist[desde],desde))
	while len(heap) != 0:
		(dist_v,v)=heapq.heappop(heap)
		for w in grafo.adyacentes_vertice(v):
			if dist_v+grafo.peso_arista(v,w)< dist[w]:
				padre[w]=v
				dist[w]=dist_v+grafo.peso_arista(v,w)
				heapq.heappush(heap,(dist[w],w))
	return reconstruir_camino(padre,hasta),dist[hasta]

def orden_topologico(grafo):
	"""Solo funciona para grafo dirigido"""
	resultado=[]
	cola = Cola()
	orden={}
	for v in grafo.obtener_todos_vertices():
		orden[v]=0
	for v in grafo.obtener_todos_vertices():
		for w in grafo.adyacentes_vertice(v):
			orden[w]+=1
	for v in grafo.obtener_todos_vertices():
		if(orden[v]==0):
			cola.encolar(v)
	while not cola.esta_vacia():
		v = cola.desencolar()
		resultado.append(v)
		for w in grafo.adyacentes_vertice(v):
			orden[w]-=1
			if orden[w]==0:
				cola.encolar(w)
	return resultado
def arbol_tendido_minimo(grafo):
	"""Recibe un grafo no dirigido y conexo.Devuelve un grafo no dirigido"""
	grafo_aux=Grafo(False)
	heap=[]
	visitados=set()
	peso_total=0
	v=grafo.obtener_vertice_aleatorio()
	grafo_aux.agregar_vertice(v)
	visitados.add(v)
	for w in grafo.adyacentes_vertice(v):
		peso=grafo.peso_arista(v,w)
		heapq.heappush(heap,(peso,w,v))
	while len(heap) != 0:
		(peso,w,v)=heapq.heappop(heap)
		if w in visitados:
			continue
		peso_total+=peso
		grafo_aux.agregar_vertice(w)
		visitados.add(w)
		grafo_aux.agregar_arista(v,w,peso)
		for z in grafo.adyacentes_vertice(w):
			peso=grafo.peso_arista(w,z)
			heapq.heappush(heap,(peso,z,w))
	return grafo_aux , peso_total

def _viajante(grafo,origen,vertice,resultado,soluciones,costo,visitados):
	"""Nos movemos para cada adyacente, vamos guardando el resultado y los visitados para cada posibilidad, si cumple la condicion 
	del viajante, nos lo guardamos en el heap  como una posible solucion del viajante.Poda: que el costo sea menor al menor del heap 
	Creamos resultado_aux y visitados_aux ,debido que si  usamos los originales , en cada adyacentes, los originales poseeria las 
	soluciones del anterior """
	if vertice == origen:
		if len(resultado) == grafo.cantidad_vertice()+1:
			heapq.heappush(soluciones,(costo,resultado))
		return None,None
	for w in grafo.adyacentes_vertice(vertice):
		if w in visitados:
			continue
		nuevo_costo=costo+grafo.peso_arista(vertice,w)	
		if soluciones and nuevo_costo >= soluciones[0][0]:# soluciones[0][0] es la solucion mas pequeña que poseemos 
			continue
		resultado_aux=resultado[:]
		resultado_aux.append(w)
		visitados_aux=set()
		visitados_aux= visitados_aux | visitados
		visitados_aux.add(w)
		_viajante(grafo,origen,w,resultado_aux,soluciones,nuevo_costo,visitados_aux)

def viajante(grafo, origen):
	if  not grafo.pertenece_vertice(origen):
		return None,None
	soluciones = []
	for w in grafo.adyacentes_vertice(origen):
		resultado=[]
		visitados=set()
		resultado.append(origen)
		resultado.append(w)
		visitados.add(w)
		costo = grafo.peso_arista(origen,w)
		_viajante(grafo,origen,w,resultado,soluciones,costo,visitados)
	(costo_menor,resultado)=heapq.heappop(soluciones)
	return resultado,costo_menor

def _agregar_adyacentes_heap(grafo,heap,vertice):
	for w in grafo.adyacentes_vertice(vertice):
		cant = grafo.peso_arista(vertice,w)
		heapq.heappush(heap,(cant,w))

def _viajante_aproximado(grafo,origen,vertice,resultado,visitados,peso):
	if len(resultado) == grafo.cantidad_vertice():
			peso+=grafo.peso_arista(resultado[-1],origen)
			resultado.append(origen)
			return resultado,peso
	heap=[]
	_agregar_adyacentes_heap(grafo,heap,vertice)
	while heap:
		(costo,w)=heapq.heappop(heap)
		if not w in visitados:
			visitados.add(w)
			resultado.append(w)
			peso+=costo
			return _viajante_aproximado(grafo,origen,w,resultado,visitados,peso)
	return None,None

def viajante_aproximado(grafo,origen):
	if  not grafo.pertenece_vertice(origen):
		return None,None
	heap=[]
	resultado=[]
	visitados=set()
	_agregar_adyacentes_heap(grafo,heap,origen)
	(costo,w)=heapq.heappop(heap)
	peso=costo
	visitados.add(origen)
	visitados.add(w)
	resultado.append(origen)
	resultado.append(w)
	return _viajante_aproximado(grafo,origen,w,resultado,visitados,peso)
def recorrer_grafo(grafo):
	"""Recorre el grafo, y devuelve una lista de lista , donde las listas segunda posee las arista.Funcion usaba para escribir en csv
	las aristas usando el writerows"""
	resultado=[]
	visitados=set()
	lista_vertices=grafo.obtener_todos_vertices()
	for v in lista_vertices:
		for w in grafo.adyacentes_vertice(v):
			if (v,w) in visitados or (w,v) in visitados:
				continue
			cant=grafo.peso_arista(v,w)
			resultado.append([v,w,cant])
			visitados.add((v,w))
			visitados.add((w,v))
	return resultado