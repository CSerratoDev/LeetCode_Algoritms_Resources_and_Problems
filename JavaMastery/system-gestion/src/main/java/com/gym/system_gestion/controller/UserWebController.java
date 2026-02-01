package com.gym.system_gestion.controller;

import com.gym.system_gestion.model.User;
import com.gym.system_gestion.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;

//Es una anotación clásica de Spring MVC
//La diferencia con RestController es que esta no está pensada para devolver datos crudos JSON
//Devuelve nombres de vistas: HTML - Thymeleaf - JSP
//Actua como intermediaria que prepara los modelos de datos
//Selecciona que plantilla HTML mostrar al usuario
@Controller
public class UserWebController {

    @Autowired
    private UserService userService;

    // Spring Security redirige aquí si no se está autenticado el usuario/cliente
    @GetMapping("/login")
    public String login(){
        return "login";
    }

    // Spring Security redirige aquí si esta autenticado el usuario/cliente
    @GetMapping("/dashboard")
    public String home() { return "dashboard";} // Este es el nombre del HTML


    @GetMapping("/register")
    public String register(Model model){
        //Creamos un objeto vacio para el HTML
        //Thymeleaf lo necesitará para guardar datos ahí
        model.addAttribute("user", new User());
        return "register";
    }

    @PostMapping("/register")
    public String saveRegister(@ModelAttribute User user){
        //Llamamos al servicio para la encriptación del password
        userService.registerUser(user);

        //Usamos redirección para que envie el usuario al login
        return "redirect:/login";
    }
}
