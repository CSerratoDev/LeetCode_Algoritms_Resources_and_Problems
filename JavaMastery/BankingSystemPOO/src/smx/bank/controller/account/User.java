package smx.bank.controller.account;

import java.time.LocalDate;

public class User {
    public String name;
    public String email;
    public LocalDate birthDate;

    public String getData(){
        return "Nombre: " + name +
                "\nEmail: " + email +
                "\nFecha de nacimiento: " + birthDate;
    }
}
