package com.gym.system_gestion.controller;

import com.gym.system_gestion.model.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.gym.system_gestion.repository.UserRepository;

import java.util.List;

@RestController
@RequestMapping("/api/users")
public class UserController {
    // Es una anotación de Spring Framework para la inyección de dependencias
    // Indica que busque un objeto
    // Esto le asigna automáticamente a la propiedad, constructor o método
    @Autowired
    private UserRepository userRepository;
    // Es una anotación de Spring MVC
    // Maneja solicitudes HTTP del tipo GET -> GETTER
    // Se coloca sobre métodos del controlador para vincularlos a una URL
    // Función: Recuperar datos del servidor sin modificar nada en la Base de datos
    @GetMapping
    public List<User> getAllUsers() {return userRepository.findAll();}
    //GetMapping se usa más para operaciones de lectura como:
    //Consultas, Búsquedas, Mostrar páginas
    @GetMapping("/crear-demo")
    public User createDemoUser() {
        User u = new User();
        u.setUsername("Dueño Alexis");
        u.setRole("ADMIN");
        u.setPassword("123456");

        return userRepository.save(u);
    }
}
