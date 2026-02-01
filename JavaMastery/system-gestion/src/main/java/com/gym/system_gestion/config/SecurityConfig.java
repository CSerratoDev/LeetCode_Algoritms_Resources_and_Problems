package com.gym.system_gestion.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.web.SecurityFilterChain;

//Es una anotación a nivel de clase de Spring
//Indica que dicha clase es una fuente de definiciones Beans -> Remplazo de Java-based

//La ventaja usan Singletons, es decir, aunque llames al método varias veces
//Spring intercepta el call y retorna siempre la misma instancia del objeto (Bean) en memoria.
@Configuration

//Es una anotación de configuración
//Activa el soporte de seguridad web en la app

//Esta detiene a Spring porque yo voy a definir mis propias reglas de acceso, formularios login y filtros.
@EnableWebSecurity
public class SecurityConfig {
    //Es una anotación a nivel de método
    //Le dice a Spring = Ejecuta este método y el objeto que devuelva administralo tú en el contenedor de la app

    //Es la forma manual de registrar componentes a diferencia de @Service o @Controller que son automáticos
    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
                .authorizeHttpRequests(auth -> auth
                        //Rutas públicas no requieren auth
                        .requestMatchers("/css/**", "/js/**", "/login", "/register").permitAll()
                        //Rutas privadas requieren auth
                        .anyRequest().authenticated()
                )
                .formLogin(form -> form
                        //URl del controlador
                        .loginPage("/login")
                        //La siguiente URL a donde redirigira al logearse
                        .defaultSuccessUrl("/dashboard", true)
                        .permitAll()
                )
                .logout(logout -> logout
                        //Define la URL de logout
                        .logoutUrl("/logout")
                        //Define la siguiente URL a donde redirige al deslogearse
                        .logoutSuccessUrl("/login?logout")
                        //Define que todos tienen acceso a esta ruta
                        //Es obvio, pero es necesario no lo olvides.
                        .permitAll()
                );

        return http.build();
    }

    @Bean //Bean para encriptar contraseñas es Obligatorio
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }
}
