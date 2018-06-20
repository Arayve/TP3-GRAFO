class Ciudad:
	def __init__(self,nombre,lat,longitud):
		self.nombre = nombre
		self.lat = lat
		self.long = longitud
	def __str__(self):
		return "Ciudad {},Latitud {},Longitud {})".format(self.nombre,self.lat,self.long)
"""Grafo dirigido y pesado"""
class Grafo:
	def __init__(self):
		self.raiz={}#cambiale el nombre si queres
		self.cantidad= 0 
	def agregar_vertice(self,ciudad):
		if ciudad in self.raiz:
			return #Quiero preguntar , al profesor si debo levantar error
		self.raiz[ciudad]={}
	def agregar_arista(self,cuidad_partida,ciudad_llegada,tiempo):#consultar que debo hacer si no existe cuidad de partida o llegada
		"""Si no existe cuidad partida o llegada lo crea"""
		dic_ciudad=self.raiz.get(cuidad_partida,{})
		dic_ciudad[ciudad_llegada]=tiempo
	def pertenece_vertice(self,cuidad):
		if cuidad in self.raiz:
			return True
	def peso_arista(self,cuidad_partida,ciudad_llegada):

	def __str__(self):
		return "{}".format(self.raiz)

cuidad1 = Ciudad("Moscu",55.755833,37.617778)
cuidad2 = Ciudad("San Petesburgo",59.950000,30.316667)
cuidad3 = Ciudad("Kaliningrado",54.716667,20.500000)
cuidad4 = Ciudad("Kazan",55.790833,49.114444)
cuidad5 = Ciudad("Nizhni Novgorod",56.326944,44.0075)

grafo=Grafo()
grafo.agregar_vertice(cuidad1)
grafo.agregar_vertice(cuidad2)
grafo.agregar_vertice(cuidad3)
grafo.agregar_vertice(cuidad4)
grafo.agregar_vertice(cuidad5)

grafo.agregar_arista(cuidad1,cuidad2,34)
if grafo.pertenece_vertice(cuidad1):
	print("SI pertenece")
"""
for clave1,valor1 in grafo.raiz.items():
	print(clave1)
	for clave2,valor2 in valor1.items():
		print(clave2)
		print(valor2)
"""