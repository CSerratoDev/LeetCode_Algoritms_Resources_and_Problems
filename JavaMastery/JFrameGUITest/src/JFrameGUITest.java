import javax.swing.*;

public class JFrameGUITest {
    public static void main(String[] args) {
        //Creamos el frame llamando la propiedad del constructor
        JFrame theFrame = new JFrame("Titulo del Sistema");

        // Asignamos un tamaño razonable
        // El tamaño debe ser mayor de 0, width, height en pixeles
        theFrame.setSize(1280, 720);

        //Hacemos que el marco aparezca en una ventana
        theFrame.setVisible(true);
    }
}
