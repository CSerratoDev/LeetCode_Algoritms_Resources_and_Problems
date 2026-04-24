package JavaMastery.Templates.Builder;

@Builder
public class Usuario {
    private String nombre;
    private String edad;
    private String email;
    private String direccion;
}

// Como usar?
Usuario usuario = Usuario.builder()
    .nombre('Ale')
    .edad(26)
    .email('ale@gmail.com')
    .build();