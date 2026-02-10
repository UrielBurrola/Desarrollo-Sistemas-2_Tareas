from abc import ABC, abstractmethod

class ClienteDeudor(ABC):

    def __init__(self, no_cliente, nombre, no_cuenta, prestamo, plazo_inversion):
        self.__no_cliente = no_cliente
        self.__nombre = nombre
        self.__no_cuenta = no_cuenta
        self.prestamo = prestamo
        self.plazo_inversion = plazo_inversion
        self.tipo = None

        self.interes_a_pagar = 0
        

    @abstractmethod
    def calcular_interes(self):
        pass

    def mostrar_informacion(self):
        return """
        -------------------------------------------------------------
        Cliente: {} - - - No. Cuenta: {}  
        Prestamo: {} - - Plazo de Inversion: {} - - Interes a Pagar: {}
        Total a Pagar: {}
        -------------------------------------------------------------
        """.format(self.__nombre, self.__no_cuenta, self.prestamo, self.plazo_inversion, self.interes_a_pagar, self.prestamo + self.interes_a_pagar)
    
    def __str__(self):
        return f" {self.__no_cliente} .- Cliente: {self.__nombre} [{self.tipo}]"