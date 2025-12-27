package vision.play.contenido;

import java.time.LocalDate;

public class Movies {
    private String title;
    private String description;
    private int duration;
    private String gener;
    private LocalDate releaseDate;
    private double calification;
    private boolean status;

    public Movies(String title, int duration, String gener) {
        this.title = title;
        this.duration = duration;
        this.gener = gener;
        this.releaseDate = LocalDate.now();
        this.status = true;
    }

    public Movies(String title, int duration, String gener, double calification) {
        this(title, duration, gener);
        this.setCalification(calification);
    }

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

    public String getTitle() {
        return title;
    }

    public String getDescription() {
        return description;
    }

    public int getDuration() {
        return duration;
    }

    public String getGener() {
        return gener;
    }

    public LocalDate getReleaseDate() {
        return releaseDate;
    }

    public double getCalification() {
        return calification;
    }

    public boolean isStatus() {
        return status;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public void setReleaseDate(LocalDate releaseDate) {
        this.releaseDate = releaseDate;
    }

    public void setStatus(boolean status) {
        this.status = status;
    }
}