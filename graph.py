import networkx as nx
import matplotlib.pyplot as plt  # Optional for visualization

# Create an empty graph
G = nx.Graph()

# Define coordinates for nodes
node_positions = {
    1: (0, 0),
    2: (1, 1),
    3: (2, 0)
}

# Add nodes with specified coordinates
G.add_nodes_from(node_positions.keys())
nx.set_node_attributes(G, node_positions, 'pos')

# Define edges based on coordinates
edges = [(1, 2), (2, 3), (3, 1)]

# Add edges to the graph
G.add_edges_from(edges)

# Draw the graph with specified node positions
pos = nx.get_node_attributes(G, 'pos')
nx.draw(G, pos, with_labels=True, node_color='skyblue', font_weight='bold')
plt.show()
