package JavaMastery.Templates.Builder;

@Service
public class ProductoService {
    @Autowired
    private ProductoRepository repositorio;

    public Producto guardaProducto(ProductoRequest request) {
        Producto producto = Producto.builder()
            .nombre(request.nombre())
            .precio(request.precio())
            .categoria(request.categoria())
            .stock(request.stock())
            .build();

        return repositorio.save(producto);
    }
}
