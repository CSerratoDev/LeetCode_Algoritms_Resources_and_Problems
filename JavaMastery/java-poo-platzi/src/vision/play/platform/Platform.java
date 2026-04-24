package vision.play.platform;

import vision.play.contenido.Movies;

import java.util.ArrayList;
import java.util.List;

public class Platform {
    private String name;
    private List<Movies> content;

    public Platform(String name) {
        this.name = name;
        this.content = new ArrayList<>();
    }

    public void addElement(Movies element){
        this.content.add(element);
    }

    public void viewTitles() {
        for (Movies movies : content) {
            System.out.println("Lista de contenidos!");
            System.out.println(movies.getTitle());
        }
    }

    public void deleteElement(Movies element) {
        this.content.remove(element);
    }

    public String getName() {
        return name;
    }

    public List<Movies> getContent() {
        return content;
    }
}
