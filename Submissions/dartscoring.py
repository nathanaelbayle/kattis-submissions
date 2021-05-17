import sys
import math

from functools import reduce


class Point:
    def __init__( self, x = 0, y = 0 ):
        self.x = x
        self.y = y

def score( s ):
    return 100 *  n  / ( 1 + s )

def dist( p_1, p_2 ):
    return math.sqrt( ( p_1.x - p_2.x ) ** 2 + ( p_1.y - p_2.y ) ** 2 )

def orientation( p_1, p_2, p_3 ):
    return ( p_2.y - p_1.y ) * ( p_3.x - p_2.x ) - ( p_3.y - p_2.y ) * ( p_2.x - p_1.x )

# Convex hull
def graham( points ):
    s = []
    hull = []

    points.sort( key = lambda point: ( point.x, point.y ) )

    for point in points:
        while len(s) >= 2 and orientation( s[-2], s[-1], point ) < 0:
            s.pop()
        s.append( point )
    hull += s

    s = []
    for point in reversed( points ):
        while len(s) >= 2 and orientation( s[-2], s[-1], point ) < 0:
            s.pop()
        s.append( point )
    hull += s[1:-1]
    return hull

for cases in range( 200 ):

    input = sys.stdin.readline().rstrip('\n').split(" ")

    if input[0] == '':
        exit(0)

    data = []
    for i in range( 0, len(input) + 1 // 2, 2 ):
        data.append( Point( float( input[ i ] ), float( input[ i + 1 ] ) ) )

    n = len( data )

    if n == 1:
        total_Length = 0
    elif n == 2:
        total_Length = 2 * dist( data[0], data[1] )
    else:
        total_Length = 0

        Hull = graham( data )

        for i in range( 1, len( Hull ) ):
            total_Length += dist( Hull[ i - 1 ], Hull[ i ] )
        total_Length += dist( Hull[ -1 ], Hull[ 0 ] )

    print( score( total_Length ) )


#
