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
    
    def __init__(self, tipo , pNombre , pValorUnitario , pCantidadBodega , pCantidadMinima):
        self.__tipo=tipo
        self.__nombre=pNombre
        self.__valorUnitario=pValorUnitario
        self.__cantidadBodega=pCantidadBodega
        self.__cantidadMinima=pCantidadMinima
        self.__cantidadUnidadesVendidas= 0
        
    
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
    
    
    def setNombre(self,  nombre):
        self.__nombre=nombre
        
    def setTipo(self, tipo):
        self.__tipo=tipo
        
    def setValorUnitario(self, valorUnitario):
        self.__valorUnitario=valorUnitario
        
    def setCantidadBodega(self, cantidadBodega):
        self.__cantidadBodega=cantidadBodega
        
    def setCantidadMinima(self, cantidaMinima):
        self.__cantidadMinima=cantidaMinima
        
    def setCantidadUnidadesVeendidas(self, unidadesVendidas):
        self.__cantidadUnidadesVendidas=unidadesVendidas
        
    def Vender (self, cantidad):
        if cantidad <= self.__cantidadBodega:
            self.__cantidadUnidadesVendidas+=cantidad
            self.__cantidadBodega-=cantidad
        else:
            print("No hay suficiente cantida en bodega")
            
    def exiteSuficiente(self, cantidad):
        if cantidad <= self.__cantidadBodega:
            return True
        else:
            return False  
        
    def darIva(self):
        if(self.__tipo == "PAPELERIA"):
            return self.__IVA_PAPELERIA
        elif(self.__tipo== "SUPERMERCADO"):
            return self.__IVA_SUPERMERCADO
        elif(self.__tipo== "FARMACIA"):
            return self.__IVA_FARMACIA
        else:
            print("La categoria no exite")
            
            
    def subirValorUnitario(self):
        if(self.__valorUnitario < 1000):
            return self.__valorUnitario * 0.01  
        elif(self.__valorUnitario <=1000 and self.__valorUnitario<=5000):
            return self.__valorUnitario *  0.02
        elif(self.__valorUnitario  > 5000):
            return self.__valorUnitario * 0.03
     # AUMENTAR EL VALOR UNITARIO DEL PRODUCTO :SI EL PRODUCTO CUESTA MENOS DE MIL AUMENTAR EL 1% SI CUESTA ENTRE 1000 Y 5000 AUMENTAR EL 2% SI CUESTA MAS DE 5000 AUMENTAR EL 3%  EL METODO SE LLAMA SUBIR VALOR UNITARIO
     
     # RECIBIR UN PEDIDO SOLO SI EN LA BODEGA SE TIENE MENOS UNIDADES DE LAS INDICADAS EN EL TOPE MINIMO EN CASO CONTRARIO EL METODO NO DEBE HACER NADA EL METODO SE LLAMA HACER PEDIDO Y TIENE UN PARAMETRO
     
    def hacerPedio(self, pCantidad):
        if(self.__cantidadBodega<self.__cantidadMinima):
            self.__cantidadBodega += pCantidad
        else:
            print("No relaizar pedido")
            
    
    def cambiarValorUnitario(self):
        if(self.__tipo== "PAPELERIA"):
            reducir = self.__valorUnitario * 0.10
            self.__valorUnitario - reducir
        
        elif(self.__tipo== "DROGUERIA"):
                reducir= self.__valorUnitario * 0.10
                self.__valorUnitario - reducir
                
        elif(self.__tipo== "SUPERMERCADO"):
            aumentar = self.__valorUnitario * 0.05
            self.__valorUnitario + aumentar
        
        else:
            print("Este producto no tiene descuento por tipo de tienda.")


        
        
