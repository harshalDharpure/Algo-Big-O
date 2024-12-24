# Vertices and their indices
vertices = ['A', 'B', 'C', 'D', 'E', 'F']
vertex_indices = { 'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5 }
 
# The adjacency matrix
adjacency_matrix = [
    [0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1],
    [0, 1, 0, 1, 1, 0],
    [0, 0, 1, 0, 1, 0],
    [0, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 1, 0]
]
 
def travBFS(graph, start):
    visited = {}
    queue = [start]
    output = []
    visited[start] = True
 
    while len(queue) > 0:
        current = queue.pop(0)
        output.append(current)
        current_idx = vertex_indices[current]
 
        neighbours = graph[current_idx]
        for i in range(len(neighbours)):
            if neighbours[i] == 1 and vertices[i] not in visited:
                queue.append(vertices[i])
                visited[vertices[i]] = True
 
    return output