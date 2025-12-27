package vision.play;
import vision.play.contenido.Movies;
import vision.play.platform.User;
import vision.play.util.ScannerUtils;

public class Main {
    public static final String NAME_PLATFORM = "VISION PLAY";
    public static final String VERSION = "1.0.0";

    public static void main(String[] args) {
        System.out.println(NAME_PLATFORM + " v" + VERSION);

        String name = ScannerUtils.captureText("Nombre del contenido");
        String gener = ScannerUtils.captureText("Genero del contenido");
        int duration = ScannerUtils.captureNumber("Duración del contenido");
        double calification = ScannerUtils.captureDecimal("Calificación del contenido");

        Movies movie = new Movies(name, duration, gener, calification);
        System.out.println(movie.getDataSheet());

        User user = new User("Alexis", "ale@visionplay.com");
        user.watch(movie);
    }
}