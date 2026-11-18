package SEGUNDO_SEMESTRE.PROGRAMACION_2.SEGUNDO_PARCIAL;

class Anuncio {
    private int numero;
    private double precio;

    public Anuncio(int numero, double precio) {
        this.numero = numero;
        this.precio = precio;
    }

    public double getPrecio() {
        return precio;
    }

    public void setPrecio(double precio) {
        this.precio = precio;
    }
}

class Artista {
    private String nombre;
    private int ci;
    private int aniosExperiencia;

    public Artista(String nombre, int ci, int aniosExperiencia) {
        this.nombre = nombre;
        this.ci = ci;
        this.aniosExperiencia = aniosExperiencia;
    }

    public String getNombre() {
        return nombre;
    }

    public int getAniosExperiencia() {
        return aniosExperiencia;
    }
}

class Obra {
    private String titulo;
    private String material;
    private Artista artista1;
    private Artista artista2;
    private Anuncio anuncio;

    public Obra(String titulo, String material,
                String nombre1, int ci1, int aniosExperiencia1,
                String nombre2, int ci2, int aniosExperiencia2,
                Anuncio anuncio) {
        this.titulo = titulo;
        this.material = material;
        this.artista1 = new Artista(nombre1, ci1, aniosExperiencia1);
        this.artista2 = new Artista(nombre2, ci2, aniosExperiencia2);
        this.anuncio = anuncio;
    }

    public Artista getA1() {
        return artista1;
    }

    public Artista getA2() {
        return artista2;
    }

    public Anuncio getB() {
        return anuncio;
    }

    public void setB(Anuncio anuncio) {
        this.anuncio = anuncio;
    }
}

class Pintura extends Obra {
    private String genero;

    public Pintura(String titulo, String material,
                   String nombre1, int ci1, int aniosExperiencia1,
                   String nombre2, int ci2, int aniosExperiencia2,
                   Anuncio anuncio, String genero) {
        super(titulo, material, nombre1, ci1, aniosExperiencia1, nombre2, ci2, aniosExperiencia2, anuncio);
        this.genero = genero;
    }
}

public class RepasoSegundoParcial {
    public static void main(String[] args) {
        Anuncio anuncio1 = new Anuncio(1, 300);

        Pintura p1 = new Pintura("Paisaje", "Oleo", "Hernan", 1234567, 10, "Carlos", 3456784, 2, anuncio1, "Oculto");
        Pintura p2 = new Pintura("La Noche", "Acuarela", "Juan", 4567895, 5, "Angel", 1546347, 3, null, "Realismo");

        Artista mayor = p1.getA1();
        if (p1.getA2().getAniosExperiencia() > mayor.getAniosExperiencia()) {
            mayor = p1.getA2();
        }
        if (p2.getA1().getAniosExperiencia() > mayor.getAniosExperiencia()) {
            mayor = p2.getA1();
        }
        if (p2.getA2().getAniosExperiencia() > mayor.getAniosExperiencia()) {
            mayor = p2.getA2();
        }
        System.out.println("Artista con mayor experiencia: " + mayor.getNombre());

        Anuncio anuncio2 = new Anuncio(2, 700);
        p2.setB(anuncio2);
        double total = p1.getB().getPrecio() + p2.getB().getPrecio();
        System.out.println("Monto total de ventas: " + total);
    }
}
