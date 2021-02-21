import sys
import copy

def create_graph(m, n):
    graph = {}
    input = []
    for i in range(m):
        graph[i] = []
    for i in range(n):
        x, y = map(int, sys.stdin.readline().split(" "))
        input.append([x, y])
        graph[x].append(y)
    return graph, input

def reversing( graph ):
    graph_inverted = {}
    for i in range(m):
        graph_inverted[i] = []
    for x in graph:
        for y in graph.get(x):
            graph_inverted[y].append(x)
    return graph_inverted

def DFS(graph, v, visited, pre, post, time):
    time += 1
    pre[v] = time
    visited[v] = True
    for neighbour in graph[v]:
        if not visited[neighbour]:
            time = DFS(graph, neighbour, visited, pre, post, time)
    time += 1
    post[v] = time
    return time

def SCC( graph ):

    _graph = reversing(graph)

    time = 0
    pre = [0] * m
    post = [0] * m
    visited = [False] * m

    for i in range(m):
        if not visited[i]:
            time = DFS(graph, i, visited, pre, post, time)

    tmp = sorted(post)
    tmp.reverse()

    tmp2 = copy.deepcopy(post)

    time = 0
    pre = [0] * m
    post = [0] * m
    visited = [False] * m

    for i in range(m):
        if not visited[tmp2.index(tmp[i])]:
            time = DFS( _graph, tmp2.index(tmp[i]), visited, pre, post, time)

    css = []
    tmp_pre = copy.deepcopy(pre)
    tmp_post = copy.deepcopy(post)
    while len(tmp_pre) > 0 or len(tmp_post) > 0:
        tmp = []*m
        min = float('inf')
        for i in range(len(tmp_pre)):
            if min > tmp_pre[i]:
                min = tmp_pre[i]

        min2 = tmp_post[tmp_pre.index(min)]

        for i in range(len(tmp_post)):
            if tmp_post[i] <= min2:
                tmp.append(tmp_post[i])

        for i in tmp:
            tmp_pre.remove(pre[post.index(i)])
            tmp_post.remove(i)

        for i in range(len(tmp)):
            x = post.index(tmp[i])
            tmp[i] = x

        css.append(tmp)
    return css


def try_inverted( graph, cfc, input ):
    tmp = []
    ans = []
    first = []
    for j in cfc:
        for k in j:
            for x in graph[k]:
                tmp_graph = copy.deepcopy(graph)
                if x not in j:
                    tmp_graph[k].remove(x)
                    tmp_graph[x].append(k)

                    tmp = SCC( tmp_graph )

                    if len(tmp) == 1:
                        ans.append([k, x])
    if ans:
        first = ans[0]
        for i in ans:
            if input.index(first) > input.index(i):
                first = i
    return first

compteur = 0
graphs = []

for g in range(5):
    compteur += 1
    try:
        m, n = map(int, sys.stdin.readline().split(" "))
    except:
        break

    graph, input = create_graph(m, n)
    graphs.append(graph)

    scc = SCC( graphs[g] )

    if len(scc) == 1:
        print("Case ", compteur, ": valid", sep='')
    else:

        x = try_inverted(graphs[g], scc, input)

        if len(x) > 1:
            print("Case ", compteur, ": ", x[0], " ", x[1], sep='')
        else:
            print("Case ", compteur, ": invalid", sep='')
