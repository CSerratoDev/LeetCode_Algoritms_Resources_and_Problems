import networkx as nx
import matplotlib.pyplot as plt


def leer_archivo_entradas(ruta: str):
    """
    Lee un archivo de texto con las entradas necesarias para la máquina de Moore.
    Formato esperado:
        Línea 1: alfabeto de entrada (ejemplo: abcñ)
        Línea 2: desplazamiento entero (ejemplo: 3)
    """
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            lineas = [line.strip().lower() for line in f.readlines() if line.strip()]

        if len(lineas) < 2:
            print("El archivo debe tener al menos 2 líneas (alfabeto y desplazamiento).")
            return None, None

        entrada = lineas[0]
        try:
            n = int(lineas[1])
        except ValueError:
            print("El desplazamiento debe ser un número entero válido.")
            return None, None

        return entrada, n

    except FileNotFoundError:
        print(f"No se encontró el archivo: {ruta}")
        return None, None
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None, None


def generar_maquina_moore(entrada=None, n=None):
    """Genera y guarda la descripción de una máquina de Moore en un archivo de texto."""
    alfabeto_espanol = list("abcdefghijklmnñopqrstuvwxyz")

    #Si no se pasa entrada, pedirla manualmente
    if entrada is None or n is None:
        entrada = input("Ingrese un alfabeto de entrada (ej: abcñ): ").strip().lower()
        if not entrada:
            print("La cadena es nula.")
            return

        for c in entrada:
            if c not in alfabeto_espanol:
                print(f"Carácter no válido: {c}")
                return

        try:
            n = int(input("Ingrese un desplazamiento n: "))
        except ValueError:
            print("El desplazamiento debe ser un número entero.")
            return

    #Calcular alfabeto desplazado
    desplazado = []
    for c in entrada:
        idx = alfabeto_espanol.index(c)
        nuevo_idx = (idx + n) % len(alfabeto_espanol)
        desplazado.append(alfabeto_espanol[nuevo_idx])

    #Definir componentes de la máquina de Moore
    Q = [f"q{i}" for i in range(len(entrada))]
    Σ = list(entrada)
    δ = {}
    λ = {}
    q0 = "q0"
    Γ = list(desplazado)

    #Construcción de funciones δ y λ
    for i, simbolo in enumerate(Σ):
        δ[(f"q{i}", simbolo)] = f"q{(i + 1) % len(Q)}"
        λ[f"q{i}"] = desplazado[i]

    #Generar contenido del archivo
    contenido = []
    contenido.append("=== MÁQUINA DE MOORE ===\n")
    contenido.append(f"Q (Estados) = {Q}\n")
    contenido.append(f"Σ (Alfabeto) = {Σ}\n")
    contenido.append(f"Γ (Transición) = {Γ}\n")
    contenido.append(f"q₀ (Estado inicial) = {q0}\n\n")

    contenido.append("=== FUNCIÓN DE TRANSICIÓN δ(q, a) ===\n")
    for (estado, simbolo), siguiente in δ.items():
        contenido.append(f"δ({estado}, '{simbolo}') → {siguiente}\n")

    contenido.append("\n=== FUNCIÓN DE SALIDA λ(q) ===\n")
    for estado, salida in λ.items():
        contenido.append(f"λ({estado}) → '{salida}'\n")

    #Guardar archivo txt
    with open("maquina_moore.txt", "w", encoding="utf-8") as f:
        f.writelines(contenido)

    print("\nArchivo 'maquina_moore.txt' generado con éxito.")
    print("Alfabeto original:", Σ)
    print("Alfabeto desplazado:", Γ)

    # Dibujar grafo de transiciones
    dibujar_grafo_moore(δ, λ, q0)


def dibujar_grafo_moore(delta: dict, lambda_func: dict, estado_inicial: str):
    """
    Dibuja el grafo de transiciones de la máquina de Moore usando NetworkX.
    Los nodos representan estados, y las aristas las transiciones δ(q, a).
    """
    G = nx.DiGraph()

    # Agregar nodos con etiquetas (estado y salida λ)
    for estado, salida in lambda_func.items():
        etiqueta_estado = f"{estado}\nλ={salida}"
        G.add_node(estado, label=etiqueta_estado)

    # Agregar aristas según δ(q, a)
    for (estado, simbolo), siguiente in delta.items():
        G.add_edge(estado, siguiente, label=simbolo)

    pos = nx.circular_layout(G)  # disposición circular para claridad visual

    # Dibujar nodos
    nx.draw_networkx_nodes(G, pos, node_color="#7FB3D5", node_size=1500, edgecolors="black")

    # Dibujar etiquetas de estados
    etiquetas = nx.get_node_attributes(G, 'label')
    nx.draw_networkx_labels(G, pos, labels=etiquetas, font_size=9, font_weight="bold")

    # Dibujar aristas con etiquetas
    nx.draw_networkx_edges(G, pos, arrowstyle="->", arrowsize=20, edge_color="gray", width=1.5)
    etiquetas_aristas = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=etiquetas_aristas, font_size=8)

    # Resaltar el estado inicial
    nx.draw_networkx_nodes(G, pos, nodelist=[estado_inicial], node_color="#58D68D", node_size=1600, edgecolors="black")

    plt.title("Diagrama de transiciones - Máquina de Moore", fontsize=12, fontweight="bold")
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    print("=== GENERADOR DE MÁQUINA DE MOORE ===")
    opcion = input("¿Desea leer entradas desde un archivo? (s/n): ").strip().lower()

    if opcion == "s":
        ruta = input("Ingrese el nombre del archivo (ej: entradas.txt): ").strip()
        entrada, n = leer_archivo_entradas(ruta)
        if entrada and n is not None:
            generar_maquina_moore(entrada, n)
    else:
        generar_maquina_moore()
