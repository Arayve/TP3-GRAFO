from random import choice

class Grafo:
	def __init__(self,grafo_dirigido):
		self.dic_vertice={}
		self.dirigido=grafo_dirigido
	def agregar_vertice(self,vertice):
		if vertice in self.dic_vertice:
			return False
		self.dic_vertice[vertice]={}
		return True
	def borrar_vertice(self,vertice):
		if not vertice in self.dic_vertice:
			return False
		self.dic_vertice.pop(vertice)
		for dic_arista in self.dic_vertice.values():
			if vertice in dic_arista:
				dic_arista.pop(vertice)
		return True
	def adyacentes_vertice(self,vertice):
		lista=[]
		if not vertice in self.dic_vertice:
			return None
		dic_arista=self.dic_vertice[vertice]
		for w in dic_arista.keys():
			lista.append(w)
		return lista
	def agregar_arista(self,vertice_a,vertice_b,peso):
		if not (vertice_a in self.dic_vertice and vertice_b in self.dic_vertice):
			return False
		dic_arista_a=self.dic_vertice[vertice_a]
		if vertice_b in dic_arista_a:
			return False
		dic_arista_a[vertice_b]=peso
		if not self.dirigido:
			dic_arista_b=self.dic_vertice[vertice_b]
			dic_arista_b[vertice_a]=peso
		return True
	def borrar_arista(self,vertice_a,vertice_b):
		if not (vertice_a in self.dic_vertice and vertice_b in self.dic_vertice):
			return None
		dic_arista_a = self.dic_vertice[vertice_a]
		if not  vertice_b in dic_arista_a:
			return None
		peso = dic_arista_a.pop(vertice_b)
		if not self.dirigido:
			dic_arista_b=self.dic_vertice[vertice_b]
			dic_arista_b.pop(vertice_a)
		return peso
	def pertenece_vertice(self,vertice):
		return vertice in self.dic_vertice
	def peso_arista(self,vertice_a,vertice_b):
		if not (vertice_a in self.dic_vertice and vertice_b in self.dic_vertice):
			return None
		dic_arista_a=self.dic_vertice[vertice_a]
		if not  vertice_b in dic_arista_a:
			return None
		return dic_arista_a[vertice_b]
	def obtener_vertice_aleatorio(self):
		lista=[]
		for vertice in self.dic_vertice.keys():
			lista.append(vertice)#QUISE hacer un random al diccionario pero aveces daba error
		return choice(lista)
	def obtener_todos_vertices(self):
		"""Devuelve tdos los vertice en una lista"""
		lista=[]
		for vertice in self.dic_vertice.keys():
			lista.append(vertice)
		return lista
	def cantidad_vertice(self):
		return len(self.dic_vertice)
	def __str__(self):
		return "{}".format(self.dic_vertice)

