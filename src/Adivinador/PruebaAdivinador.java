/*
Kevin Rafael Díaz López 02/05/2024
Este es la prueba del programa en el que debemos adivinar un número dependiendo de la dificultad.
 */
package Adivinador;

import java.util.Scanner;

public class PruebaAdivinador {

    public static void main(String[] args) {
        Scanner consola = new Scanner(System.in);
        System.out.println("J U E G O   A D I V I N A D O R");
        System.out.println(); // Salto de línea.

        System.out.println("Seleccione la dificultad (Facil / Dificil):");
        char dificultad = 'l'; //Inicializa la variable dificultad para que el while intere mientras sea diferente de facil o dificil.
        while (dificultad != 'f' && dificultad != 'F' && dificultad != 'd' && dificultad != 'D') {
            dificultad = consola.next().charAt(0);
            if (dificultad != 'f' && dificultad != 'F' && dificultad != 'd' && dificultad != 'D') { //Verifica que la letra ingresada sea f/F o d/D.
                System.out.println("Error, seleccione correctamente la dificultad (f/F o d/D)");
            }
        }
        Adivinador juego = new Adivinador(dificultad);
        //TRAMPA: System.out.println("\nNúmero a adivinar: " + juego.numeroAdivinar);

        for (int i = 0; juego.numeroIntentos != juego.intentosMaximos; i++) {

            System.out.println("Ingrese un número");
            int num = consola.nextInt(); //Lee el número
            juego.intentoAdivinar(num); //Se manda el número

            if (juego.gano == true) { //Comprueba si gano es igual a true.
                System.out.println("\nW I N");
                break;
            }
        }
    }
}
