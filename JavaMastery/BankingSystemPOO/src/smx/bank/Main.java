package smx.bank;
import smx.bank.controller.account.User;
import smx.bank.controller.authController.ScannerUtils;

import java.time.LocalDate;

public class Main {
    public static void main(String[] args){
        System.out.println("SMX Bank 💰");

        String name = ScannerUtils.captureText("Ingresa tu nombre");
        int age = ScannerUtils.captureInt("Ingresa tu edad");

        User user = new User();
        user.name = name;
        user.email = "test@gmail.com";
        user.birthDate = LocalDate.of(2000,1,1);

        System.out.println(user.getData());

        if(age < 18){
            System.out.println("No tienes edad para tener una cuenta de banco");
        } else if (age <= 69){
            System.out.println("Bienvenido a SMX Bank, " + name + "!");
        }
    }
}
