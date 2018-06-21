class Grafo:
	def __init__(self,grafo_dirigido):
		self.dic_vertice={}
		self.dirigido=grafo_dirigido
	def agregar_vertice(self,vertice):
		if vertice in self.dic_vertice:
			return False
		self.dic_vertice[vertice]={}
		return True
	def agregar_arista(self,vertice_A,vertice_B,peso):
		if vertice_A and vertice_B in self.dic_vertice:#fijater que no cause errores esta sintasis
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
		return False
	def borrar_arista(self,vertice_A,vertice_B):
		
	def pertenece_vertice(self,vertice):
		return vertice in self.dic_vertice
	def peso_arista(self,vertice_A,vertice_B):
		if vertice_A and vertice_B in self.dic_vertice:
			dic_arista_A=self.dic_vertice[vertice_A]
			if  vertice_B in dic_arista_A:
				return dic_arista_A[vertice_B]
		return False
	def __str__(self):
		return "{}".format(self.raiz)
grafo1=Grafo(False)
grafo1.agregar_vertice("A")
grafo1.agregar_vertice("B")
grafo1.agregar_arista("A","B",3)




