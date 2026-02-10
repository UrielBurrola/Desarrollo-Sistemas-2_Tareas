from  ClienteDeudor import ClienteDeudor

class PrestamoAuto(ClienteDeudor):

    def __init__(self, no_cliente, nombre, no_cuenta, prestamo, plazo_inversion):
        super().__init__(no_cliente, nombre, no_cuenta, prestamo, plazo_inversion)
        self.interes_a_pagar = self.calcular_interes()
        self.tipo = "Automotriz"

    def calcular_interes(self):
        return self.__prestamo * ((self.__plazo_inversion * 12)* 0.15)