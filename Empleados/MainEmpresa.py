from empleados import empleados

empleados = empleados()
empleados.default()

def menu_agg():
    print("Empleado a agregar: 1. Secretario  2. Vendedor")

    op = input("Ingrese su opcion: ")

    if op == "1":
        empleados.agg_secretario()

    elif op == "2":
        empleados.agg_vendedor()

    else:
        print("Opcion no valida")

if __name__ == '__main__':
    while True:
        print("Opciones: \n1. Agregar Empleado \n2. Mostrar Empleados \n3. Aumentar Salario")
        opcion = input("Ingrese su opcion: ")

        if opcion == "1":
            try:
                menu_agg()
            except ValueError:
                print("Datos no validos.")
            except TypeError:
                print("Datos invalidos.")

        elif opcion == "2":
            empleados.mostrar_empleados()
            print("Ingrese el numero de empleado para consultar su informacion (0 para regresar.): ")
            try:
                sel = int(input("- "))
                if sel == 0:
                    continue
                else:
                    empleados.impresion_empleado(sel-1)
            except IndexError:
                print("Empleado no encontrado")
            except ValueError:
                print("Ingrese un numero valido")

        elif opcion == "3":
            empleados.mostrar_empleados()
            print("Ingrese el numero de empleado para aumentar su sueldo (0 para regresar.): ")
            try:
                sel = int(input("- "))
                if sel == 0:
                    continue
                else:
                    empleados.aumento(sel-1)
            except IndexError:
                print("Empleado no encontrado")
            except ValueError:
                print("Ingrese un numero valido")