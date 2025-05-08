public class Main {
    public static void main(String[] args) {
        DVD[] dvdCollection = new DVD[3];
        dvdCollection[0] = new DVD("Iron Man", 2008, "Jon Favreau");
        dvdCollection[1] = new DVD("Avengers Endgame", 2019, "Brothers Russo");
        dvdCollection[2] = new DVD("The Dark Knight", 2008, "Christopher Nolan");
        for (DVD i : dvdCollection) {
            System.out.println(i);
        }
    }
}


