import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(G, start):
    dist = {v: float('inf') for v in G.nodes()}
    dist[start] = 0
    visited = set()

    while len(visited) != len(G.nodes()):
        node = None
        node_dist = float('inf')
        for v in dist:
            if v not in visited and dist[v] < node_dist:
                pos = nx.spring_layout(G)
                nx.draw_networkx_nodes(G, pos, node_size=2000, nodelist=None, node_color="tab:orange", alpha=0.75)
                nx.draw_networkx_nodes(G, pos, nodelist=v, node_color="green", alpha=0.75)
                nx.draw_networkx_edges(G, pos, alpha=0.5, width=6)
                nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))
                label_options = {"ec": "k", "fc": "white", "alpha": 0.7}
                nx.draw_networkx_labels(G, pos, font_size=14, bbox=label_options)
                ax = plt.gca()
                ax.margins(0.20)
                plt.axis("off")
                plt.show()
                node = v
                node_dist = dist[v]

        visited.add(node)
        neighbors = set(G.neighbors(node))
        for n in neighbors:
            new_dist = dist[node] + G[node][n]['weight']
            if new_dist < dist[n]:
                dist[n] = new_dist

    return dist

datos=[]
lineas=[]
l=[]
n=[]
nodos=int(input("Ingrese el número de nodos: "))
for i in range(nodos):
    l.append(i)
i=0
with open("in2.txt") as archivo:
    for linea in archivo:
        if i in l:
            lineas.append(linea)
        i=i+1

for i in lineas:
    n.append(i.rstrip('\n'))

Grafo = nx.Graph()
for i in n:
    Grafo.add_node(i)

Grafo.add_edge(n[2], n[1], weight=2)
Grafo.add_edge(n[0], n[1], weight=3)
Grafo.add_edge(n[2], n[0], weight=1)
Grafo.add_edge(n[0], n[3], weight=4)

origen = input("Ingresa un nodo origen: ")
destino = input("Ingresa un nodo destino: ")

distancias = dijkstra(Grafo, origen)
print(f"Distancia más corta desde {origen} a todos los demás nodos: {distancias}")
print(f"Distancia más corta desde {origen} a {destino}: {distancias[destino]}")

ruta_mas_corta = nx.dijkstra_path(Grafo, origen, destino)
print(f"Ruta más corta desde {origen} a {destino}: {ruta_mas_corta}")

pos = nx.spring_layout(Grafo)
nx.draw(Grafo, pos, with_labels=True)
nx.draw_networkx_edge_labels(Grafo, pos, edge_labels=nx.get_edge_attributes(Grafo, 'weight'))

# Dibujar la ruta más corta en rojo
edges = [(ruta_mas_corta[i], ruta_mas_corta[i+1]) for i in range(len(ruta_mas_corta)-1)]
nx.draw_networkx_nodes(Grafo, pos, node_size=2000, nodelist=None, node_color="tab:orange", alpha=0.75)
nx.draw_networkx_nodes(Grafo, pos, nodelist=None, node_color="green", alpha=0.75)
nx.draw_networkx_edges(Grafo, pos, edgelist=edges, edge_color='r', width=3)

plt.show()
