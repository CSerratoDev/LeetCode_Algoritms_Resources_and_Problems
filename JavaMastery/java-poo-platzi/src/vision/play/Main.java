package vision.play;
import vision.play.contenido.Movies;
import vision.play.platform.User;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        System.out.println("VISION PLAY 🎬");

        Movies movie = new Movies();
        movie.title = "Spider-Man";
        movie.releaseDate = LocalDate.of(2002, 4, 29);
        movie.gener = "Fiction";
        movie.setCalification(4.7);

        System.out.println(movie.getDataSheet());

        User user = new User();
        user.name = "Alexis";
        user.lastRegister = LocalDateTime.of(2025, 12, 17, 14, 50, 10);

        System.out.println(user.lastRegister);
        user.watch(movie);

//        Scanner scanner = new Scanner(System.in);
//        System.out.println("Cual es tu nombre?");
//        String nombre = scanner.nextLine();
//        System.out.println("Hola " + nombre + " ¡Bienvenido a Vision Play!");
//
//        System.out.println(nombre + " cuantos años tieneS?");
//        int edad = scanner.nextInt();
//        System.out.println(nombre + " puede ver contenido +" + edad);


    }
}