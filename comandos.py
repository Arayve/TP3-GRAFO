from grafo import Grafo
import sys

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

def cargar_set_datos(nombre_archivos):

	#PROCESO ARCHIVOS Y DEVUELVO EL GRAFO

	return None

def main():
	if len(sys.argv) < 2:
		print("Cantidad de parametros invalida")
		return False

	nombre_archivos = sys.argv

	grafo = cargar_set_datos(nombre_archivos)

	while True:
		linea_actual = input()
		if linea_actual == "":
			return False

		linea_comando = linea_actual.split(" ")
		if not comparar_comando(grafo, linea_comando):
			print("Parametro incorrecto")
			return False

main()