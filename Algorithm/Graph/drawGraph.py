import matplotlib.pyplot as plt
import networkx as nx

def createGraph(data, special_nodes):
    G = nx.Graph()
    G.add_edges_from(data)

    special_nodes_colors = []

    for node in G.nodes():
        if node in special_nodes:
            special_nodes_colors.append("green")
        else:
            special_nodes_colors.append("blue")

    plt.figure(figsize=(6, 6))
    pos = nx.spring_layout(G, seed=42)

    nx.draw(
        G, 
        pos, 
        with_labels=True, 
        node_size=800, 
        node_color="lightblue",
        font_size=10, 
        font_weight="bold", 
        edge_color="gray"
    )

    plt.title("Graph generated", fontsize=14)
    plt.show()

if __name__ == "__main__":
    data = [
        ("A", "B"),
        ("A", "C"),
        ("B", "D"),
        ("C", "D"),
        ("D", "E"),
    ]

    special_nodes = input("Special Nodes, for example(A,B): ")
    special_nodes = [n.strip() for n in special_nodes.split(",")]

    createGraph(data, special_nodes)