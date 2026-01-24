package com.gym.system_gestion.repository;

import com.gym.system_gestion.model.Partner;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface PartnerRepository extends JpaRepository<Partner, Long>{
    // Al extender de JpaRepository, Spring crea automáticamente métodos para:
    // .save()   -> Guardar
    // .findAll() -> Buscar todos
    // .findById() -> Buscar por ID
    // .delete() -> Borrar

    // SELECT * FROM socios WHERE LOWER(nombre) LIKE %palabraClave%
    List<Partner> findByNombreContainingIgnoreCase(String palabraClave);
}
