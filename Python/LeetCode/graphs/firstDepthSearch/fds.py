# Python/LeetCode/firstDepthSearch/fds.py

def firstDepthSearch(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    print(start)  # process the node

    for neighbor in graph[start]:
        if neighbor not in visited:
            firstDepthSearch(graph, neighbor, visited)

    return visited


graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': ['A', 'B', 'D']
}

firstDepthSearch(graph, 'C')