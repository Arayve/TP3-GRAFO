from grafo import Grafo
import sys
import csv
ENCABEZADO_CUIDADES="11"
ENCABEZADO_RUTA="55"

def procesar_ir(grafo, desde, hasta):

	return None

#	lista_camino = camino_minimo(grafo, desde, hasta)

#	for vertice in lista_camino:
#		print(str(vertice), end = " -> ")

	#FALTA EL COSTO TOTAL

def procesar_viaje_optimo(grafo, origen):

	return None

#	lista_recorrido = viajante(grafo, origen)

#	for vertice in lista_recorrido:
#		print(str(vertice), end = " -> ")

	#FALTA EL COSTO TOTAL

def procesar_viaje_aproximado(grafo, origen):

	return None

#	lista_recorrido = viajante_aproximado(grafo, origen)

#	for vertice in lista_recorrido:
#		print(str(vertice), end = " -> ")

	#FALTA EL COSTO TOTAL

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
	with open(nombre_archivo_ciudades, "r") as archivo:
		archivo_cuidades_csv = csv.reader(archivo)
		for nombre_cuidad, lat, log in archivo_cuidades_csv:
			if nombre_cuidad = ENCABEZADO_CUIDADES:
				continue
				centinela = ESTOY_EN_CUIDADES
			if nombre_cuidad = ENCABEZADO_RUTA:
				break
			grafo.agregar_vertice(nombre_cuidad)
			coordenadas[nombre_cuidad]=(lat,log)
		for cuidad_partida , cuidad_llegada , costo in archivo_cuidades_csv:
			grafo.agregar_arista(cuidad_partida,cuidad_llegada,costo)
	return grafo , coordenadas


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

	grafo, coordenadas = cargar_set_datos(sys.argv[1])

	while True:
		linea_actual = input()
		if linea_actual == "":
			return False

		linea_comando = linea_actual.split(" ")
		if not comparar_comando(grafo, linea_comando, sys.argv[2]):
			print("Parametro incorrecto")
			return False

main()