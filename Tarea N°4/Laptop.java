package comp.agrega;

public class Laptop {
    private String modelo;
    private int cantApps;
    private Aplicacion[] apps = new Aplicacion[50];
    private Pantalla pantalla;//composicion: la pantalla se crea dentro de la laptop

    public Laptop(String modelo, String tipo, int ancho, int alto) {
        this.modelo = modelo;
        this.cantApps = 0;
        this.pantalla = new Pantalla(tipo, ancho, alto);
    }

    public String getModelo() {
        return this.modelo;
    }

    public int getCantApps() {
        return this.cantApps;
    }

    public int getAnchoPantalla() {
        return this.pantalla.getAncho();
    }

    //inciso c
    public boolean agregaApp(Aplicacion app) {
        if (this.cantApps < 50) {
            this.apps[this.cantApps] = app;
            this.cantApps++;
            return true;
        }
        return false;
    }

    //inciso d
    public void eliminaApps() {
        for (int i = 0; i < this.cantApps; i++) {
            this.apps[i] = null;
        }
        this.cantApps = 0;
    }

    //inciso f: peso decreciente, si hay empate por nombre
    public void ordenaApps() {
        for (int i = 0; i < this.cantApps - 1; i++) {
            for (int j = 0; j < this.cantApps - 1 - i; j++) {
                Aplicacion a = this.apps[j];
                Aplicacion b = this.apps[j + 1];
                boolean cambiar = false;
                if (a.getTamano() < b.getTamano()) {
                    cambiar = true;
                } else if (a.getTamano() == b.getTamano()
                        && a.getNombre().compareToIgnoreCase(b.getNombre()) > 0) {
                    cambiar = true;
                }
                if (cambiar) {
                    this.apps[j] = b;
                    this.apps[j + 1] = a;
                }
            }
        }
    }

    public void muestraApps() {
        if (this.cantApps == 0) {
            System.out.println("   (sin aplicaciones)");
        }
        for (int i = 0; i < this.cantApps; i++) {
            System.out.println("   " + this.apps[i]);
        }
    }

    @Override
    public String toString() {
        return "Laptop{" + "modelo=" + modelo + ", cantApps=" + cantApps + ", pantalla=" + pantalla + '}';
    }
}
