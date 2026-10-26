package comp.agrega;

public class Pantalla {
    private String tipo;
    private int ancho;
    private int alto;

    public Pantalla(String tipo, int ancho, int alto) {
        this.tipo = tipo;
        this.ancho = ancho;
        this.alto = alto;
    }

    public Pantalla() {
        this.tipo = "amoled";
        this.ancho = 7;
        this.alto = 6;
    }

    public int getAncho() {
        return this.ancho;
    }

    @Override
    public String toString() {
        return "Pantalla{" + "tipo=" + tipo + ", ancho=" + ancho + ", alto=" + alto + '}';
    }
}
