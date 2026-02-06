package tareaVolumenes;

public class Esfera extends Figura {

    public Esfera(int radio) {
        this.radio = radio;
    }
    
    public double calcularVolumen() {
        return (4 * Math.PI * Math.pow(radio, 3)) / 3;
    }
}
