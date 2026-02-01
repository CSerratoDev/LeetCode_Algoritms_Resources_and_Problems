package com.gym.system_gestion.controller;

import com.gym.system_gestion.model.Partner;
import com.gym.system_gestion.repository.PartnerRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

@Controller
public class PartnerWebController {

    @Autowired
    private PartnerRepository partnerRepository;

    @GetMapping("/socios")
    public String listarSocios(
            Model model,
            @RequestParam(name = "palabraClave", required = false) String palabraClave,
            @RequestParam(name = "page", defaultValue = "0") int page
        ) {

            Pageable pageable = PageRequest.of(page, 8);

            Page<Partner> listaSocios;

            if (palabraClave != null && !palabraClave.isEmpty()) {
                listaSocios = partnerRepository.findByNombreContainingIgnoreCase(palabraClave, pageable);
            } else {
                listaSocios = partnerRepository.findAll(pageable);
            }
        model.addAttribute("partners", listaSocios);
        model.addAttribute("palabraClave", palabraClave);
        model.addAttribute("totalItems", listaSocios.getTotalElements());
        model.addAttribute("totalPages", listaSocios.getTotalPages());
        model.addAttribute("currentPage", page);

        return "lista-socios";
    }
    @GetMapping("/socios/nuevo")
    public String mostrarFormularioRegistro(Model model) {
        model.addAttribute("partner", new Partner());
        return "registro-socio";
    }

    @PostMapping("/socios/guardar")
    public String guardarSocio(@ModelAttribute("partner") Partner partner) {
        partnerRepository.save(partner);

        return "redirect:/socios";
    }
    @GetMapping("/socios/editar/{id}")
    public String mostrarFormularioEditar(@PathVariable Long id, Model model) {
        Partner partner = partnerRepository.findById(id)
                .orElseThrow(() -> new IllegalArgumentException("ID invalido: " + id));

        model.addAttribute("partner", partner);

        return "registro-socio";
    }

    @GetMapping("/socios/eliminar/{id}")
    public String eliminarSocio(@PathVariable Long id) {
        partnerRepository.deleteById(id);
        return "redirect:/socios";
    }
}