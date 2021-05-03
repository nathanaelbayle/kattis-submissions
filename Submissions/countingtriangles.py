import sys
import math


class Point:
    def __init__( self, x=0, y=0 ):
        self.x = x
        self.y = y


def intersect2( line_1, line_2 ):

    ( A, B ), ( C, D ) = line_1, line_2

    a_1 = B.x - A.x
    b_1 = B.y - A.y

    a_2 = C.x - D.x
    b_2 = C.y - D.y

    a_3 = C.x - A.x
    b_3 = C.y - A.y


    d = a_1 * b_2 - a_2 * b_1
    if d == 0:
        return False

    p_x = ( a_3 * b_2 - b_3 * a_2 ) / d
    p_y = ( a_1 * b_3 - b_1 * a_3 ) / d

    return not ( p_x < 0 or p_x > 1 or p_y < 0 or p_y > 1 )


def intersect( line_1, line_2 ):

    ( A, B ), ( C, D ) = line_1, line_2

    a_1 = ( B.y - A.y ) / ( B.x - A.x )
    a_2 = ( D.y - C.y ) / ( D.x - C.x )

    b_1 = A.y - ( a_1 * A.x )
    b_2 = C.y - ( a_2 * C.x )

    if a_1 == a_2:
        return False

    tmp = ( b_2 - b_1 ) / ( a_1 - a_2 )
    if ( tmp >= min( A.x, B.x ) and tmp <= max( A.x, B.x ) ) and ( tmp >= min( C.x, D.x ) and tmp <= max( C.x, D.x ) ):
        return True
    return False






while True:
    n = int( sys.stdin.readline().rstrip('\n') )

    if n == 0:
        exit()

    line = []
    for i in range( n ):
        x_1, y_1, x_2, y_2 = map( float, sys.stdin.readline().rstrip('\n').split(" ") )
        p_1 = Point( x_1, y_1 )
        p_2 = Point( x_2, y_2 )
        line.append( ( p_1, p_2 ) )

    count = 0
    for i in range( n - 2 ):
        for j in range( i + 1, n - 1 ):
            for k in range( j + 1, n ):
                if intersect( line[i], line[j] ):
                    if intersect( line[j], line[k] ):
                        if intersect( line[i], line[k] ):
                            count += 1

    print( count )
