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
		if  not vertice in self.dic_vertice:
			return False
		self.dic_vertice.pop(vertice)
		for dic_arista in self.dic_vertice.values():
			if vertice in dic_arista:
				dic_arista.pop(vertice)
		return True
	def adyacentes_vertice(self,vertice):
		if vertice in self.dic_vertice:
			return len(self.dic_vertice[vertice])
		
	def agregar_arista(self,vertice_A,vertice_B,peso):
		if not(vertice_A  in self.dic_vertice and vertice_B in self.dic_vertice):
			return False
		dic_arista_A=self.dic_vertice[vertice_A]
		if vertice_B in dic_arista_A:
			return False
		dic_arista_A[vertice_B]=peso
		if not self.dirigido:
			dic_arista_B=self.dic_vertice[vertice_B]
			"""if vertice_A in dic_arista_B:#creo que esta demas 
				return False"""
			dic_arista_B[vertice_A]=peso
		return True
	def borrar_arista(self,vertice_A,vertice_B):
		if not (vertice_A in self.dic_vertice and vertice_B in self.dic_vertice):
			return None
		dic_arista_A = self.dic_vertice[vertice_A]
		if not  vertice_B in dic_arista_A:
			return None
		peso = dic_arista_A.pop(vertice_B)
		if not self.dirigido:
			dic_arista_B=self.dic_vertice[vertice_B]
			dic_arista_B.pop(vertice_A)
		return peso
	def pertenece_vertice(self,vertice):
		return vertice in self.dic_vertice
	def peso_arista(self,vertice_A,vertice_B):
		if not(vertice_A in self.dic_vertice and vertice_B in self.dic_vertice):
			return None
		dic_arista_A=self.dic_vertice[vertice_A]
		if not  vertice_B in dic_arista_A:
			return None
		return dic_arista_A[vertice_B]
	def obtener_vertice_aleatorio(self):
		lista=[]
		for vertice in self.dic_vertice.keys():
			lista.append(vertice)#QUISE hacer un random al diccionario pero aveces daba error
		return choice(lista)
	def obtener_todos_vertice(self):
		"""Devuelve tdos los vertice en una lista"""
		lista=[]
		for vertice in self.dic_vertice.keys():
			lista.append(vertice)
		return lista
	def cantidad_vertice(self):
		return len(self.dic_vertice)
grafo1=Grafo(False)
grafo1.agregar_vertice("A")
grafo1.agregar_vertice("B")
grafo1.agregar_vertice("C")
grafo1.agregar_vertice("D")
grafo1.agregar_arista("A","B",3)
grafo1.agregar_arista("A","C",5)
print(grafo1.peso_arista("A","B"))
lista=grafo1.obtener_todos_vertice()
print(lista)
print(grafo1.obtener_vertice_aleatorio())
print(grafo1.cantidad_vertice())
print(grafo1.pertenece_vertice("D"))
print(grafo1.adyacentes_vertice("A"))
print(grafo1.borrar_vertice("A"))
print(grafo1.adyacentes_vertice("B"))
