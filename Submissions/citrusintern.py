import sys

def findMin( node ):

    if not len( member[ node ] ):
        costSubordinates [ node ] = float( 'inf' )
        costSuperior [ node ] = 0
        return

    delta = float( 'inf' )

    for i in member[ node ]:
        findMin( i )
        res[ node ] += costSuperior[ i ]
        costSubordinates[ node ] += min( res[i], costSubordinates [i] )
        costSuperior[ node ]     += min( res[i], costSubordinates [i] )
        delta = min( max( ( res[i] - costSubordinates [i] ), 0 ), delta )
    costSubordinates[ node ] += delta

n = int( sys.stdin.readline() )

member = { i : [] for i in range( n ) }
cost   = { }

rootArray = [ 0 ] * n
for i in range( n ):
    inpu = sys.stdin.readline().rstrip('\n').split(" ")

    cost[i] = int( inpu[0] )
    if inpu[1] == '0':
        continue
    for j in range( 2, len(inpu) ):
        member[i].append( int( inpu[j] ) )
        rootArray[ int( inpu[j] ) ] = -1

root = rootArray.index( 0 )

res = []

for i in cost:
    res.append( cost[i] )

costSubordinates  = [ 0 ] * n
costSuperior      = [ 0 ] * n

findMin( root )

print( min( res[root], costSubordinates[ root ] ) )
