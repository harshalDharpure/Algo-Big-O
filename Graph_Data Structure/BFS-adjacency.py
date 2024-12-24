# An adjacency list in Python
adjacency_list = {
    'A': ['B', 'F'],
    'B': ['A', 'F', 'C'],
    'C': ['B', 'E', 'D'],
    'D': ['C', 'E'],
    'E': ['D', 'C', 'F'],
    'F': ['A', 'B', 'E']
}
 
def travBFS(graph, start):
    visited = {} # to keep track of visited nodes
    queue = [start] # queue to process nodes
    output = [] # list to save the traversal order
    visited[start] = True
 
    while len(queue) > 0:
        current = queue.pop(0)
        output.append(current)
 
        neighbours = graph[current]
        for neighbour in neighbours:
            if neighbour not in visited:
                queue.append(neighbour)
                visited[neighbour] = True
 
    return output