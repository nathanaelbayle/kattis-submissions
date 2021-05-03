import sys
from collections import deque


def create_path( parent, s, t ):
    path = [t]
    while t != s:
        t = parent[t]
        path.append(t)
    return tuple( reversed(path) )

def BFS( graph, s, t ):
    q = deque( [s] )
    parent = {}
    while q:
        v = q.popleft()
        for u in graph[v]:
            if u in parent:
                continue
            if capacity[(v,u)] <= 0:
                continue
            parent[u] = v
            q.append( u )
            if u == t:
                return create_path( parent, s, t )

edges = lambda p: zip( p, p[1:] )

def maxflow( graph, s, t ):
    flow = 0
    P = BFS( graph, s, t )          # P => Path from s to t
    while P :
        F = min( capacity[(v,u)] for (v, u) in edges(P) )
        flow += F
        for i in range( 1, len(P) ):
            v, u = P[i - 1], P[i]
            capacity[(v,u)] -= F
            capacity[(u,v)] += F
        try:
            P = BFS( graph, s, t )
        except:
            return flow
    return flow

n, p, k = map( int, sys.stdin.readline().rstrip('\n').split(" ") )

graph_initial   = { i : [] for i in range( 1, n + 1) }
capacity = { }
for i in range( p ):
    a, b, c = map( int, sys.stdin.readline().rstrip('\n').split(" ") )
    graph_initial[ a ].append( b )
    graph_initial[ b ].append( a )

    capacity[ ( a, b ) ] = c
    capacity[ ( b, a ) ] = c


flow = maxflow(graph_initial, 1, 2)
print( flow )

for i in range( k ):
    a, b, c = map( int, sys.stdin.readline().rstrip('\n').split(" ") )
    if b not in graph_initial[a]:
        graph_initial[ a ].append( b )
        graph_initial[ b ].append( a )

    if ( a, b ) in capacity:
        capacity[ ( a, b ) ] += c
        capacity[ ( b, a ) ] += c
    else:
        capacity[ ( a, b ) ] = c
        capacity[ ( b, a ) ] = c

    flow += maxflow(graph_initial, 1, 2)
    print( flow )
