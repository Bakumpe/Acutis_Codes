# Python/LeetCode/breadthFirstSearch/bfs.py

from collections import deque

def breadthFirstSearch(graph, start):
    visited = {start}
    queue = deque([start])

    while queue:
        node = queue.popleft()
        print(node)  # process the node

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return visited


graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': ['A', 'B', 'D']
}

breadthFirstSearch(graph, 'A')