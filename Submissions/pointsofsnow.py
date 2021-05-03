import sys


left   = lambda i : 2 * i
right  = lambda i : 2 * i + 1
parent = lambda i : i // 2
index  = lambda T, i : len(T) // 2 + i



def update(tree, l, r, value):
    while True:
        pl = parent(l)
        pr = parent(r)
        if pl == pr:
            return
        if l % 2 == 0:
            tree[right(pl)] += value
        if r % 2 == 1:
            tree[left(pr)] += value
        l, r = pl, pr


def query( tree, idx ):
    sum = tree[idx]
    while True:
        sum += tree[parent(idx)]
        idx = parent(idx)
        if idx == 1:
            return sum




n, k, q =  map( int, sys.stdin.readline().rstrip('\n').split(" ") )

data = [0] * n
tree = [0] * len(data) + data


for i in range(k+q):
    tmp = sys.stdin.readline()
    if tmp[0] == '!':
        l, r, d = map( int, tmp[2:].rstrip('\n').split(" ") )
        update( tree, n + l - 1 , n + r, d)
    else:
        x = int(tmp[2:])
        print(query( tree, n + x - 1 ))
