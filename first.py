#Create adjacency list
def adjacency_list_dictionary(V,edges):
    adj_list ={}
    # Add vertices to the dictionary
    for v in range(V):
        adj_list[v] = []

    # Add edges to the dictionary
    for e in edges:
        u,v = e #u = e[0] , v = e[1]
        # For undirected graph
        adj_list[u].append(v)
        adj_list[v].append(u) 
    return adj_list

#crete example for graph
V = 6
edges = [(0,1),(0,2),(1,3),(1,4),(2,4),(3,5),(4,5)]
graph = adjacency_list_dictionary(V,edges)


def create_adj_matrix(V,edges):
    matrix = [[0]*V for i in range(V)]

    for edge in edges:
        u ,v = edge
        matrix[u][v] =1
        matrix[v][u] =1
    
    return matrix

# Example
v1 = 3 
edges1 = [(0,1),(1,2),(2,0)]
adj_matrix1 = create_adj_matrix(v1,edges1)
adj_list1 = adjacency_list_dictionary(v1,edges1)   
for row in adj_matrix1:
    print(row)
print()

for key in adj_list1:
    print(key, adj_list1[key])
print()

v2 = 4 
edges2 = [(0,1),(1,2),(1,3),(2,3),(3,0)]
adj_matrix2 = create_adj_matrix(v2,edges2)
adj_list2 = adjacency_list_dictionary(v2,edges2)   
for row in adj_matrix2:
    print(row)
print()

for key in adj_list2:
    print(key, adj_list2[key])
print()

















######################################################################
from collections import defaultdict

# Default is 0 for missing keys
d = defaultdict(int)

d['a'] = 5
print(d['a'])  # Output: 5
print(d['b'])  # Output: 0 (default value, since 'b' doesn't exist)

######################################################################
from collections import defaultdict

# Default is an empty list for missing keys
d = defaultdict(list)

d['a'].append(1)
d['a'].append(2)
d['b'].append(3)

print(d)  # Output: defaultdict(<class 'list'>, {'a': [1, 2], 'b': [3]})


######################################################################
from collections import defaultdict

# Default is an empty set for missing keys
d = defaultdict(set)

d['a'].add(1)
d['b'].add(2)

print(d)  # Output: defaultdict(<class 'set'>, {'a': {1}, 'b': {2}})

######################################################################
from collections import defaultdict

# Default is 'unknown' for missing keys
def default_value():
    return "unknown"

d = defaultdict(default_value)

print(d['a'])  # Output: unknown
print(d['b'])  # Output: unknown

######################################################################
from collections import defaultdict

data = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']

# Using defaultdict to count the frequency of elements
counter = defaultdict(int)

for item in data:
    counter[item] += 1

print(counter)  # Output: defaultdict(<class 'int'>, {'apple': 2, 'banana': 3, 'orange': 1})
######################################################################
