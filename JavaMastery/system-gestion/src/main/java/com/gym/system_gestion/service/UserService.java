package com.gym.system_gestion.service;

import com.gym.system_gestion.model.User;
import com.gym.system_gestion.repository.UserRepository;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;


@Service
public class UserService implements UserDetailsService {
    private final UserRepository userRepository;
    private final PasswordEncoder passwordEncoder;

    public UserService(UserRepository userRepository, PasswordEncoder passwordEncoder) {
        this.userRepository = userRepository;
        this.passwordEncoder = passwordEncoder;
    }
    //Es una anotación estándar de Java
    //Sirve como mecanismo de control de seguridad
    //Indica al controlador que el método tiene la intención de sobrescribir un método declarado en una clase padre (superclase)
    //En otros casos: Implementar un método definido en una interfaz
    @Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
        User user = userRepository.findByUsername(username)
                .orElseThrow(() -> new UsernameNotFoundException("User not found with username: " + username));

        return org.springframework.security.core.userdetails.User
                .withUsername(user.getUsername())
                .password(user.getPassword())
                .roles(user.getRole())
                .build();
    }

    public void registerUser(User user) {
        //Encriptamos contraseñas antes de empezar el registro
        user.setPassword(passwordEncoder.encode(user.getPassword()));

        //Asignamos el rol si no se ha especificado
        if (user.getRole() == null || user.getRole().isEmpty()) user.setRole("USER");

        //Si todo ya esta bien guardamos el usuario en la base de datos
        userRepository.save(user);
    }
}
