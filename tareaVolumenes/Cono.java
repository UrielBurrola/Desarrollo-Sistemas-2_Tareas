package tareaVolumenes;

public class Cono extends Figura {

    public Cono(int arista, int radio) {
        this.arista = arista;
        this.radio = radio;
    }
    
    public double calcularVolumen() {
        return  (4* (Math.PI * Math.pow(radio, 2) * arista)) / 3;
    }
}
