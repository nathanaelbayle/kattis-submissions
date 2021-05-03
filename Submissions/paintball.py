import sys

def Matching( edge ):
    if visited[edge]:
        return

    visited[edge] = True
    for neighbour in graph[edge]:
        if not match[neighbour] or Matching( match[neighbour] ):
            match[neighbour] = edge
            return True
    return False


n, m = map( int, sys.stdin.readline().rstrip('\n').split(" ") )

graph = { i : [] for i in range( n + 1 ) }

for i in range( m ):
    a, b = map( int, sys.stdin.readline().rstrip('\n').split(" ") )
    graph[ a ].append( b )
    graph[ b ].append( a )

res = 0
match = [False] * ( n + 1 )

for i in range( 1, n + 1 ):
    visited = [False] *( n + 1 )
    res += Matching( i )

if res < n:
    print("Impossible")
    exit()

solution = [0] * ( n + 1 )
for i in range( 1, n + 1 ):
    solution[ match[i] ] = i

for i in range( 1, n + 1 ):
    print( solution[ i ])
