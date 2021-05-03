import sys


def left  ( i ) : return 2 * i
def right ( i ) : return 2 * i + 1
def parent( i ) : return i // 2
def index ( i ) : return len(T) // 2 + i


def fill(tree, op=sum):
    internal = range(1, len(tree) // 2)
    for idx in reversed(internal):
        tree[idx] = op((tree[left(idx)], tree[right(idx)]))


def update(tree, idx, value, op=sum):
    tree[idx] += value
    idx = parent(idx)
    while idx > 0:
        tree[idx] = op((tree[left(idx)], tree[right(idx)]))
        idx = parent(idx)


def update2( tree, idx, val ):
    tree[idx] += val
    i = idx
    while i > 1:
        tree[i//2] = tree[i] + tree[i+1]
        i = i//2


def query( tree, l, r ):
    res = tree[l]
    while True:
        pl = parent(l)
        pr = parent(r)
        if pl == pr:
            return res
        if l % 2 == 0 :
            res += tree[right(pl)]
        if r % 2 == 1 :
            res += tree[left(pr)]
        l, r = pl, pr


NB_GEMS = 6

n, m = map( int, sys.stdin.readline().rstrip('\n').split(" ") )

value = []
value.extend(sys.stdin.readline().rstrip('\n').split(" "))
for i in range(NB_GEMS):
    value[i] = int(value[i])

data = []
input = sys.stdin.readline().rstrip('\n')
for char in input:
    data.append( int(char) )

Trees = { i : [0] * (2 * n) for i in range(1,NB_GEMS+1) }

for gem in range(1,NB_GEMS+1):
    for i in range(n):
        if data[i] == gem:
            Trees[gem][ n + i ] += 1
    fill( Trees[gem] )

for i in range(m):
    gem, x, y = map( int, sys.stdin.readline().rstrip('\n').split(" ") )

    if gem == 1:
        update( Trees[ data[ x - 1 ] ], n + x - 1, -1 )
        data[ x - 1 ] = y
        update( Trees[ y ], n + x - 1, 1 )

    elif gem == 2:
        value[ x - 1 ] = y

    else:
        sum = 0
        for j in range( 1, NB_GEMS + 1 ):
            sum += query( Trees[j], n + x - 1, n + y ) * value[ j-1 ]
        print(sum)
