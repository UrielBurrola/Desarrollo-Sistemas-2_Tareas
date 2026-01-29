class Empleado:

    def __init__(self, nombre, apellidos, RFC, direccion, años, telefono, salario):
        self.nombre = nombre
        self.apellido = apellidos
        self.RFC = RFC
        self.direccion = direccion
        self.añosAntiguedad = años
        self.telefono = telefono
        self.salario = salario
        self.aumento = 0.0

    def aumento_salario(self):
        self.salario += self.salario * self.aumento

    def imprimir(self):
        info = f""" 
Nombre: {self.nombre} {self.apellido}
-----------------------------------------------------------------  
        {self.direccion}  Telefono: {self.telefono}
        RFC: {self.RFC}
        
        Salario: {self.salario}  Años de antiguedad: {self.añosAntiguedad}
-----------------------------------------------------------------"""
        return info

