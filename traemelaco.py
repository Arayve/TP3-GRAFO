from grafo import Grafo
import biblioteca
import sys
import csv

CUIDAD = "cuidad"
RUTA = "ruta"
PRIMER_COMANDO = "ir"
SEGUNDO_COMANDO = "viaje optimo"
TERCER_COMANDO = "viaje aproximado"
CUARTO_COMANDO = "itinerario"
QUINTO_COMANDO = "reducir_caminos"
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
def escrbir_kml(kml,desde,hasta,coordenadas,nombre_funcion,lista_camino):
	with open(kml,"w") as archivo:
		escribir_encabezado(nombre_funcion,desde,hasta,archivo)
		for vertice in lista_camino:
			tupla_coorde=coordenadas[vertice]
			escribir_vertice_kml(vertice,tupla_coorde[0],tupla_coorde[1],archivo)
		for i in range(len(lista_camino)-1):
			tupla_coorde1=coordenadas[lista_camino[i]]
			tupla_coorde2=coordenadas[lista_camino[i+1]]
			escribir_artista(archivo,tupla_coorde1[0],tupla_coorde1[1],tupla_coorde2[0],tupla_coorde2[1])
		escribir_final(archivo)
def _imprimir_camino(lista_camino):
	lista_aux=lista_camino[:-1]
	if len(lista_camino)>1:
		for vertice in lista_aux:
			print(vertice, end = " -> ")
	print(lista_camino[-1])
def procesar_ir(grafo, desde, hasta,coordenadas,kml):
	lista_camino,costo= biblioteca.camino_minimo(grafo, desde, hasta)
	_imprimir_camino(lista_camino)
	print("Costo total: {}".format(costo))
	escrbir_kml(kml,desde,hasta,coordenadas,PRIMER_COMANDO,lista_camino)
def procesar_viaje_optimo(grafo,origen,coordenadas,kml):
	lista_camino,costo= biblioteca.viajante(grafo, origen)
	_imprimir_camino(lista_camino)
	print("Costo total: {}".format(costo))
	escrbir_kml(kml,origen,"",coordenadas,SEGUNDO_COMANDO,lista_camino)
def procesar_viaje_aproximado(grafo, origen,coordenadas,kml):
	lista_camino,costo = biblioteca.viajante_aproximado(grafo, origen)
	_imprimir_camino(lista_camino)
	print("Costo total: {}".format(costo))
	escrbir_kml(kml,origen,"",coordenadas,TERCER_COMANDO,lista_camino)
def procesar_itinerario(recomendaciones,coordenadas,kml): #recomendaciones es el nombre de un archivo .csv 
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
	_imprimir_camino(lista_orden_topologico)
	escrbir_kml(kml,"recomendaciones.csv","",coordenadas,CUARTO_COMANDO,lista_orden_topologico)
def procesar_reducir_caminos(grafo, destino,coordenadas): #destino es el nombre de un archivo .csv
	tendido_minimo,costo=biblioteca.arbol_tendido_minimo(grafo)
	lista_recorrido=biblioteca.recorrer_grafo(tendido_minimo)
	cant_arista=len(lista_recorrido)
	with open(destino,"w") as archivo:
		archivo.write("{}\n".format(tendido_minimo.cantidad_vertice()))
		for clave,valor in coordenadas.items():
			archivo.write("{},{},{}\n".format(clave,valor[0],valor[1]))
		archivo.write("{}\n".format(cant_arista))
		archivo_csv=csv.writer(archivo)
		archivo_csv.writerows(lista_recorrido)
	print("Peso total: {}".format(costo))
def comparar_comando(grafo, linea_comando,kml,coordenadas):

	largo = len(linea_comando)

	if largo == 3:
		if linea_comando[0] == PRIMER_COMANDO:
			procesar_ir(grafo, linea_comando[1], linea_comando[2],coordenadas,kml)
			return True
	if largo == 2:
		if linea_comando[0] == SEGUNDO_COMANDO:
			procesar_viaje_optimo(grafo, linea_comando[1],coordenadas,kml)
			return True
		if linea_comando[0] == TERCER_COMANDO:
			procesar_viaje_aproximado(grafo, linea_comando[1],coordenadas,kml)
			return True
		if linea_comando[0] == CUARTO_COMANDO :
			procesar_itinerario(linea_comando[1],coordenadas,kml)
			return True
		if linea_comando[0] == QUINTO_COMANDO:
			procesar_reducir_caminos(grafo, linea_comando[1],coordenadas)
			return True
	return False
def _invertir_centinela(estoy_en):
	if estoy_en == "":
		return CUIDAD
	return RUTA
def cargar_set_datos(nombre_archivo_ciudades):
	"""El archivo debe contener sus encabezados correspondiente, los cuales son las cantidad de vertice y arista"""
	grafo = Grafo(False)
	coordenadas = {}
	estoy_en = ""
	with open(nombre_archivo_ciudades, "r") as archivo_csv:
		for linea in archivo_csv:
			lista_campos=linea.rstrip("\n").split(",")
			if len(lista_campos) == 1:
				estoy_en =_invertir_centinela(estoy_en)
				continue
			if estoy_en == CUIDAD and len(lista_campos) == 3:
				grafo.agregar_vertice(lista_campos[0])
				coordenadas[lista_campos[0]]=(lista_campos[1],lista_campos[2])
			if estoy_en == RUTA and len(lista_campos) == 3:
				costo=int(lista_campos[2])
				grafo.agregar_arista(lista_campos[0],lista_campos[1],costo)
	return grafo,coordenadas
def separar_comando(linea_actual):
	
	if linea_actual[:2] == "ir":
		linea_actual=linea_actual[:2]+","+linea_actual[3:]
		linea_comando = linea_actual.rstrip("\n").split(",")
		linea_comando[2]=linea_comando[2][1:]
		return linea_comando
	if linea_actual[:5] == "viaje":
		linea_comando = linea_actual.rstrip("\n").split(",")
		linea_comando[1]=linea_comando[1][1:]
		return linea_comando
	
	linea_comando = linea_actual.rstrip("\n").split(" ")
	return linea_comando

def main():
	if len(sys.argv) != 3:
		print("Cantidad de parametros invalida")
		return False

	grafo, coordenadas = cargar_set_datos(sys.argv[1])
	
	for linea_actual in sys.stdin:
		linea_comando = separar_comando(linea_actual)
		if not comparar_comando(grafo, linea_comando, sys.argv[2],coordenadas):
			print("Parametro incorrecto")
			return False
main()
