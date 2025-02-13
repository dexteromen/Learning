import heapq

def prim(graph, start):
    # Initialize the priority queue with the start node
    pq = [(0, start)]  # (edge weight, node)
    
    # Initialize data structures
    in_mst = set()  # Set of nodes included in the MST
    mst_edges = []  # List to store the edges in the MST
    total_weight = 0  # Total weight of the MST
    
    while pq:
        # Get the node with the smallest edge weight
        weight, node = heapq.heappop(pq)
        
        # If the node is already in the MST, skip it
        if node in in_mst:
            continue
        
        # Add the node to the MST
        in_mst.add(node)
        total_weight += weight
        
        # If this edge is not the starting node (weight > 0), record it
        if weight > 0:
            mst_edges.append((prev_node, node, weight))
        
        # Explore all the neighbors of the current node
        for neighbor, edge_weight in graph[node].items():
            if neighbor not in in_mst:
                heapq.heappush(pq, (edge_weight, neighbor))
                prev_node = node
    
    return mst_edges, total_weight

# Example graph represented as an adjacency list
# The graph is a dictionary where the keys are nodes, and the values are dictionaries 
# of neighboring nodes with the associated edge weights.
graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'A': 1, 'C': 3, 'D': 6},
    'C': {'A': 3, 'B': 3, 'D': 4, 'E': 6},
    'D': {'B': 6, 'C': 4, 'E': 2},
    'E': {'C': 6, 'D': 2}
}

# Example usage of Prim's algorithm
start_node = 'A'
mst_edges, total_weight = prim(graph, start_node)

print(f"Edges in the Minimum Spanning Tree: {mst_edges}")
print(f"Total weight of the Minimum Spanning Tree: {total_weight}")
# Output: Edges in the Minimum Spanning Tree: [('A', 'B', 1), ('B', 'C', 3), ('C', 'D', 4), ('D', 'E', 2)]