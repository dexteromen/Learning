from collections import deque

def bfs(graph, start):
    visited = set()  # Keep track of visited nodes
    order_of_visit = []  # To store the order of visited nodes
    
    queue = deque([start])  # Use a queue to explore the nodes
    visited.add(start)

    while queue:
        node = queue.popleft()  # Remove the node from the queue
        order_of_visit.append(node)
        
        # Explore all neighbors of the current node
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order_of_visit

# Example graph (undirected)
graph_bfs = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Example usage of BFS
start_node_bfs = 'A'
bfs_result = bfs(graph_bfs, start_node_bfs)
print(f"BFS traversal starting from {start_node_bfs}: {bfs_result}")
# Output: BFS traversal starting from A: ['A', 'B', 'C', 'D', 'E', 'F']
