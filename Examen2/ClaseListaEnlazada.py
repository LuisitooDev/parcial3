#definimos la calse para el manejo de las listas enlazadas
from clasenodo import Nodo

class ListaEnlazada:
    #metodo contructor
    def __init__(self):
        self.cabeza=None
    #metodo para determinar si la lista esta vacia
    def isEmpty(self):
        return self.cabeza is None
    #metodo para agregar nodos al inicio de la lista enlazada
    def add(self,item):
        new_nodo=Nodo(item)
        new_nodo.setSiguiente(self.cabeza)
        self.cabeza=new_nodo
    #metodo para imprimir la lista enlazada
    def printList(self):
        actual=self.cabeza
        while actual is not None:
            print(actual.obtenerDato(),end=" -> ")
            actual=actual.obtenerSiguiente()

    #metodo para determinar el tamano de la lista
    def size(self):
        contador=0
        actual=self.cabeza
        while actual is not None:
            contador+=1
            actual=actual.obtenerSiguiente()
        return contador
    
    #metodo para buscar un valor dentro de la lista
    def search(self,item):
        actual=self.cabeza
        found=False
        while actual is not None and not found:
            if actual.obtenerDato() is item:
                found=True
            else:
                actual=actual.obtenerSiguiente()
        return found
    #metodo para remover nodos de la lista enlazada
    def remover(self,item):
        actual=self.cabeza
        anterior=None
        found=False
        while actual is not None and not found:
            if actual.obtenerDato() is item:
                found=True
            else:
                anterior=actual
                actual=actual.obtenerSiguiente()
        if found:
            if anterior is None:
                self.cabeza=actual.obtenerSiguiente()
            else:
                anterior.setSiguiente(actual.obtenerSiguiente())
        else:
            print("Error! El valor no fue encontrado!")
            raise ValueError
    #metodo para insertar un nuevo nodo segun la posicion
    def insertar(self,posicion,item):
        if posicion >self.size()-1:
            print("Error! fuera de rango")
            raise IndexError
        actual=self.cabeza
        anterior=None
        pos=0
        if pos is 0:
            self.add(item)
        else:
            new_nodo=Nodo(item)
            while pos<posicion:
                pos+=1
                anterior=actual
                actual=actual.obtenerSiguiente()
            anterior.setSiguiente(new_nodo)
            new_nodo.setSiguiente(actual)
    #metodo para retornar la posicion de un elemento dentro de una lista
    def index(self,item):
        actual=self.cabeza
        pos= 0
        found=False
        while actual is not None and not found:
            if actual.obtenerDato() is item:
                found=True
            else:
                actual=actual.obtenerSiguiente()
                pos+=1
        if found:
            pass #deja seguir corriendo la funcion
        else:
            pos=None
        return pos
    #metodo para borrar un elemento segun su posicion
    def pop(self,posicion=None):
        item=0
        if posicion>self.size():
            print("Error! Posicion fuera de rango!")
            raise IndexError #lanza errores
        actual=self.cabeza
        if posicion is None:
            item=actual.obtenerDato()
            self.cabeza=actual.obtenerSiguiente()
        else:
            pos=0
            anterior=None
            while pos<posicion:
                anterior=actual
                actual=actual.obtenerSiguiente()
                pos+=1
                item=actual.obtenerDato()
            anterior.setSiguiente(actual.obtenerSiguiente())
            print(item)
            return item
    #metodo para agregar al final de la lista metodo append
    def append(self,item):
        actual=self.cabeza
        anterior=None
        pos=0
        tamano=self.size()
        while pos<tamano:
            anterior=actual
            actual=actual.obtenerSiguiente()
            pos+=1
        new_nodo=Nodo(item)
        if anterior is None:
            new_nodo.setSiguiente(actual)
            self.cabeza=new_nodo
        else:
            anterior.setSiguiente(new_nodo)
    #metodo de ordenamiento de la lista enlazada
    def ordenarLista(self):
        actual=self.cabeza
        anterior=None
        tamano=self.size()
        for i in range(tamano):
            for j in range(tamano):
                aux1=actual.obtenerDato()
                anterior=actual
                actual=actual.obtenerSiguiente()
                aux2=actual.obtenerDato()
                if aux1>aux2:
                    actual.setDato(aux1)
                    anterior.setDato(aux2)
                if actual.obtenerSiguiente() is None:
                    break
            actual=self.cabeza
    #metodo para determinar el valor maximo en la lista ordenada
    def maximo(self):
        max=0
        actual=self.cabeza
        while actual is not None:
            dato=actual.obtenerDato()
            if dato>max:
                max=dato
            actual=actual.obtenerSiguiente()
        return max
    #metodo para ver el minimo
    def minimo(self):
        min=1000000000000000000000000000000000
        actual=self.cabeza
        while actual is not None:
            dato=actual.obtenerDato()
            if dato<min:
                min=dato
            actual=actual.obtenerSiguiente()
        return min
    #metodo para hacer la sumatoriade todos los elementos de la lista anlazada
    def sumatoria(self):
        suma=0
        actual=self.cabeza
        while actual is not None:
            dato=actual.obtenerDato()
            suma=suma+dato
            actual=actual.obtenerSiguiente()
        return suma
    #Metodo para obtener datos
    def obtenerDatos(self):
        actual=self.cabeza
        lista=[]
        tamano=self.size()
        for i in range(tamano):
            dato =  actual.obtenerDato()
            lista.append(dato)
            actual=actual.obtenerSiguiente()
        return lista