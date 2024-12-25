# Time complexity explanation:

# The time complexity is O(V+E), where V is the number of vertices and E is the number of edges.

# Creating the adjacency list will take O(E) time as we're iterating over all edges.

# DFS itself also has a time complexity of O(V+E) because we're visiting every vertex once and checking all their neighbours (which corresponds to the edges).

# Space complexity explanation:

# The space complexity is O(V+E).

# The adjacency list will take O(V+E) space. This is because we have a separate list for each vertex, and the total length of all lists is twice the number of edges (since each edge contributes to 2 vertices).

# The visited dictionary will take O(V) space as it could potentially store all vertices.

# There is also additional O(V) space required for the call stack in the case of a DFS on a connected graph.

# So, overall, the space complexity is O(V+E).



def build_adj_list(n, edges):
    # Initialize adjacency list with empty lists for each vertex
    adj_list = [[] for _ in range(n)]
    
    # Add edges to adjacency list
    for edge in edges:
        node1 = edge[0]  # first node of edge
        node2 = edge[1]  # second node of edge
        adj_list[node1].append(node2)
        adj_list[node2].append(node1)
    
    return adj_list
 
def dfs(graph, vertex, visited):
    # Mark vertex as visited
    visited[vertex] = True
    
    # Get neighbors of current vertex
    neighbors = graph[vertex]
    
    # Visit all unvisited neighbors
    for neighbor in neighbors:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
 
def count_components(n, edges):
    # Build adjacency list
    graph = build_adj_list(n, edges)
    
    # Initialize visited set
    visited = {}
    
    count = 0
    for vertex in range(n):
        if vertex not in visited:
            count += 1
            dfs(graph, vertex, visited)
    
    return count
 
n = 7  # vertices 0, 1, 2, 3, 4, 5, 6
edges = [[0,1],[1,2],[3,4],[5,6]]
print(count_components(n, edges))