import heapq

def dijkstra(graph, start):
    # Create a priority queue for the vertices to explore, initialized with the start node
    queue = [(0, start)]  # (distance, node)
    
    # Initialize distances with infinity
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Store the previous node in the shortest path
    previous_nodes = {node: None for node in graph}
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)  # Get the node with the smallest distance
        
        # If the distance of the current node is greater than the current known distance, skip it
        if current_distance > distances[current_node]:
            continue
        
        # Explore each neighbor of the current node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # If a shorter path to the neighbor is found, update the distance and add to the priority queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))
    
    return distances, previous_nodes

def shortest_path(previous_nodes, start, end):
    path = []
    current_node = end
    while current_node is not None:
        path.insert(0, current_node)
        current_node = previous_nodes[current_node]
    return path

# Example graph represented as an adjacency list:
# The graph is a dictionary where each key is a node and the value is another dictionary
# with the neighboring node as the key and the edge weight as the value
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Example usage of Dijkstra's algorithm
start_node = 'A'
end_node = 'D'

# Run Dijkstra's algorithm
distances, previous_nodes = dijkstra(graph, start_node)

# Output the shortest distance from start to each node
print("Shortest distances from start node:", distances)

# Get the shortest path from start to end
path = shortest_path(previous_nodes, start_node, end_node)
print(f"The shortest path from {start_node} to {end_node} is:", path)
