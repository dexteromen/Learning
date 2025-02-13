from collections import defaultdict

# Step 1: Perform DFS and store the vertices in the order of their finishing times
def dfs(graph, node, visited, stack):
    visited.add(node)
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, stack)
    
    stack.append(node)  # Store the node in the stack when finished

# Step 2: Reverse the graph
def reverse_graph(graph):
    reversed_graph = defaultdict(list)
    
    for node in graph:
        for neighbor in graph[node]:
            reversed_graph[neighbor].append(node)
    
    return reversed_graph

# Step 3: Perform DFS on the reversed graph
def dfs_reversed(graph, node, visited, scc):
    visited.add(node)
    scc.append(node)
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_reversed(graph, neighbor, visited, scc)

# Step 4: Kosaraju's algorithm to find strongly connected components (SCCs)
def kosaraju(graph):
    # Step 1: Perform DFS on the original graph and fill the stack
    visited = set()
    stack = []
    
    for node in graph:
        if node not in visited:
            dfs(graph, node, visited, stack)
    
    # Step 2: Reverse the graph
    reversed_graph = reverse_graph(graph)
    
    # Step 3: Perform DFS on the reversed graph and find SCCs
    visited = set()
    sccs = []
    
    while stack:
        node = stack.pop()
        if node not in visited:
            scc = []
            dfs_reversed(reversed_graph, node, visited, scc)
            sccs.append(scc)
    
    return sccs

# Example usage
graph = {
    'A': ['B'],
    'B': ['C'],
    'C': ['A', 'D'],
    'D': ['E'],
    'E': ['D']
}

sccs = kosaraju(graph)

print("Strongly Connected Components (SCCs):")
for idx, scc in enumerate(sccs, 1):
    print(f"SCC {idx}: {scc}")

# A -> B
# B -> C
# C -> A, D
# D -> E
# E -> D

# Strongly Connected Components (SCCs):
# SCC 1: ['A', 'B', 'C']
# SCC 2: ['D', 'E']


# Explanation of Output:
# The nodes A, B, and C form one SCC because they are mutually reachable.
# The nodes D and E form another SCC because they are mutually reachable.
# The graph is divided into 2 strongly connected components.
# Time Complexity:
# DFS is performed twice (once on the original graph and once on the reversed graph), and both DFS runs take O(V + E) time.
# Hence, the total time complexity of Kosaraju's algorithm is O(V + E), which is efficient for large graphs.