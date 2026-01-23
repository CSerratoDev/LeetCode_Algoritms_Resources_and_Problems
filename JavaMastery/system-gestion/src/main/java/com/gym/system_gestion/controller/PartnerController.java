package com.gym.system_gestion.controller;

import com.gym.system_gestion.model.Partner;
import com.gym.system_gestion.repository.PartnerRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/partners") // La URL base será http://localhost:8080/api/partners
public class PartnerController {

    @Autowired
    private PartnerRepository partnerRepository;

    // 1. Ver todos los socios
    @GetMapping
    public List<Partner> getAllPartners() {
        return partnerRepository.findAll();
    }

    // 2. Crear un socio de prueba (Demo)
    @GetMapping("/crear-demo")
    public Partner createDemoPartner() {
        // Asegúrate de que tu constructor en Partner.java coincida con esto
        // Si no tienes constructor, usa los setters:
        Partner p = new Partner();
        p.setNombre("Alex Gym");
        p.setEmail("alex" + System.currentTimeMillis() + "@test.com");
        // p.setActivo(true); // Si tienes este campo

        return partnerRepository.save(p);
    }
}