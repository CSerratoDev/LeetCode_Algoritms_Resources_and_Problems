public class Main {
    public static void main(String[] args) {
        DVD[] dvdCollection = new DVD[3];
        DVD avengersDVD = new DVD("Avengers Endgame", 2019, "Brothers Russo");
        dvdCollection[0] = avengersDVD;
        System.out.println(dvdCollection[0]);
    }
}


