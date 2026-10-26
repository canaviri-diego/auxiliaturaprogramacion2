package comp.agrega;

import java.util.ArrayList;
import java.util.Scanner;

public class COmpAgrega {

    public static void main(String[] args) {
        Scanner te = new Scanner(System.in);

        //inciso a: instanciar N objetos Laptop en un vector
        System.out.print("Cantidad de laptops (N): ");
        int n = Integer.parseInt(te.nextLine().trim());
        ArrayList<Laptop> vec = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            System.out.println("--- Laptop " + (i + 1) + " ---");
            System.out.print("Modelo: ");
            String modelo = te.nextLine();
            System.out.print("Tipo de pantalla: ");
            String tipo = te.nextLine();
            System.out.print("Ancho: ");
            int ancho = Integer.parseInt(te.nextLine().trim());
            System.out.print("Alto: ");
            int alto = Integer.parseInt(te.nextLine().trim());
            Laptop lap = new Laptop(modelo, tipo, ancho, alto);
            System.out.print("Cantidad de aplicaciones: ");
            int m = Integer.parseInt(te.nextLine().trim());
            for (int j = 0; j < m; j++) {
                System.out.print("  Nombre app " + (j + 1) + ": ");
                String nom = te.nextLine();
                System.out.print("  Tamano app " + (j + 1) + ": ");
                int tam = Integer.parseInt(te.nextLine().trim());
                lap.agregaApp(new Aplicacion(nom, tam));
            }
            vec.add(lap);
        }

        //inciso b y e: mostrar la laptop con mas aplicaciones
        System.out.println("\n=== Laptop(s) con mas aplicaciones ===");
        int may = 0;
        for (Laptop l : vec) {
            if (l.getCantApps() > may) {
                may = l.getCantApps();
            }
        }
        for (Laptop l : vec) {
            if (l.getCantApps() == may) {
                System.out.println(l);
            }
        }

        //inciso c: agregar una aplicacion a la laptop de modelo X
        System.out.print("\nModelo X al que se agrega una aplicacion: ");
        String x = te.nextLine();
        System.out.print("Nombre de la aplicacion: ");
        String nom = te.nextLine();
        System.out.print("Tamano de la aplicacion: ");
        int tam = Integer.parseInt(te.nextLine().trim());
        for (Laptop l : vec) {
            if (l.getModelo().equals(x)) {//equals, no ==
                l.agregaApp(new Aplicacion(nom, tam));
            }
        }

        //inciso d: eliminar las apps de la laptop con pantalla de ancho Y
        System.out.print("\nAncho Y de pantalla para eliminar sus aplicaciones: ");
        int y = Integer.parseInt(te.nextLine().trim());
        for (Laptop l : vec) {
            if (l.getAnchoPantalla() == y) {
                l.eliminaApps();
            }
        }

        //inciso f: ordenar apps de cada laptop (peso decreciente, empate por nombre)
        System.out.println("\n=== Aplicaciones ordenadas por laptop ===");
        for (Laptop l : vec) {
            l.ordenaApps();
            System.out.println(l);
            l.muestraApps();
        }
    }
}
