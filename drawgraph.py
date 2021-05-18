import os
from datetime import datetime
import matplotlib.pyplot as plt
import networkx as nx


# bunch of constants
# graph key related
CONNECTION_KEY = "connects_to"
COLOR_KEY = "color"

# color palletes
EDGE_COLOR = "#000000"
ROUTE_COLOR = "#0000FFFF"
TRANSPARENT = "#00000000"
BACKGROUND_COLOR = "#999999"
HIGHLIGHT_COLOR = "#00FFFB"

# file stuff
OUTPUT_DIR = "output/"
DATETIME_FORMAT = "%Y_%m_%d-%H:%M:%S"
OUTPUT_DPI = 300


def draw_graph(title, graph, route=None, stops=None, stopString=None):
    G = nx.DiGraph()
    edges = []
    node_colors = []
    edge_colors = []

    for node in graph:
        # transform graph notation into a set of tuples representing
        # the edges

        for connection in graph[node][CONNECTION_KEY]:

            if connection != '':
                edges.append((node, connection))

    # Append edges to graph G
    G.add_edges_from(edges)

    # generating color map for nodes
    for node in G.nodes:
        node_colors.append(graph[node][COLOR_KEY])

    # generating color map for edges
    for edge in G.edges:
        for i in range(0, len(route)-1):
            path = False
            if route[i] == edge[0] and route[i+1] == edge[1]:
                edge_colors.append(ROUTE_COLOR)
                path = True
                break
        if not path:
            edge_colors.append(EDGE_COLOR)

    # Instance fig (actual image file)
    fig = plt.figure()

    # set fig title
    plt.title(stopString)

    # Set the route on graph G
    nx.add_path(G, route)

    # Set graph layout
    pos = nx.spring_layout(G)

    # Draw base graph
    nx.draw(G, with_labels=True, node_color=node_colors,
            edge_color=edge_colors, pos=pos)

    # Draw actual route on top of previous graph
    nx.draw(G.subgraph(stops), pos=pos, node_color=TRANSPARENT,
            with_labels=True, font_color=HIGHLIGHT_COLOR, edge_color=TRANSPARENT)

    # background color
    fig.set_facecolor(BACKGROUND_COLOR)

    # Save file
    try:
        os.makedirs(OUTPUT_DIR)

    except FileExistsError:
        pass
    try:
        savedir = OUTPUT_DIR+title+"_"+datetime. now().strftime(DATETIME_FORMAT)
        plt.savefig(savedir, dpi=OUTPUT_DPI)
    except:
        print("Error writing output result!")
