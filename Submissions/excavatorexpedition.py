import sys
from collections import deque

V, E = map(int, sys.stdin.readline().split(" "))

list = sys.stdin.readline().rstrip('\n')

def create_graph(m, n):
    graph = {}
    for i in range(m):
        graph[i] = []
    for i in range(n):
        x, y = map(int, sys.stdin.readline().split(" "))
        graph[x].append(y)
    return graph

def weight( u, v ):
    if v == end:
        return 0
    if list[v] == '.':
        weight = -1
    else:
        weight = 1
    return weight

def iterative_topological_sort(graph, start):
    visited = [False]*V
    stack = []
    ordered = []
    queue = [start]
    while len(queue) > 0:
        v = queue.pop()
        if not visited[v]:
            visited[v] = True
            queue.extend(graph[v])

            while len(stack) > 0 and v not in graph[stack[-1]]:
                tmp = stack.pop()
                ordered.append(tmp)
            stack.append(v)

    return stack + ordered[::-1]

graph = create_graph(V, E)

indegree = [0]*V

start = 0
end = V-1

dist = [float('-inf')]*V
dist[start] = 0

toposort = iterative_topological_sort( graph, start )

for u in toposort:
    for v in graph[u]:
        if dist[v] < dist[u] + weight(u, v):
            dist[v] = dist[u] + weight(u, v)

print(dist[end])
