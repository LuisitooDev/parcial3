import random as ran
from ClaseListaEnlazada import ListaEnlazada

class numeros:
    def __init__(self):
        self.mi_lista=ListaEnlazada()
        self.lista_impares= []
        self.mis_multiplos=ListaEnlazada()
    
    def generarNumeros(self):
        for i in range(50):
            self.mi_lista.append(ran.randint(1,100))
    def mostrarLista(self):
        self.mi_lista.printList()
    def obtenerImpares(self):
        lista=self.mi_lista.obtenerDatos()
        for j in range(len(lista)):
            if lista[j]%2!=0:
                self.lista_impares.append(lista[j])
        print(self.lista_impares)
        print("\n")
        print(len(self.lista_impares))
    def multiplos3(self):
        lista=self.mi_lista.obtenerDatos()
        for i in range(len(lista)):
            if lista[i]%3==0:
                self.mis_multiplos.append(lista[i])
        self.mis_multiplos.printList()
        print("\n")
    def ordenarnumeros(self):
        self.mi_lista.ordenarLista()
        self.mi_lista.printList()
        print("\n")
        print("El valor maximo es: ",self.mi_lista.maximo())
        print("El valor maximo es: ",self.mi_lista.minimo())
    def promedios(self):
        suma=self.mis_multiplos.sumatoria()
        tamano=self.mis_multiplos.size()
        promedio=suma/tamano
        print(promedio)
    