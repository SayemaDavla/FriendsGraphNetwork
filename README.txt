This project analyzed a social media friendship network to reveal how users are interconnected. 
It allows you to:

- Find the most closely related nodes with the highest number of edges
- Find the least connected nodes with the fewest edges
- Find shortest paths between two users, to understand how they are connected.
- Identify the sets of nodes that are internally reachable from each other
- Retrieve stats about a given user
- Mutual Friends Between Two Nodes
- Closest Connected Nodes to a Given Node
- Community Detection
- Visualize the Network


**Interaction / Prompts:**
- "Find most connected node": returns the user with the highest number of friends.
- "Find least connected nodes": lists users with the fewest friendships.
- "Shortest path between [User A] and [User B]": prints the number of edges in the shortest path.
- "Mutual friends between [User A] and [User B]": returns a set of users who are friends with both.
- "Node stats for [User]": prints the degree 
- "Most similar nodes to [User]": prints nodes closest in terms of path length.

**Program Response:**
In response to these commands, the program prints the requested information directly to the console.  
The code uses NetworkX for graph operations, and matplotlib for visualization.

**Special Instructions:**
You must have Python 3.x installed along with the following packages:
- networkx
- matplotlib
- community (python-louvain)

No external API keys are needed.  
Ensure that `graph_nodes.txt` (the dataset edges list) is in the same directory as the code files.

**Data Structure:**
- Nodes represent users (unique user IDs).
- Edges represent friendships between these users.
