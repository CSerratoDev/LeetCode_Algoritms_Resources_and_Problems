package com.gym.system_gestion.controller;

import com.gym.system_gestion.model.Partner;
import com.gym.system_gestion.repository.PartnerRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller; // Ojo: ya no es RestController
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Controller // Esto dice: "Yo controlo pantallas HTML"
public class PartnerWebController {

    @Autowired
    private PartnerRepository partnerRepository;

    @GetMapping("/inicio")
    public String login(){
        return "login";
    }

    @GetMapping("/socios") // URL: localhost:8080/socios
    public String listarSocios(Model model, @RequestParam(name = "palabraClave", required = false) String palabraClave) {
        List<Partner> listaSocios;
        if (palabraClave != null && !palabraClave.isEmpty()) {
            // Si hay palabra clave, usamos nuestro buscador mágico
            listaSocios = partnerRepository.findByNombreContainingIgnoreCase(palabraClave);
        } else {
            // Si no hay nada, traemos todo (como antes)
            listaSocios = partnerRepository.findAll();
        }

        model.addAttribute("partners", listaSocios);
        model.addAttribute("palabraClave", palabraClave); // Para mantener el texto en la cajita

        return "lista-socios";
    }
    // 1. Mostrar el formulario vacío
    @GetMapping("/socios/nuevo")
    public String mostrarFormularioRegistro(Model model) {
        // Pasamos un objeto vacío para que el formulario lo llene
        model.addAttribute("partner", new Partner());
        return "registro-socio"; // Este será el nuevo archivo HTML
    }

    // 2. Recibir los datos y guardarlos
    @PostMapping("/socios/guardar")
    public String guardarSocio(@ModelAttribute("partner") Partner partner) {
        // Spring mete automáticamente los datos del HTML en el objeto 'partner'
        partnerRepository.save(partner);

        // Al terminar, redirigimos al usuario a la lista para que vea su nuevo socio
        return "redirect:/socios";
    }
    // 3. EDITAR: Mostrar el formulario con los datos cargados
    @GetMapping("/socios/editar/{id}")
    public String mostrarFormularioEditar(@PathVariable Long id, Model model) {
        // Buscamos al socio por ID, si no existe lanzamos error (o null)
        Partner partner = partnerRepository.findById(id)
                .orElseThrow(() -> new IllegalArgumentException("ID invalido: " + id));

        model.addAttribute("partner", partner);

        // ¡Usamos el MISMO HTML de registro! No hace falta crear otro.
        // Como el objeto 'partner' ya tiene datos, los inputs aparecerán llenos.
        return "registro-socio";
    }

    // 4. ELIMINAR: Borrar socio y volver a la lista
    @GetMapping("/socios/eliminar/{id}")
    public String eliminarSocio(@PathVariable Long id) {
        partnerRepository.deleteById(id);
        return "redirect:/socios";
    }
}