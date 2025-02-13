from collections import deque

def bfs(adj_matrix, start, nodes):
    visited = set()  # Keep track of visited nodes
    order_of_visit = []  # To store the order of visited nodes
    
    queue = deque([start])  # Use a queue to explore the nodes
    visited.add(start)

    while queue:
        node = queue.popleft()  # Remove the node from the queue
        order_of_visit.append(nodes[node])  # Append the node to the visit order
        
        # Explore all neighbors of the current node
        for neighbor in range(len(adj_matrix)):
            if adj_matrix[node][neighbor] == 1 and neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order_of_visit

# Example adjacency matrix (undirected)
# The matrix represents the following graph:
# A - B, A - C, B - D, B - E, C - F, E - F

adj_matrix = [
    [0, 1, 1, 0, 0, 0],  # A
    [1, 0, 0, 1, 1, 0],  # B
    [1, 0, 0, 0, 0, 1],  # C
    [0, 1, 0, 0, 0, 0],  # D
    [0, 1, 0, 0, 0, 1],  # E
    [0, 0, 1, 0, 1, 0],  # F
]

# Mapping of indices to node names
nodes = ['A', 'B', 'C', 'D', 'E', 'F']

# Example usage of BFS
start_node_bfs = 0  # Start node index (A corresponds to index 0)
bfs_result = bfs(adj_matrix, start_node_bfs, nodes)

print(f"BFS traversal starting from {nodes[start_node_bfs]}: {bfs_result}")
# Output: BFS traversal starting from A: ['A', 'B', 'C', 'D', 'E', 'F']