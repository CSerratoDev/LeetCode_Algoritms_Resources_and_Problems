package JavaMastery.Templates.Builder;
import java.math.BigDecimal;

@Builder
public record Producto (
    String nombre,
    BigDecimal precio,
    String categoria,
    Integer stock
) {}

// Como usarlo?
Producto producto = Producto.builder()
    .nombre('pc')
    .precio(new BigDecimal('4000.99'))
    .stock(10)
    .build();