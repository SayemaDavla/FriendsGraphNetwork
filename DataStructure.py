import networkx as nx
import community
import matplotlib.pyplot as plt

def find_most_connected_node(G):
    """
    Return the node with the highest degree (most edges) in the graph G.

    Parameters:
        G (networkx.Graph): The graph to analyze.

    Returns:
        tuple: (node, degree) representing the most connected node and its degree.
    """
    degrees = G.degree()
    most_connected_node, degree = max(degrees, key=lambda x: x[1])
    return most_connected_node, degree

def least_connected_nodes(G):
    """
    Return the nodes with the smallest degree (least edges) in the graph G,
    along with that minimum degree value.

    Parameters:
        G (networkx.Graph): The graph to analyze.

    Returns:
        (list, int): A list of nodes with the minimum degree and the minimum degree value.
    """
    degrees = dict(G.degree())
    min_degree = min(degrees.values())
    min_degree_nodes = [node for node, degree in degrees.items() if degree == min_degree]
    return min_degree_nodes, min_degree

def closely_connected_nodes(G, node):
    """
    Print the nodes closest to a given node based on shortest path length.

    Parameters:
        G (networkx.Graph): The graph to analyze.
        node (str): The node of interest.
    """
    node_of_interest = node
    lengths = nx.single_source_shortest_path_length(G, node_of_interest)
    if node_of_interest in lengths:
        del lengths[node_of_interest]
    sorted_nodes = sorted(lengths.items(), key=lambda x: x[1])

    print("Friends closest to the node of interest based on shortest path length:")
    for n, distance in sorted_nodes[:10]:
        print(f"Friend: {n}, Distance: {distance}")

def shortest_path(G, source_node, target_node):
    """
    Compute the shortest path length between two nodes if the graph is connected.

    Parameters:
        G (networkx.Graph): The graph to analyze.
        source_node (str): The starting node.
        target_node (str): The target node.

    Returns:
        int or None: The shortest path length if it exists, otherwise None.
    """
    try:
        length = nx.shortest_path_length(G, source=source_node, target=target_node)
        return length
    except nx.NetworkXNoPath:
        return None
    except nx.NodeNotFound:
        return None

def connected_components(G):
    """
    Return the connected components of the graph.

    Parameters:
        G (networkx.Graph): The graph to analyze.

    Returns:
        list of sets: Each set contains the nodes of a connected component.
    """
    components = list(nx.connected_components(G))
    return components

def node_stats(G, node):
    """
    Return statistics about a given node, including its degree and optional profile link.

    Parameters:
        G (networkx.Graph): The graph to analyze.
        node (str): The node of interest.

    Returns:
        dict: A dictionary with 'degree' and optionally 'profile_link' keys.
    """
    stats = {}
    stats['degree'] = G.degree(node)
    if 'profile_link' in G.nodes[node]:
        stats['profile_link'] = G.nodes[node]['profile_link']
    return stats

def mutual_friends(G, node1, node2):
    """
    Find mutual friends between two given nodes.

    Parameters:
        G (networkx.Graph): The graph to analyze.
        node1 (str): First node.
        node2 (str): Second node.

    Returns:
        set: A set of nodes that are neighbors of both node1 and node2.
    """
    neighbors1 = set(G.neighbors(node1))
    neighbors2 = set(G.neighbors(node2))
    print(f'This is neighbor1: {neighbors1}')
    print(f'This is neighbor2: {neighbors2}')
    mutuals = neighbors1 & neighbors2
    return mutuals

def community_detection(G):
    """
    Perform community detection on the graph using the Louvain method and plot the result.

    Parameters:
        G (networkx.Graph): The graph to analyze.

    Returns:
        dict: A partition dictionary mapping nodes to community IDs.
    """
    partition = community.best_partition(G)
    pos = nx.spring_layout(G, k=0.5, iterations=50)
    plt.figure(figsize=(15, 15))
    num_communities = max(partition.values()) + 1
    cmap = plt.get_cmap('viridis', num_communities)
    node_colors = [partition[node] for node in G.nodes()]
    node_sizes = [200 for _ in G.nodes()]
    labels = {node: node for node in G.nodes()}
    nx.draw_networkx(
        G,
        pos,
        labels=labels,
        with_labels=True,
        node_size=node_sizes,
        font_size=10,
        node_color=node_colors,
        cmap=cmap,
        edge_color='gray'
    )

    sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=0, vmax=num_communities - 1))
    sm.set_array([])
    cbar = plt.colorbar(sm, cax=plt.axes([0.95, 0.1, 0.03, 0.8]))
    cbar.set_label('Community')
    plt.title('Community Detection')
    return partition

def plot_graph(G):
    """
    Plot the entire graph with nodes and edges using a spring layout.

    Parameters:
        G (networkx.Graph): The graph to plot.
    """
    pos = nx.spring_layout(G)
    plt.figure(figsize=(15, 15))
    node_sizes = [200 for _ in G.nodes()]
    labels = {node: node for node in G.nodes()}

    nx.draw_networkx(
        G,
        pos,
        labels=labels,
        with_labels=True,
        node_size=node_sizes,
        font_size=10,
        edge_color='gray'
    )
    plt.title('Friends Graph')

def plot_both_graphs(G):
    """
    Plot community detection result. Placeholder for extending additional plots.
    
    Parameters:
        G (networkx.Graph): The graph to plot.
    """
    communities = community_detection(G)

def build_graph_from_file(file_path):
    """
    Build a graph from an edge list file.

    Parameters:
        file_path (str): The path to the edge list file.

    Returns:
        networkx.Graph: The constructed graph object.
    """
    G = nx.Graph()
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('%'):
                continue  
            parts = line.split()
            if len(parts) < 2:
                continue 
            user1, user2 = parts[0], parts[1]
            G.add_edge(user1, user2)
    return G
