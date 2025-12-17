package vision.play.util;

import java.util.Scanner;

public class ScannerUtils {
    public static Scanner scanner = new Scanner(System.in);

    public static String captureText(String message){
        System.out.println(message + ": ");
        return scanner.nextLine();
    }

    public static int captureNumber(String message){
        System.out.println(message + ": ");

        int data = scanner.nextInt();
        scanner.nextLine();
        return data;
    }

    public static double captureDecimal(String message){
        System.out.println(message + ": ");

        double data = scanner.nextDouble();
        scanner.nextLine();
        return data;
    }
}
