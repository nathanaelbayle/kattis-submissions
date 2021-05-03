import sys
import heapq

# Find
def find( u ):
    if comp[u] == u:
        return u
    else:
        parent = find(comp[u])
        comp[u] = parent
        return parent

# Union
def union( u, v ):
    r1 = find(u)
    r2 = find(v)
    if rank[r1] < rank[r2]:
        comp[r1] = r2
        size[r2] += size[r1]
    elif rank[r2] < rank[r1]:
        comp[r2] = r1
        size[r1] += size[r2]
    else:
        comp[r1] = r2
        rank[r2] += 1
        size[r2] += size[r1]

# Kruskal
def kruskal( edges ):
    global nb
    while edges:
        w, ( u, v ) = heapq.heappop(edges)
        if find(u) != find(v):
            if w > 10000:
                w -= 10000
            if u in insecure_building and tab[u] == 1:
                continue
            mst.append( (w,u,v) )
            union(u,v)
            tab[u] = 1
            tab[v] = 1
            nb += w
    return mst



n, m, p = map( int, sys.stdin.readline().split(" ") )

if m == 0:
    print(0)
    exit()

tmp = sys.stdin.readline().rstrip('\n').split(" ")

if tmp != ['']:
    insecure_building = { int(tmp[i]) : int(tmp[i]) for i in range(len(tmp))}
else:
    insecure_building = {}
comp = { i : i for i in range(1,n+1) }
rank = { i : 0 for i in range(1,n+1) }
tab  = { i : 0 for i in range(1,n+1) }

edges = []
size = [1] * (n + 1)

nb = 0

# Read the input
for i in range(m):
    x, y, l = map( int, sys.stdin.readline().split(" ") )
    if x in insecure_building or y in insecure_building:
        l += 10000
    if n > 2:
        if x in insecure_building and y in insecure_building:
            continue
    edges.append( ( l, ( x, y ) ) )

if n == 2:
    if insecure_building:
        print(edges[0][0]-10000)
        exit()
    else:
        print("impossible")
        exit()

heapq.heapify(edges)

mst = []
kru = kruskal(edges)




if len(kru) == 0 or size[find(kru[0][1])] != n:               # if mst is empty or size of final set not equal to number of vertex
    print("impossible")                                       # print impossible
else:
    print(nb)
