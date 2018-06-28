from grafo import Grafo
import biblioteca
import sys
import csv

CUIDAD="11"
RUTA="55"
def escribir_encabezado(nombre_funcion,desde,hasta,archivo):
	archivo.write('<?xml version="1.0" encoding="UTF-8"?>\n')
	archivo.write('kml xmlns="http://earth.google.com/kml/2.1">\n')
	archivo.write('\t<Document>\n')
	archivo.write('\t\t<name>{} {}, {}</name>\n'.format(nombre_funcion,desde,hasta))
def escribir_vertice_kml(vertice,lat,log,archivo):
	archivo.write("\t\t<Placemark>\n")
	archivo.write("\t\t\t<name>{}</name>\n".format(vertice))
	archivo.write("\t\t\t<Point>\n")
	archivo.write("\t\t\t\t<coordinates>{}, {}</coordinates>\n".format(lat,log))
	archivo.write("\t\t\t</Point>\n")
	archivo.write("\t\t</Placemark>\n")
def escribir_artista(archivo,lat1,log1,lat2,log2):
	archivo.write("\t\t<Placemark>\n")
	archivo.write("\t\t\t<LineString>\n")
	archivo.write("\t\t\t\t<coordinates>{}, {} {}, {}</coordinates>\n".format(lat1,log1,lat2,log2))
	archivo.write("\t\t\t<LineString>\n")
	archivo.write("\t\t</Placemark>\n")
def escribir_final(archivo):
	archivo.write('\t<Document>\n')
	archivo.write('</kml>')
def procesar_ir(grafo, desde, hasta,coordenadas,kml):
	lista_camino,costo= biblioteca.camino_minimo(grafo, desde, hasta)
	lista_aux=lista_camino[:-1]
	if len(lista_camino)>1:
		for vertice in lista_aux:
			print(vertice, end = " -> ")
	print(lista_camino[-1])
	print("Costo total: {}".format(costo))
	with open(kml,"w") as archivo:
		escribir_encabezado("ir",desde,hasta,archivo)
		for vertice in lista_camino:
			tupla_coorde=coordenadas[vertice]
			escribir_vertice_kml(vertice,tupla_coorde[0],tupla_coorde[1],archivo)
		for i in range(len(lista_camino)-1):
			tupla_coorde1=coordenadas[lista_camino[i]]
			tupla_coorde2=coordenadas[lista_camino[i+1]]
			escribir_artista(archivo,tupla_coorde1[0],tupla_coorde1[1],tupla_coorde2[0],tupla_coorde2[1])
		escribir_final(archivo)
def procesar_viaje_optimo(grafo, origen,kml):
	lista_recorrido,costo= biblioteca.viajante(grafo, origen)
	lista_aux=lista_recorrido[:-1]
	if len(lista_recorrido)>1:
		for vertice in lista_aux:
			print(vertice, end = " -> ")
	print(lista_recorrido[-1])
	print("Costo total: {}".format(costo))

def procesar_viaje_aproximado(grafo, origen, kml):
	lista_recorrido,costo = biblioteca.viajante_aproximado(grafo, origen)
	lista_aux=lista_recorrido[:-1]
	if len(lista_recorrido)>1:
		for vertice in lista_aux:
			print(vertice, end = " -> ")
	print(lista_recorrido[-1])
	print("Costo total: {}".format(costo))

def procesar_itinerario(grafo, recomendaciones,kml): #recomendaciones es el nombre de un archivo .csv FIJATE QUE CREO QUE GRAfO NO HACE FALTA
	grafo_recomendaciones=Grafo(True)
	with open(recomendaciones,"r") as archivo_csv:
		for linea in archivo_csv:
			lista_campos=linea.rstrip("\n").split(",")
			for cuidad in lista_campos:
				grafo_recomendaciones.agregar_vertice(cuidad)#no importa si hay repetido , no los vuelve a copiar
	with open(recomendaciones,"r") as archivo_csv:
		for linea in archivo_csv:
			lista_campos=linea.rstrip("\n").split(",")
			grafo_recomendaciones.agregar_arista(lista_campos[0],lista_campos[1],0)
	lista_orden_topologico=biblioteca.orden_topologico(grafo_recomendaciones)
	lista_aux=lista_orden_topologico[:-1]
	if len(lista_orden_topologico)>1:
		for vertice in lista_aux:
			print(vertice, end = " -> ")
	print(lista_orden_topologico[-1])
def procesar_reducir_caminos(grafo, destino): #destino es el nombre de un archivo .csv
	grafo_tendido,costo=biblioteca.arbol_tendido_minimo(grafo)
	lista_recorrido=biblioteca.recorrer_grafo(grafo_tendido)
	with open(destino,"w") as archivo:
		archivo_csv=csv.writer(archivo)
		archivo_csv.writerows(lista_recorrido)
	print("Peso total: {}".format(costo))
def comparar_comando(grafo, linea_comando,kml,coordenadas):

	largo = len(linea_comando)

	if largo == 3:
		if linea_comando[0] == "ir":
			procesar_ir(grafo, linea_comando[1], linea_comando[2],coordenadas,kml)
			return True
		if linea_comando[0] == "viaje":
			if linea_comando[1] == "optimo":
				procesar_viaje_optimo(grafo, linea_comando[2],kml)
				return True
			if linea_comando[1] == "aproximado":
				procesar_viaje_aproximado(grafo, linea_comando[2],kml)
				return True
	if largo == 2:
		if linea_comando[0] == "itinerario":
			procesar_itinerario(grafo, linea_comando[1],kml)
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
		if not comparar_comando(grafo, linea_comando, sys.argv[2],coordenadas):
			print("Parametro incorrecto")
			return False

main()