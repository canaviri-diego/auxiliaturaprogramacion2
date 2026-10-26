package comp.agrega;

public class Aplicacion {
    private String nombre;
    private int tamano;

    public Aplicacion(String nombre, int tamano) {
        this.nombre = nombre;
        this.tamano = tamano;
    }

    public Aplicacion() {
        this.nombre = "";
        this.tamano = 0;
    }

    public String getNombre() {
        return this.nombre;
    }

    public int getTamano() {
        return this.tamano;
    }

    @Override
    public String toString() {
        return "Aplicacion{" + "nombre=" + nombre + ", tamano=" + tamano + '}';
    }
}
