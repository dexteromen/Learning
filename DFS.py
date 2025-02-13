def dfs(graph, start):
    visited = set()  # Keep track of visited nodes
    order_of_visit = []  # To store the order of visited nodes
    
    def dfs_recursive(node):
        visited.add(node)
        order_of_visit.append(node)
        
        # Explore all neighbors of the current node
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs_recursive(neighbor)

    # Start DFS traversal
    dfs_recursive(start)
    
    return order_of_visit

# Example graph (undirected)
graph_dfs = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Example usage of DFS
start_node_dfs = 'A'
dfs_result = dfs(graph_dfs, start_node_dfs)
print(f"DFS traversal starting from {start_node_dfs}: {dfs_result}")
# Output: DFS traversal starting from A: ['A', 'B', 'D', 'E', 'F', 'C']




def dfs_stack(graph, start):
    visited = set()
    stack = [start]
    order_of_visit = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            order_of_visit.append(node)
            # Push neighbors to the stack (reverse the order for proper traversal)
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

    return order_of_visit

# Example usage of non-recursive DFS
dfs_stack_result = dfs_stack(graph_dfs, start_node_dfs)
print(f"Non-recursive DFS traversal starting from {start_node_dfs}: {dfs_stack_result}")
# Output: Non-recursive DFS traversal starting from A: ['A', 'C', 'F', 'E', 'B', 'D']