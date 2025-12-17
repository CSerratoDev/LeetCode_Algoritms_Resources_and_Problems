package vision.play.contenido;

import java.time.LocalDate;

public class Movies {
    public String title;
    public String description;
    public int duration;
    public String gener;
    public LocalDate releaseDate;
    public double calification;
    public boolean status;

    public void play() {
        System.out.println("Reproduciendo " + title);
    }

    public String getDataSheet(){
        return title + " (" + releaseDate.getYear() + ")\n" +
                "Género: " + gener +
                "\nCalificacion: " + calification + "/5";
    }

    public void setCalification(double calification){
        if (calification >= 0 && calification <= 5) {
            this.calification = calification;
        }
    }

    public boolean isPopular(){
        return calification >= 4;
    }
}