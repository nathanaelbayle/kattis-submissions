import sys

class Point:
    def __init__( self, index, x = 0, y = 0 ):
        self.index = index
        self.x = x
        self.y = y

def graham( points ):
    s = []
    poly = []
    points.sort( key = lambda point: (point.x, point.y) )

    for point in points:
        while len(s) >= 2 and orientation( s[-2], s[-1], point ) < 0:
            s.pop()
        s.append( point )
    poly += s
    for point in reversed( points ):
        if point not in poly:
            poly.append( point )
    return poly

def orientation( p_1, p_2, p_3 ):
    return ( p_2.y - p_1.y ) * ( p_3.x - p_2.x ) - ( p_3.y - p_2.y ) * ( p_2.x - p_1.x )

c = int( sys.stdin.readline() )

for nb_case in range( c ):
    data = sys.stdin.readline().rstrip('\n').split(" ")

    n = int( data.pop( 0 ) )

    points = [ ]
    for i in range( 0, n * 2, 2 ):
        points.append( Point( i // 2, int( data[ i ] ), int( data[ i + 1 ] ) ) )

    points.sort( key = lambda point: point.x )

    res = graham( points )

    for point in res:
        print( point.index, end=" ")
    print()

#
