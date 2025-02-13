# Topological sort.
# https://www.geeksforgeeks.org/topological-sorting/

# Function to perform DFS and topological sorting
def topologicalSortUtil(v, adj, visited, st):
    
    # Mark the current node as visited
    visited[v] = True

    # Recur for all adjacent vertices
    for i in adj[v]:
        if not visited[i]:
            topologicalSortUtil(i, adj, visited, st)

    # Push current vertex to stack which stores the result
    st.append(v)

# Function to perform Topological Sort
def topologicalSort(adj):
    # Number of vertices
    V = len(adj) 
    
    # Stack to store the result
    st = []
    visited = [False] * V

    # Call the recursive helper function to store
    # Topological Sort starting from all vertices one by one
    for i in range(V):
        if not visited[i]:
            topologicalSortUtil(i, adj, visited, st)
    
    # Append contents of stack and reverse it
    return st[::-1]

if __name__ == "__main__":
    
    # Graph represented as an adjacency list
    adj = [[], [], [3], [1], [0, 1], [0, 2]]

    ans = topologicalSort(adj)
    print( "Topological Sort: ", end="")
    for i in range(len(ans)):
        print(ans[i], end=" ") 
    print()
