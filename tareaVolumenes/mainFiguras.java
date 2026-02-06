package tareaVolumenes;
import java.util.Scanner;

public class mainFiguras {
    
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        
        while(true){

            System.out.print("""
                    Opciones:
                        1. Cubo
                        2. Cilindro
                        3. Cono
                        4. Esfera
                        0. Salir
                    Opción: """);
            int opcion = sc.nextInt();

            switch (opcion) {
                case 0 -> {;
                    sc.close();
                    return;
                }

                case 1 -> {
                    System.out.print("Ingrese la arista del cubo: ");
                    int arista = sc.nextInt();
                    Cubo cubo = new Cubo(arista, 0);
                    System.out.println("El volumen del cubo es: " + cubo.calcularVolumen());
                }

                case 2 -> {
                    System.out.print("Ingrese la altura del cilindro: ");
                    int arista = sc.nextInt();
                    System.out.print("Ingrese el radio del cilindro: ");
                    int radio = sc.nextInt();
                    Cilindro cilindro = new Cilindro(arista, radio);
                    System.out.println("El volumen del cilindro es: " + cilindro.calcularVolumen());
                }

                case 3 -> {
                    System.out.print("Ingrese la altura del cono: ");
                    int arista = sc.nextInt();
                    System.out.print("Ingrese el radio del cono: ");
                    int radio = sc.nextInt();
                    Cono cono = new Cono(arista, radio);
                    System.out.println("El volumen del cono es: " + cono.calcularVolumen());
                }

                case 4 -> {
                    System.out.print("Ingrese el radio de la esfera: ");
                    int radio = sc.nextInt();
                    Esfera esfera = new Esfera(radio);
                    System.out.println("El volumen de la esfera es: " + esfera.calcularVolumen());
                }
            
                default -> System.out.println("Opción no válida.");
            }
            System.out.println();
        }
    }
}
