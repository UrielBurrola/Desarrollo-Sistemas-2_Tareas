import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class mainApp {
    private JLabel lb1;
    private JTextField cal1;
    private JTextField cal2;
    private JTextField cal3;
    private JButton calcularButton;
    private JLabel lbPromedio;
    private JLabel lbDesviacion;
    private JLabel lbMax;
    private JLabel lbMin;
    private JPanel ventanaP;

    public mainApp() {
        calcularButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try {
                    int n1 = Integer.parseInt(cal1.getText());
                    int n2 = Integer.parseInt(cal2.getText());
                    int n3 = Integer.parseInt(cal3.getText());
                    int[] valores = {n1, n2, n3};

                    int max = valores[0];
                    int min = valores[0];
                    int promedio = (n1+n2+n3) / valores.length;
                    int ESuma = 0;

                    for(int v : valores){
                        //Comprobacion de rango valido para los valores
                        if (v < 0 || v > 10){
                            throw new IllegalArgumentException("Las calificaciones solo pueden estar entre 0 y 10.");
                        }

                        //Sumatoria para la desviacion
                        ESuma += (int) Math.pow(v-promedio, 2);

                        min = Math.min(v, min);
                        max = Math.max(v, max);

                    }

                    double desviacion = Math.sqrt((double) (ESuma /valores.length));

                    lbPromedio.setText("Promedio: " + promedio);
                    lbDesviacion.setText(String.format("Desviacion Estandar: %.2f", desviacion));
                    lbMax.setText("Nota Maxima: " + max);
                    lbMin.setText("Nota Minima: " + min);
                }

                // Excepciones
                catch (NumberFormatException nfe){
                    JOptionPane.showMessageDialog(ventanaP,
                            "Calificacion Invalida",
                            "Error", JOptionPane.ERROR_MESSAGE
                            );
                    cal1.setText("");
                    cal2.setText("");
                    cal3.setText("");

                }
                catch (IllegalArgumentException a){
                    JOptionPane.showMessageDialog(ventanaP,
                            a.getMessage(),
                            "Error", JOptionPane.ERROR_MESSAGE
                    );
                    cal1.setText("");
                    cal2.setText("");
                    cal3.setText("");
                }

            }
        });

    }

    public static void main(String[] args){
        JFrame ventana = new JFrame("Calculos Calificaciones");
        ventana.setContentPane(new mainApp().ventanaP);
        ventana.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        ventana.pack();
        ventana.setLocationRelativeTo(null);
        ventana.setVisible(true);
    }
}
