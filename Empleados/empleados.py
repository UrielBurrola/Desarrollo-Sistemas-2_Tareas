from Vendedor import Vendedor
from Empleado import Empleado
from Secretario import Secretario

class empleados():

    def __init__(self):
        self.lista_empleados = []

    def default(self):
        self.lista_empleados.append(Vendedor(
            "Uri",
            "fig",
            "abc1234",
            "cosa 123",
            3,
            6621234,
            100.00,
            1,
            15
        ))

    def datos_empleado(self):
        datos = [
            input("Introduce el nombre: "),
            input("Introduce el apellido: "),
            input("Introduce el RFC: "),
            input("Introduce la direccion: "),
            int(input("Introduce los años de antiguedad: ")),
            int(input("Introduce el telefono: ")),
            float(input("Introduce el salario: "))
        ]
        return datos

    #nombre, apellidos, RFC, direccion, años, telefono, salario,area_venta,comision
    def agg_vendedor(self):
        datos = self.datos_empleado()
        datos.append(int(input("Introduce el numero del area de venta del vendedor: ")))
        datos.append(int(input("Introduce el porcentaje de comision(%): ")))
        self.lista_empleados.append(Vendedor(*datos))

    #nombre, apellidos, RFC, direccion, años, telefono, salario, numDespacho, numFax
    def agg_secretario(self):
        datos = self.datos_empleado()
        datos.append(int(input("Introduce el numero de despacho: ")))
        datos.append(int(input("Introduce el numero de fax: ")))
        self.lista_empleados.append(Secretario(*datos))

    def mostrar_empleados(self):
        if len(self.lista_empleados)>0:
            for n, e in enumerate(self.lista_empleados):
                print(f"{n+1}) {e.nombre} {e.apellido} [{e.puesto}] -- Salario: {e.salario}$")

    def impresion_empleado(self, index):
        self.lista_empleados[index].imprimir()

    def aumento(self, index):
        self.lista_empleados[index].aumento_salario()
