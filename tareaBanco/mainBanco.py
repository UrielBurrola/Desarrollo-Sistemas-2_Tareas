from PrestamoAuto import PrestamoAuto
from PrestamoHipoteca import PrestamoHipoteca
from PrestamoPersonal import PrestamoPersonal


def mostrarprestamos(lista_prestamos):
    for prestamo in lista_prestamos:
        print(prestamo)
    
    print("\n ingrese el numero de prestamo pra mostrar detalles de los préstamos")
    opcion = int(input(": "))
    if opcion < 1 or opcion > len(lista_prestamos):
        print("Opción inválida. Por favor, seleccione un número válido.")
        return
    else:
        print(lista_prestamos[opcion-1].mostrar_informacion())

def main():

    lista_prestamos = []
    while True:
        print("""
        Seleccione el tipo de préstamo:
        ----------------------------------
        1. Prestamo Personal
        2. Prestamo Hipotecario
        3. Prestamo Automotriz
        ----------------------------------
        4. Mostrar Prestamos
        ----------------------------------
        0. Salir
              """)
        opcion = input(": ")

        if opcion in ["1", "2", "3"]:
            nombre = input("Ingrese el nombre del cliente: ")
            no_cuenta = input("Ingrese el número de cuenta: ")
            prestamo = float(input("Ingrese el monto del préstamo: "))
            plazo_inversion = int(input("Ingrese el plazo de inversión (en años): "))

            if opcion == "1":
                cliente = PrestamoPersonal(no_cliente=len(lista_prestamos)+1, nombre=nombre, no_cuenta=no_cuenta, prestamo=prestamo, plazo_inversion=plazo_inversion)
                lista_prestamos.append(cliente)

            elif opcion == "2":
                cliente = PrestamoHipoteca(no_cliente=len(lista_prestamos)+1, nombre=nombre, no_cuenta=no_cuenta, prestamo=prestamo, plazo_inversion=plazo_inversion)
                lista_prestamos.append(cliente)

            elif opcion == "3":
                cliente = PrestamoAuto(no_cliente=len(lista_prestamos)+1, nombre=nombre, no_cuenta=no_cuenta, prestamo=prestamo, plazo_inversion=plazo_inversion)
                lista_prestamos.append(cliente)

        elif opcion == "4":
            mostrarprestamos(lista_prestamos)

        elif opcion == "0":
            break

if __name__ == "__main__":
    main()