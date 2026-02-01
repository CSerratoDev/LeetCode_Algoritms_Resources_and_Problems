package com.gym.system_gestion.repository;

import com.gym.system_gestion.model.User;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.Optional;
//Es una anotación de estereotipo de Spring Framework
//Marca la clase / interfaz
//Actua como la capa de acceso a datos (Persistencia)
//Registra el bean (objeto)
//Convierte errores técnicos a una jerarquía de excepciones unificadas y comprensibles de Spring
@Repository
public interface UserRepository extends JpaRepository<User, Long> {
    //JpaRepository mantiene la capa de servicio limpia, si hay cambios de base de datos
    //la traducción de excepciones siguen siendo las mismas.

    //Optional sirve para manejar elegantemente si no existe el objeto
    Optional<User> findByUsername(String username);
}
