# Define the adjacency list of the graph
adjacency_list = {
    'A': ['B', 'F'],
    'B': ['A', 'C'],
    'C': ['B', 'E', 'D'],
    'D': ['C', 'E'],
    'E': ['D', 'C', 'F'],
    'F': ['A', 'E']
}
 
# Recursive function for Depth-first search (DFS)
def trav_recursive_DFS(graph, vertex, output, visited):
    # Append the current vertex to the output
    output.append(vertex)
 
    # Mark the current vertex as visited
    visited[vertex] = True
 
    # Get all neighbors of the current vertex
    neighbours = graph[vertex]
 
    # For each neighbor of the current vertex
    for neighbour in neighbours:
        # If the neighbor has not been visited yet
        if neighbour not in visited:
            # Recursively perform DFS on the neighbor
            trav_recursive_DFS(graph, neighbour, output, visited)
 
    # Return the output list
    return output