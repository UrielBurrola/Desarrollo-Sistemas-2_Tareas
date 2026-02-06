package tareaVolumenes;

public class Cilindro extends Figura {

    public Cilindro(int arista, int radio) {
        this.arista = arista;
        this.radio = radio;
    }
    
    public double calcularVolumen() {
        return Math.PI * Math.pow(radio, 2) * arista;
    }
}
