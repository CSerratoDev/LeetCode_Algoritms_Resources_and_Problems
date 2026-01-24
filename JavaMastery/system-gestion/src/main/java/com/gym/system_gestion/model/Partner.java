package com.gym.system_gestion.model;

import jakarta.persistence.*; // Importante: Spring Boot 3 usa 'jakarta', no 'javax'
import java.time.LocalDate;

@Entity // Esto le dice a Spring: "Haz una tabla de esto"
@Table(name = "socios") // Nombre de la tabla en MySQL
public class Partner {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY) // Auto-increment (1, 2, 3...)
    private Long id;

    @Column(nullable = false, length = 100)
    private String nombre;

    @Column(nullable = false, unique = true) // No puede haber dos emails iguales
    private String email;

    private LocalDate fechaRegistro;

    @Column(name = "fecha_vencimiento")
    private LocalDate fechaVencimiento;

    public LocalDate getFechaVencimiento() {
        return fechaVencimiento;
    }
    public void setFechaVencimiento(LocalDate fechaVencimiento) {
        this.fechaVencimiento = fechaVencimiento;
    }

    private boolean activo;

    // --- CONSTRUCTORES ---
    public Partner() {
        // Constructor vacío requerido por JPA
    }

    public Partner(String nombre, String email) {
        this.nombre = nombre;
        this.email = email;
        this.fechaRegistro = LocalDate.now();
        this.activo = true;
    }

    // --- GETTERS Y SETTERS (Obligatorios) ---
    // Puedes generarlos con clic derecho -> Source -> Generate Getters and Setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getNombre() { return nombre; }
    public void setNombre(String nombre) { this.nombre = nombre; }
    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }
}