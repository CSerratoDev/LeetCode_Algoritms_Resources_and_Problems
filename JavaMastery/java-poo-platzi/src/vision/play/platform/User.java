package vision.play.platform;
import vision.play.contenido.Movies;

import java.time.LocalDateTime;

public class User {
    public String name;
    public String email;
    public LocalDateTime lastRegister;

    public void watch(Movies movie) {
        System.out.println(name + " esta viendo...");
        movie.play();
    }
}
