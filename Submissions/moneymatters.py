import sys

sys.setrecursionlimit(10000)

def dfs( node ):
    global balance
    balance += liste[node]
    visited[node] = True
    for x in adjacency[node]:
        if not visited[x]:
            dfs(x)

n, m =  map(int, sys.stdin.readline().split(" "))

liste = []
ami = []
adjacency = [[] for _ in range(n)]

for i in range(n):
    liste.append(int(sys.stdin.readline().rstrip('\n')))

for i in range(m):
    x, y = map(int, sys.stdin.readline().rstrip('\n').split(" "))
    ami.append([x,y])

for i in range(m):
    x, y = map(int, ami[i])
    adjacency[x].append(y)
    adjacency[y].append(x)

visited = [False]*n

balance = 0

for i in range(n):
    if visited[i]:
        continue
    balance = 0
    dfs(i)
    if balance != 0:
        print("IMPOSSIBLE")
        sys.exit(0)
print("POSSIBLE")
sys.exit(0)
