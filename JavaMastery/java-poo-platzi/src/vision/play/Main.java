package vision.play;
import vision.play.contenido.Movies;
import vision.play.platform.Platform;
import vision.play.platform.User;
import vision.play.util.ScannerUtils;

public class Main {
    public static final String NAME_PLATFORM = "VISION PLAY";
    public static final String VERSION = "1.0.0";
    public static final int SALIR = 5;
    public static final int AGREGAR = 1;
    public static final int MOSTRAR = 2;
    public static final int BUSCAR = 3;
    public static final int ELIMINAR = 4;

    public static void main(String[] args) {
        Platform platform = new Platform(NAME_PLATFORM);
        System.out.println(NAME_PLATFORM + " v" + VERSION);

        while(true) {
            int option = ScannerUtils.captureNumber("""
                    Ingresa una de las siguientes opciones
                    1) Agregar contenido
                    2) Mostrar todo
                    3) Buscar titulo
                    4) Eliminar
                    5) Salir
                    """);
            System.out.println("Opcion elegida: " + option);

            switch (option) {
                case AGREGAR -> {
                    String name = ScannerUtils.captureText("Nombre del contenido");
                    String gener = ScannerUtils.captureText("Genero del contenido");
                    int duration = ScannerUtils.captureNumber("Duración del contenido");
                    double calification = ScannerUtils.captureDecimal("Calificación del contenido");

                    platform.addElement(new Movies(name, duration, gener, calification));
                }
                case MOSTRAR -> platform.viewTitles();
                case BUSCAR -> {

                }
                case ELIMINAR -> {

                }
                case SALIR -> System.exit(0);
            }
        }

        //User user = new User("Alexis", "ale@visionplay.com");
        //user.watch(movie);
    }
}