NOMBRE = TP3
PYFILES = biblioteca.py cola.py grafo.py traemelaco.py
zipear:
	zip $(NOMBRE).zip $(PYFILES)
run:
	cat comandos.txt | python3 traemelaco.py sedes.csv mapa.kml

