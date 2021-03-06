import matplotlib.pyplot as plt
import networkx as nx


def save_graph(graph: nx.DiGraph, path: str) -> None:
    """
    Saves the graph using networkx drawing

    Parameters
    --------------------------------------
    graph: nx.DiGraph
        Graph to be saved
    path: str
        Path and name of the file to be saved
    """
    plt.figure(figsize=(20, 20))

    pos = nx.spring_layout(graph)
    nx.draw_networkx_edges(graph, pos, width=2, arrowsize=30)
    nx.draw_networkx_edge_labels(graph, pos, font_size=25, edge_labels=nx.get_edge_attributes(graph, 'weight'))
    nx.draw_networkx_nodes(graph, pos, node_size=[len(v) * 1000 for v in graph.nodes()])
    nx.draw_networkx_labels(graph, pos, font_size=20, font_family='sans-serif')

    plt.axis('off')
    plt.tight_layout()
    plt.savefig(path)
    plt.close()


def save_graphviz(graph: nx.DiGraph, path: str) -> None:
    """
    Converts the networkx graph to a graphviz format and saves accordingly

    Parameters
    --------------------------------------
    graph: nx.DiGraph
        Graph to be saved
    path: str
        Path and name of the file to be saved
    """
    try:
        graph = nx.nx_agraph.to_agraph(graph)
        graph.node_attr.update()
        # graph.node_attr.update(style='filled', fillcolor='#40e0d0')
        graph.graph_attr.update(bgcolor='transparent')
        graph.layout('dot')
        graph.draw(f'{path}.png')

        # graph = nx.drawing.nx_pydot.to_pydot(graph)
        # graph.write_png(f'{path}.png')
    except Exception:
        save_graph(graph, path)