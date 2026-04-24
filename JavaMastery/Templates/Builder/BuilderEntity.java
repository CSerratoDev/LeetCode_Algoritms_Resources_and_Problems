package JavaMastery.Templates.Builder;
import java.math.BigDecimal;

// Request DTO
public record ProductoRequest(
    String nombre,
    BigDecimal precio,
    String categoria,
    Integer stock
) {}

// Entity
@Entity
@Builder
public class Producto {

    @Id @GeneratedValue
    private Long id;
    private String nombre;
    private BigDecimal precio;
    private String categoria;
    private Integer stock;
}
