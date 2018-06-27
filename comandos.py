from grafo import Grafo
import biblioteca
import sys
import csv
CUIDAD="11"
RUTA="55"

def procesar_ir(grafo, desde, hasta):

	lista_camino,costo= biblioteca.camino_minimo(grafo, desde, hasta)
	lista_aux=lista_camino[:-1]
	if len(lista_camino)>1:
		for vertice in lista_aux:
			print(vertice, end = " -> ")
	print(lista_camino[-1])
	print("Costo total: {}".format(costo)) 
def procesar_viaje_optimo(grafo, origen):
	lista_recorrido,costo= biblioteca.viajante(grafo, origen)
	lista_aux=lista_recorrido[:-1]
	if len(lista_recorrido)>1:
		for vertice in lista_aux:
			print(vertice, end = " -> ")
	print(lista_recorrido[-1])
	print("Costo total: {}".format(costo))

def procesar_viaje_aproximado(grafo, origen):
	lista_recorrido,costo = biblioteca.viajante_aproximado(grafo, origen)
	lista_aux=lista_recorrido[:-1]
	if len(lista_recorrido)>1:
		for vertice in lista_aux:
			print(vertice, end = " -> ")
	print(lista_recorrido[-1])
	print("Costo total: {}".format(costo))

def procesar_itinerario(grafo, recomandaciones): #recomendaciones es el nombre de un archivo .csv

	return None

def procesar_reducir_caminos(grafo, destino): #destino es el nombre de un archivo .csv

	return None

def comparar_comando(grafo, linea_comando):

	largo = len(linea_comando)

	if largo == 3:
		if linea_comando[0] == "ir":
			procesar_ir(grafo, linea_comando[1], linea_comando[2])
			return True
		if linea_comando[0] == "viaje":
			if linea_comando[1] == "optimo":
				procesar_viaje_optimo(grafo, linea_comando[2])
				return True
			if linea_comando[1] == "aproximado":
				procesar_viaje_aproximado(grafo, linea_comando[2])
				return True
	if largo == 2:
		if linea_comando[0] == "itinerario":
			procesar_itinerario(grafo, linea_comando[1])
			return True
		if linea_comando[0] == "reducir_caminos":
			procesar_reducir_caminos(grafo, linea_comando[1])
			return True

	return False

def cargar_set_datos(nombre_archivo_ciudades):
	"""El archivo debe contener sus encabezados correspondiente"""
	grafo = Grafo(False)
	coordenadas = {}
	estoy_en = ""
	with open(nombre_archivo_ciudades, "r") as archivo_csv:
		for linea in archivo_csv:
			lista_campos=linea.rstrip("\n").split(",")
			if lista_campos[0] == CUIDAD:
				estoy_en = CUIDAD
				continue
			if lista_campos[0] == RUTA:
				estoy_en = RUTA
				continue
			if estoy_en == CUIDAD and len(lista_campos) == 3:
				grafo.agregar_vertice(lista_campos[0])
				coordenadas[lista_campos[0]]=(lista_campos[1],lista_campos[2])
			if estoy_en == RUTA and len(lista_campos) == 3:
				costo=int(lista_campos[2])
				grafo.agregar_arista(lista_campos[0],lista_campos[1],costo)
	return grafo,coordenadas
"""
	archivo_ciudades = open(nombre_archivo_ciudades, "r")

	linea_actual = archivo_ciudades.read() #El archivo sedes.csv tiene un "11" al principio y un "55" en el medio
#NO LEE CORRECTAMENTE, DEBERIA LEER LINEA POR LINEA
	while linea_actual != "55":
		linea_actual = archivo_ciudades.read()
		linea_ciudad = linea_actual.split(",")
		grafo.agregar_vertice(linea_ciudad[0])
		coordenadas[linea_ciudad[0]] = linea_ciudad

	while linea_actual != "":
		linea_actual = archivo_ciudades.read()
		linea_ciudad = linea_actual.split(",")
		grafo.agregar_arista(linea_ciudad[0], linea_ciudad[1], linea_ciudad[2])

	archivo_ciudades.close()

	return grafo, coordenadas
"""
def main():

	if len(sys.argv) != 3:
		print("Cantidad de parametros invalida")
		return False

	grafo , coordenadas = cargar_set_datos(sys.argv[1])

	while True:
		linea_actual = input()
		if linea_actual == "":
			return False

		linea_comando = linea_actual.split(" ")
		if not comparar_comando(grafo, linea_comando):
			print("Parametro incorrecto")
			return False

main()