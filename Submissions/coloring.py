import sys
import copy


def coloration( graph, colors ):

    try:
        node = colors.index( None )
    except:
        node = False

    if not node:
        return True

    used_color = []
    for neighbor in graph[ node ]:
        if colors[neighbor] != None:
            if colors[neighbor] not in used_color:
                used_color.append( colors[neighbor] )

    color = copy.deepcopy( coloring )

    for elem in used_color:
        if elem in color:
            color.remove( elem )

    for c in color:
        colors[ node ] = c
        if coloration( graph, colors ):
            return True
        colors[ node ] = None

    return False


n = int( sys.stdin.readline() )

graph = { }

for i in range( n ):
    graph[i] = list( map( int,  sys.stdin.readline().rstrip('\n').split(" ") ) )

colors = [ None ] * n

colors[0] = 1
colors[graph[0][0]] = 2

for nb_color in range( 2, n + 2 ):

    coloring = [ i for i in range( 1 , nb_color + 1 ) ]
    if coloration( graph, colors ):
        print( nb_color )
        exit( 0 )
