from Empleado import Empleado

##Tiene despacho, número de fax e incrementa su salario un 5% anual

class Secretario(Empleado):

    puesto = "Secretario"

    def __init__(self, nombre, apellidos, RFC, direccion, años, telefono, salario, numDespacho, numFax):
        super().__init__(nombre, apellidos, RFC, direccion, años, telefono, salario)
        self.numDespacho = numDespacho
        self.numFax = numFax
        self.aumento = 0.05

    def imprimir(self):
        info = super().imprimir()
        info += f"""
-----------------------------------------------------------------
Numero de Despacho: {self.numDespacho}  Numero de Fax: {self.numFax}
-----------------------------------------------------------------
"""
        print(info)