#Definimos la clase nodo para crear nodos y otras opciones
class Nodo:
    #Metodo constructor
    def __init__(self, valor):
        self.dato=valor
        self.next=None
    #Metodo que obtiene el valor del dato del nodo.
    def obtenerDato(self):
        return self.dato
    #Metodo para obtener el apuntador de la referencia nodo.
    def obtenerSiguiente(self):
        return self.next
    #Metodo par asignar nuevo valor al dato del nodo.
    def setDato(self,val):
        self.dato=val
    #Metodo para asignar una nueva referencia (nuevo apuntador) del siguiente nodo
    def setSiguiente(self, valr):
        self.next=valr