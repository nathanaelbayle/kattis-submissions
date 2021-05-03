import sys
from collections import defaultdict

# Find
def find(x):
    p = parent[x]
    while p != parent[p]:
        p = parent[p]
    while x != p:
        x, parent[x] = parent[x], p
    return p

# Union
def union( u, v ):
    r1 = find(u)
    r2 = find(v)
    if r1 == r2:
        return
    if rank[r1] < rank[r2]:
        building[building_reverse[r2]] = r1
        parent[r2] = r1
        size[r1] += size[r2]
    elif rank[r1] > rank[r2]:
        building[building_reverse[r1]] = r2
        parent[r1] = r2
        size[r2] += size[r1]
    else:
        building[building_reverse[r1]] = r2
        parent[r1] = r2
        size[r2] += size[r1]
        rank[r2] += 1

def default():
    return 0

n = int( sys.stdin.readline() )


size = [1] * ( 1100000 )                  # To compute the size of any set

parent = { i : i for i in range( 1100000 ) }
rank   = { i : 0 for i in range( 1100000 ) }

building = defaultdict( default )
building_reverse = defaultdict( default )

count = 0

for i in range( n ):
    try:
        str_1, str_2 = map( type(" "), sys.stdin.readline().rstrip('\n').split(" ") )
    except:
        exit()
    if str_1 not in building:
        building[str_1] = count
        building_reverse[count] = str_1
        count += 1
    if str_2 not in building:
        building[str_2] = count
        building_reverse[count] = str_2
        count += 1

    union(find( building[str_1] ), find( building[str_2] ) )
    print(size[ find( building[str_2] ) ])
