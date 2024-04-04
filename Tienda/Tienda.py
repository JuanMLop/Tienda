from typing import Any
from Producto import Producto
class Tienda:
    """---------------------------------------------------------------------------
    #Atributos
    None significa nada vacio
    ---------------------------------------------------------------------------"""


    #__producto1 = None
    #__producto2 = None
    #__producto3 = None
    #__producto4 = None
 
    """---------------------------------------------------------------------------
    #Metodos
    ---------------------------------------------------------------------------"""
    
    def __init__(self, ):
        self.dineroEnCaja= 0
        self.__producto1= Producto("Papeleria", "Lapiz", 550.0, 18, 5)
        self.__producto2= Producto("Papeleria", "Borrador", 300.0, 15, 5)
        self.__producto3= Producto("Supermercado", "Cafe", 5600.0, 20, 10)
        self.__producto4= Producto("Drogueria", "Desinfectante", 3200.0, 12, 11)
    
    def getProducto1(self):
        return self.__producto1
    def getProducto2(self):
        return self.__producto2
    def getProducto3(self):
        return self.__producto3
    def getProducto4(self):
        return self.__producto4
        
