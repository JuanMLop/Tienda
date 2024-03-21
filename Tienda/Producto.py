from enum import  Enum

class Tipo(Enum):
    Papeleria = 1
    Supermercado = 2
    Farmacia = 3
class Producto:
    
    
    __subsidio= False
    __calidad= 'A'
    
    """---------------------------------------------------------------------------
    #Constantes
    Tipo double
    flotantes
    ---------------------------------------------------------------------------"""
    
    __IVA_PAPELERIA= 0.16
    __IVA_FARMACIA= 0.12
    __IVA_SUPERMERCADO= 0.4
    
    """---------------------------------------------------------------------------
    #E-num se crea dento de la misma clase
    ---------------------------------------------------------------------------"""
    
    """---------------------------------------------------------------------------
    #Atributos variable escrita en mayusculas no se toca
    ---------------------------------------------------------------------------"""
    
    __nombre=None
    __tipo = Enum ('Tipo',['PAPELERIA', 'SUPERMERCADO', 'FARMACIA'])
    __valorUnitario = 0.0
    __cantidadBodega= 0
    __cantidadMinima= 0
    __cantidadUnidadesVendidas= 0
    
    """---------------------------------------------------------------------------
    #Metodos
    ---------------------------------------------------------------------------"""
    def getNombre(self):
        return  self.__nombre
    
    def getTipo(self):
        return self.__tipo
    
    def getValorUnitario(self):
        return self.__valorUnitario
    
    def getCantidadBodega(self):
        return self.__cantidadBodega
    
    def getCantidadMinima(self):
        return self.__cantidadMinima
    
    def getCantidadUnidadesVendidas(self):
        return self.__cantidadUnidadesVendidas
    
    
    
    
    
    
    
    
    

    


        
        
