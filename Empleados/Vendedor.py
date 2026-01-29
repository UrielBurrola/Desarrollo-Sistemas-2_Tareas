from Empleado import Empleado

# Tiene coche de la empresa (identificado por la matricula, marca y modelo), teléfono móvil, área de venta,
# lista de clientes y porcentaje que se lleva de las ventas en concepto de comisiones.
# Incrementa su salario un 10% anual. Tendrá, al menos, las siguientes funciones miembro:
#Constructores (debe rellenar la información personal y los datos principales)
# Imprimir (debe imprimir sus datos personales y su puesto en la empresa).
#Dar de alta un nuevo cliente.
#Dar de baja un cliente.
# Cambiar de coche.

class Vendedor(Empleado):

    puesto = "Vendedor"

    def __init__(self, nombre, apellidos, RFC, direccion, años, telefono, salario,area_venta,comision):
        super().__init__(nombre, apellidos, RFC, direccion, años, telefono, salario)
        self.area_venta = area_venta
        self.comision = comision
        self.aumento = 0.1
        self.lista_clientes = []

    def mostrar_clientes(self):
        if self.lista_clientes.__len__() == 0:
            print("Lista de Clientes vacia. ")
        else:
            for n,c in enumerate(self.lista_clientes):
                print(f"{n+1} .- {c}")

    def alta_cliente(self):
        self.lista_clientes.append(input("Ingrese el nombre del cliente: "))
        print("Cliente añadido.")

    def baja_cliente(self):
        try:
            self.lista_clientes.remove(int(input("Ingrese el numero del cliente a dar de baja: ")))

        except IndexError:
            print("Cliente no encontrado: ")

    def imprimir(self):
        info = super().imprimir()
        info+= f"""
Area de venta: {self.area_venta} Comision por venta: {self.comision}%
----------------------------------------------------------------- 
"""
        print(info)
        self.mostrar_clientes()
        print("""
-----------------------------------------------------------------""")
        print("1. Agg. cliente 2. Dar de Baja 3. Continuar")
        if input() == "1":
            self.alta_cliente()
        elif input() == "2":
            self.baja_cliente()
        else:
            return