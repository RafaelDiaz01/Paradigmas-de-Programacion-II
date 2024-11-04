/*
Kevin Rafael Díaz López 
Este es un programa en el que debemos adivinar un número dependiendo de la dificultad.
*/

package Adivinador;

import java.util.Random;

public class Adivinador {

    int numeroIntentos; // Número de intentos realizados por el jugador
    int intentosMaximos; // Número máximo de intentos permitidos
    int numeroAdivinar; // Número que el jugador debe adivinar
    int numeroMaximo; // Límite superior del rango de números que el jugador puede adivinar
    char dificultad; // Nivel de dificultad del juego
    boolean gano; // Bandera que indica si el jugador ganó o no

    // Constructor que inicializa el juego con la dificultad especificada
    public Adivinador(char dificultad) {
        this.dificultad = dificultad;
        // Configuración de la dificultad y límites de números según la elección del usuario
        if (this.dificultad == 'f' || this.dificultad == 'F') {
            this.intentosMaximos = 15;
            this.numeroMaximo = 50;
        }

        if (this.dificultad == 'd' || this.dificultad == 'D') {
            this.intentosMaximos = 5;
            this.numeroMaximo = 100;
        }

        // Generación aleatoria del número que el jugador debe adivinar
        var rnd = new Random();
        this.numeroAdivinar = rnd.nextInt(this.numeroMaximo);
    }

    // Método para que el jugador realice un intento de adivinanza
    public boolean intentoAdivinar(int intentoActual) {
        int i = 0;
        while (i == 0) {
            // Verificación de si el número ingresado coincide con el número a adivinar
            if (this.numeroAdivinar != intentoActual) {
                // Incremento del contador de intentos
                this.numeroIntentos += 1;
                System.out.println("\nIntentos que lleva: " + numeroIntentos + "\n");
                
                // Comprobación si el número ingresado es mayor o menor que el número a adivinar
                if (intentoActual <= numeroAdivinar) {
                    System.out.println("El numero a adivinar es mayor que el número ingresado\n");
                }
                
                if (intentoActual >= numeroAdivinar) {
                    System.out.println("El numero a adivinar es menor que el número ingresado\n");
                }
            } else {
                gano = true; // Si el jugador adivina el número, establece la bandera 'gano' como verdadera
            }
            i++;
        }
        
        // Verificación si el jugador ha agotado todos sus intentos
        if (this.numeroIntentos == this.intentosMaximos) {
            System.out.println("\nL O S E");
            System.out.println("Su número a adivinar era: " + this.numeroAdivinar);
        }
        
        return gano; // Devuelve el estado de la bandera 'gano'
    }
}
