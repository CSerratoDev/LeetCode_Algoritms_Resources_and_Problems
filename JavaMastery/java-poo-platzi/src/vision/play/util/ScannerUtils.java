package vision.play.util;

import java.util.Scanner;

public class ScannerUtils {
    public static final Scanner SCANNER = new Scanner(System.in);

    public static String captureText(String message){
        System.out.print(message + ": ");
        return SCANNER.nextLine();
    }

    public static int captureNumber(String message){
        System.out.print(message + ": ");

        while(!SCANNER.hasNextInt()) {
            System.out.println("El dato es invalido " + message + ": ");
            SCANNER.next();
        }

        int data = SCANNER.nextInt();
        SCANNER.nextLine();
        return data;
    }

    public static double captureDecimal(String message){
        System.out.print(message + ": ");

        while(!SCANNER.hasNextDouble()) {
            System.out.println("El dato es invalido " + message + ": ");
            SCANNER.next();
        }
        double data = SCANNER.nextDouble();
        SCANNER.nextLine();
        return data;
    }
}
