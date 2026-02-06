package tareaVolumenes;

public class Cubo extends Figura {

    public Cubo(int arista, int radio) {
        this.arista = arista;
        this.radio = radio;
    }
    
    public double calcularVolumen() {
        return Math.pow(arista, 3);
    }
}
