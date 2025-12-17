package vision.play;
import vision.play.contenido.Movies;
import vision.play.platform.User;
import vision.play.util.ScannerUtils;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        System.out.println("VISION PLAY 🎬");

        String name = ScannerUtils.captureText("Nombre del contenido");
        String gener = ScannerUtils.captureText("Genero del contenido");
        int duration = ScannerUtils.captureNumber("Duración del contenido");
        double calification = ScannerUtils.captureDecimal("Calificación del contenido");

        Movies movie = new Movies();
        movie.title = name;
        movie.releaseDate = LocalDate.of(2002, 4, 29);
        movie.gener = gener;
        movie.setCalification(calification);
        movie.duration = duration;

        System.out.println(movie.getDataSheet());

        User user = new User();
        user.name = "Alexis";
        user.lastRegister = LocalDateTime.of(2025, 12, 17, 14, 50, 10);

        user.watch(movie);
    }
}