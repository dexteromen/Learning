from collections import deque

# BFS from given source s
def bfs(adj, s):
    # Create a queue for BFS
    q = deque()
    # Initially mark all the vertices as not visited When we push a vertex into the q, we mark it as visited
    visited = [False] * len(adj)
    # Mark the source node as visited and enqueue it
    visited[s] = True
    q.append(s)
    # Iterate over the queue
    while q:
        # Dequeue a vertex from queue and print it
        curr = q.popleft()
        print(curr, end=" ")
        # Get all adjacent vertices of the dequeued vertex. If an adjacent has not been visited, mark it visited and enqueue it
        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True
                q.append(x)

# DFS Recursive from given source s
def dfs_rec(adj, visited, s):
    # Mark the current vertex as visited
    visited[s] = True

    # Print the current vertex
    print(s, end=" ")

    # Recursively visit all adjacent vertices
    # that are not visited yet
    for i in adj[s]:
        if not visited[i]:
            dfs_rec(adj, visited, i)


def create_adj_list(V,edges):
    adj_list ={}
    for v in range(V):
        adj_list[v] = []

    for e in edges:
        u,v = e
        adj_list[u].append(v)
        adj_list[v].append(u)
    return adj_list


def print_adj_list(adj_list):
    for key in adj_list:
        print(key, ":", adj_list[key])


if __name__ == "__main__":
    V = 8
    edges = [(0,1),(0,2),(0,3),(1,4),(1,5),(2,6),(3,7)] 
    startNode = 0

    #CREATING ADJACENCY LIST
    adj_list = create_adj_list(V,edges)
    print_adj_list(adj_list)

    #PRINTING BFS TRAVERSAL
    print("BFS Traversal:")
    bfs(adj_list,0)
    print()

    #PRINTING DFS TRAVERSAL
    print("DFS Traversal:")
    visited = [False] * V
    dfs_rec(adj_list, visited, 0)
    print()
