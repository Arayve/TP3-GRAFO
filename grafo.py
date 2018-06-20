class Ciudad:
	def __init__(self,nombre,lat,longitud):
		self.nombre = nombre
		self.lat = lat
		self.long = longitud
	def __str__(self):
		return "Ciudad {},Latitud {},Longitud {})".format(self.nombre,self.lat,self.long)

class Grafo:
	def __init__(self):
		self.raiz={}#cambiale el nombre si queres
		self.cantidad= 0 
	def agregar_vertice(self,ciudad):
		if ciudad in self.raiz:
			return #Quiero preguntar , al profesor si debo levantar error
		self.raiz[ciudad]={}
	def agregar_arista(self,cuidad_partida,ciudad_llegada,tiempo):
		"""Si no existe cuidad partida o llegada lo crea"""
		aux=Campo(vertice_entrante,valor)
		dic_ciudad=self.raiz.get(cuidad_partida,{})
		dic_ciudad[ciudad_llegada]=tiempo
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

for x in grafo.raiz.keys():
	print(x)