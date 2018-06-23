class _Nodo:

    """Representa un nodo"""
    
    def __init__ (self, dato, prox= None):

        """Crea un nodo, con el dato y, si se
        desea, con el nodo siguiente"""
        
        self.dato = dato
        
        self.prox = prox
        
class Cola:

    """Representa la clase cola, con metodos para
    encolar, desencolar, esta_vacia y cambiar_prmero"""
    
    def __init__(self):

        """Crea una cola vacia"""
        
        self.prim = None
        
        self.ultimo = None
        
    def encolar (self, dato):

        """Encola un elemento"""
        
        nodo = _Nodo(dato)
        
        if not self.prim:
            
            self.prim = nodo
            
        else:
            
            self.ultimo.prox = nodo
            
        self.ultimo = nodo
        
    def desencolar (self):

        """Desencola el primer elemento.
        Si esta vacia levanta ValueError"""

        if self.esta_vacia():

            raise ValueError()
        
        nodo = self.prim
        
        dato = nodo.dato
        
        self.prim = nodo.prox
        
        return dato
    
    def esta_vacia (self):

        """ Devuelve True si la cola esta vacia.
        False si no."""
        
        return self.prim is None
    
    def ver_primero(self):

        """Devuelve el primer dato de la cola.
        Si esta vacia levanta ValueError. """
        
        if not self.prim:
            
            raise ValueError()
        
        return self.prim.dato
    
    def cambiar_primero(self,valor):

        """Permite cambiar el primer elemento de
        la cola sin afectar el orden.
        levanta ValueError si esta vacia"""

        if self.esta_vacia():

            raise ValueError()
        
        self.prim.dato = valor

    def imprimir_cola(self):

        """Imprime todo el contenido de la cola"""
        
        resultado=[]#Esto es porque el profesor al mostrar modo debug la cola lo imprimia en una lista , por ende asumimos que imprimo una lista .
        actual=self.prim
        while not actual is None:
            
            resultado.append(actual.dato)
            
            actual=actual.prox
        
        print(resultado)

