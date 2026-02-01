package com.gym.system_gestion.controller;

import com.gym.system_gestion.model.Partner;
import com.gym.system_gestion.repository.PartnerRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/partners")
public class PartnerController {

    @Autowired
    private PartnerRepository partnerRepository;

    @GetMapping
    public List<Partner> getAllPartners() {
        return partnerRepository.findAll();
    }

    @GetMapping("/crear-demo")
    public Partner createDemoPartner() {
        Partner p = new Partner();
        p.setNombre("Alex Gym");
        p.setEmail("alex" + System.currentTimeMillis() + "@test.com");

        return partnerRepository.save(p);
    }
}