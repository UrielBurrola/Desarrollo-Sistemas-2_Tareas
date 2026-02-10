from ClienteDeudor import ClienteDeudor

class PrestamoPersonal(ClienteDeudor):
    def __init__(self, no_cliente, nombre, no_cuenta, prestamo, plazo_inversion):
        super().__init__(no_cliente, nombre, no_cuenta, prestamo, plazo_inversion)
        self.interes_a_pagar = self.calcular_interes()
        self.tipo = "Personal"

    def calcular_interes(self):
        return self.prestamo * self.plazo_inversion * 0.05