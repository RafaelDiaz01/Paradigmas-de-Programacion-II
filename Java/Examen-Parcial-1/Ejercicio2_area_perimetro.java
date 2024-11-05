    private void boton1ActionPerformed(java.awt.event.ActionEvent evt) {                                       
        // Calcula el área del rectangulo:
        try {
            // Solicita los valores de base y altura como cadenas de texto
            String baseStr = JOptionPane.showInputDialog(null, "Ingrese la base del rectángulo");
            String alturaStr = JOptionPane.showInputDialog(null, "Ingrese la altura del rectángulo");

            // Convierte las entradas de texto en números de tipo double
            double base = Double.parseDouble(baseStr);
            double altura = Double.parseDouble(alturaStr);

            double area = base * altura; // Calcula el área

            // Muestra el resultado en un cuadro de diálogo
            JOptionPane.showMessageDialog(null, "Área del rectángulo: " + area);
        } catch (NumberFormatException e) {
            JOptionPane.showMessageDialog(null, "Por favor, ingrese valores numéricos válidos.");
        }
    }                                      

    private void boton2ActionPerformed(java.awt.event.ActionEvent evt) {                                       
        // Calcula el perímetro del rectángulo:
        try {
            // Solicita los valores de base y altura como cadenas de texto
            String baseStr = JOptionPane.showInputDialog(null, "Ingrese la base del rectángulo");
            String alturaStr = JOptionPane.showInputDialog(null, "Ingrese la altura del rectángulo");

            // Convierte las entradas de texto en números de tipo double
            double base = Double.parseDouble(baseStr);
            double altura = Double.parseDouble(alturaStr);

            double perimetro = 2 * (base + altura); // Calcula el perímetro.

            // Muestra el resultado en un cuadro de diálogo
            JOptionPane.showMessageDialog(null, "Perímetro del rectángulo: " + perimetro);
        } catch (NumberFormatException e) {
            JOptionPane.showMessageDialog(null, "Por favor, ingrese valores numéricos válidos.");
        }
    }                                      

    private void boton3ActionPerformed(java.awt.event.ActionEvent evt) {                                       
        // Calcula el área del círculo:
        try {
            // Solicita el valor del radio como cadena de texto.
            String radioStr = JOptionPane.showInputDialog(null, "Ingrese el radio del círculo");

            // Convierte la entrada de texto en números de tipo double
            double radio = Double.parseDouble(radioStr);

            double area = 3.1416 * radio * radio; // Calcula el área

            // Muestra el resultado en un cuadro de diálogo
            JOptionPane.showMessageDialog(null, "Área del círculo: " + area);
        } catch (NumberFormatException e) {
            JOptionPane.showMessageDialog(null, "Por favor, ingrese valores numéricos válidos.");
        }
    }                                      

    private void boton4ActionPerformed(java.awt.event.ActionEvent evt) {                                       
        // Calcula el perímetro del círculo:
        try {
            // Solicita el valor del radio como cadenas de texto.
            String radioStr = JOptionPane.showInputDialog(null, "Ingrese el radio del circulo");

            // Convierte las entradas de texto en números de tipo double.
            double radio = Double.parseDouble(radioStr);

            double peri = 3.1416 * 2 * radio; // Calcula el perímetro.

            // Muestra el resultado en un cuadro de diálogo
            JOptionPane.showMessageDialog(null, "Perímetro del círculo: " + peri);
        } catch (NumberFormatException e) {
            JOptionPane.showMessageDialog(null, "Por favor, ingrese valores numéricos válidos.");
        }
    }     
