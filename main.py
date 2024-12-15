from DataStructure import (
    build_graph_from_file,
    find_most_connected_node,
    least_connected_nodes,
    shortest_path,
    connected_components,
    node_stats,
    mutual_friends,
    closely_connected_nodes,
    community_detection,
    plot_graph
)
import matplotlib.pyplot as plt

def main():
    G = build_graph_from_file('graph_nodes.txt')
    
    print("Graph loaded successfully!")
    print("Welcome to the Social Network Analysis Tool.\n")
    print("Available Actions:")
    print("1. Find the most connected node")
    print("2. Find the least connected nodes")
    print("3. Find the shortest path between two nodes")
    print("4. Show connected components")
    print("5. Get stats for a node of interest")
    print("6. Find mutual friends between two nodes")
    print("7. Find friends closest to a node of interest")
    print("8. Detect communities and plot the community graph")
    print("9. Plot the entire graph")
    print("10. Exit\n")

    while True:
        choice = input("Enter the number of the action you want to perform: ")

        if choice == '1':
            most_connected_node, degree = find_most_connected_node(G)
            print(f"The most connected node is '{most_connected_node}' with a degree of {degree}.\n")

        elif choice == '2':
            min_degree_nodes, min_degree = least_connected_nodes(G)
            print(f"Minimum degree is {min_degree}.")
            print(f"Nodes with minimum degree ({min_degree}): {min_degree_nodes}\n")

        elif choice == '3':
            source_node = input("Enter the source node ID: ")
            target_node = input("Enter the target node ID: ")
            length = shortest_path(G, source_node, target_node)
            if length is not None:
                print(f"Shortest path length from {source_node} to {target_node} is {length}.\n")
            else:
                print("No path exists between the specified nodes.\n")

        elif choice == '4':
            components = connected_components(G)
            for i, component in enumerate(components):
                print(f"Component {i + 1}: {component}")
            print()

        elif choice == '5':
            node_of_interest = input("Enter the node ID to get stats: ")
            try:
                stats = node_stats(G, node_of_interest)
                print(f"\nStats for node '{node_of_interest}':")
                print(f" - Degree (number of friends): {stats['degree']}")
                if 'profile_link' in stats:
                    print(f" - Profile link: {stats['profile_link']}")
                print()
            except:
                print("That node does not exist in the graph.\n")

        elif choice == '6':
            node_a = input("Enter the first node ID: ")
            node_b = input("Enter the second node ID: ")
            try:
                mutuals = mutual_friends(G, node_a, node_b)
                print(f"\nMutual friends between '{node_a}' and '{node_b}': {mutuals}\n")
            except:
                print("One or both of these nodes do not exist in the graph.\n")

        elif choice == '7':
            node_interest = input("Enter the node ID of interest: ")
            if node_interest in G.nodes():
                closely_connected_nodes(G, node_interest)
                print()
            else:
                print("That node does not exist in the graph.\n")

        elif choice == '8':
            print("\nDetecting communities in the graph using the Louvain method...")
            communities = community_detection(G)
            print("Communities detected. Displaying community plot...")
            plt.show()
            print()

        elif choice == '9':
            print("\nPlotting the graph...")
            plot_graph(G)
            plt.show()
            print("Graph displayed.\n")

        elif choice == '10':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 10.\n")

if __name__ == "__main__":
    main()
