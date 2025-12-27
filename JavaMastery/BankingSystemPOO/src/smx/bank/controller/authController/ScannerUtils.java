package smx.bank.controller.authController;

import java.util.Scanner;

public class ScannerUtils {
    public static Scanner scanner = new Scanner(System.in);
    //para capturar texto, por ejemplo para los datos del usuario
    public static String captureText(String message){
        System.out.println(message + ": ");
        return scanner.nextLine();
    }
    //para capturar valores enteros, como por ejemplo la edad
    public static int captureInt(String message){
        System.out.println(message + ": ");
        int data = scanner.nextInt();
        scanner.nextLine();
        return data;
    }
}
