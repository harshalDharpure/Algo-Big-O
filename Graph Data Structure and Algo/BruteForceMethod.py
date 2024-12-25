# Part 1: Code with Comments explaining Time Complexity

# Part 2: Code with Comments explaining Space Complexity

# Part 1 -

from collections import deque
 
# Time complexity: O(p) where p is the number of prerequisites.
def buildAdjList(n, prerecs):
    adjList = [[] for _ in range(n)]
    for prerec in prerecs:
        toTake, firstTake = prerec
        adjList[firstTake].append(toTake)
    return adjList
# Final time complexity of buildAdjList: O(n + p)
 
# Time complexity: O(E) where E is the total number of edges in the graph, since in the worst case we will visit all edges once
def checkCycleBFS(vertex, graph):
    queue = deque()
    visited = {}
    for i in range(len(graph[vertex])):
        queue.append(graph[vertex][i])
    while queue:
        curr = queue.popleft()
        visited[curr] = True
        if curr == vertex:
            return True
        neighbours = graph[curr]
        for neighbour in neighbours:
            if neighbour not in visited:
                queue.append(neighbour)
    return False
# Final time complexity of checkCycleBFS: O(E + n) (where n is the number of vertices and E is the number of edges)
 
# Time complexity: O(n*(E+n)), as we run checkCycleBFS for each of the n vertices
def checkIfCanFinish(n, prerecs):
    adjList = buildAdjList(n, prerecs)
    hasCycle = False
    for vertex in range(n):
        hasCycle = checkCycleBFS(vertex, adjList)
        if hasCycle == True:
            return False
    return True
# Final time complexity of checkIfCanFinish: O(n+p + n*(E+n)) = O(p + n^2 + nE)











# Part 2-

from collections import deque
 
# Space complexity: O(n), we are creating an adjacency list of n lists
def buildAdjList(n, prerecs):
    adjList = [[] for _ in range(n)]
    for prerec in prerecs:
        toTake, firstTake = prerec
        adjList[firstTake].append(toTake)
    return adjList
# Final space complexity of buildAdjList: O(n + p), as it needs to store 'p' prerequisites
 
# Space complexity: O(n), as in the worst case scenario, we might end up adding all nodes to the queue.
# Additionally, we are also maintaining a dictionary 'visited' which could contain all the nodes in the worst case.
def checkCycleBFS(vertex, graph):
    queue = deque()
    visited = {}
    for i in range(len(graph[vertex])):
        queue.append(graph[vertex][i])
    while queue:
        curr = queue.popleft()
        visited[curr] = True
        if curr == vertex:
            return True
        neighbours = graph[curr]
        for neighbour in neighbours:
            if neighbour not in visited:
                queue.append(neighbour)
    return False
# Final space complexity of checkCycleBFS: O(n), as queue and visited dictionary can hold at max 'n' vertices.
 
# Space complexity: O(n + E), as we need space for the adjacency list (for storing the prerequisite pairs) and for storing 'n' vertices.
def checkIfCanFinish(n, prerecs):
    adjList = buildAdjList(n, prerecs)
    hasCycle = False
    for vertex in range(n):
        hasCycle = checkCycleBFS(vertex, adjList)
        if hasCycle == True:
            return False
    return True
# Final space complexity of checkIfCanFinish: O(n + E)
 
n=8
prerecs=[[1,0],[2,0],[4,2],[3,2],[1,3],[5,6],[7,5],[7,6]]
print(checkIfCanFinish(n, prerecs))