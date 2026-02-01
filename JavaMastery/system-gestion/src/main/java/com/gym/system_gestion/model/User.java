package com.gym.system_gestion.model;

import jakarta.persistence.*;

import java.util.UUID;

//Es una anotación del estándar JPA (Java Persistence API)
//La marca como una entidad persistente
//Indica al ORM Hibernate que esta clase es una tabla en la base de datos
//También que sus instancias son filas
@Entity
@Table(name = "usuarios")
public class User {
    @Id // Representa una clave primaria (PK)
    @GeneratedValue(strategy = GenerationType.UUID)
    private UUID userId; //Tipo de variable UUID (cadena alfanumérica larga)
    //Getter
    public String getUsername() {
        return username;
    }

    public String getPassword() {
        return password;
    }
    public String getRole() {
        return role;
    }
    //Setter
    public void setPassword(String password) {
        this.password = password;
    }

    public void setRole(String role) {
        this.role = role;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    //Representa una columna de la tabla específica.
    @Column(nullable = false, unique = true)  // Podemos agregar parámetros
    // nullable es que no puede ser nulo el dato, por lo tanto, obligatorio
    // unique es que no puede haber un dato igual en la base de datos, esto mantiene seguridad
    private String username;

    @Column(nullable = false)
    private String password;

    @Column(nullable = false)
    private String role;
    // EL ORM Hibernate requiere un constructor vacío
    public User() {}
    // Constructor de User
    public User(String username, String password, String role) {
        this.username = username;
        this.password = password;
        this.role = role;
    }

}
