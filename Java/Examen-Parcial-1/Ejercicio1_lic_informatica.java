private void botonCalcularMouseClicked(java.awt.event.MouseEvent evt) {                                           
        try {
            var numero = Integer.parseInt(campo1.getText()); // Obtiene el número ingresado en el campo1.
            StringBuilder salida = new StringBuilder();  // Para acumular el resultado completo.
            
            for (int i = 1; i <= numero; i++) {  // Bucle que se ejecuta mientras "i" sea menor o igual a "numero".
                if (i % 3 == 0 && i % 5 == 0) {  // Comprueba si es múltiplo de 3 y 5.
                    salida.append("Licenciatura en Informática, \n");
                } else if (i % 3 == 0) {  // Comprueba si es múltiplo de 3.
                    salida.append("Licenciatura, ");
                } else if (i % 5 == 0) {  // Comprueba si es múltiplo de 5.
                    salida.append("Informática, ");
                } else {  // Si no se cumplió ninguna condición, imprime el valor de "i".
                    salida.append(i).append(", ");
                }
            }
            
            resultado.setText(salida.toString());  // Asigna el resultado acumulado al campo de texto "resultado".
        } catch (Exception e) {
            campo1.setText("");
            System.out.println("error"); // Imprime un mensaje de error en la consola.
            resultado.setText("Syntax Error"); // En el campo resultado, muestra un mensaje de error.
            JOptionPane.showMessageDialog(null, "No es un número entero"); // Muestra una ventana flotante.
        }
    }
