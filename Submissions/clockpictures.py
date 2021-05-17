import sys

A = 8191
B = 2147483647
MAX = 360000

def compute( line ):
    h, big_int = 0, 1

    rolling = [ 0 ] * n
    for i in range( n ):
        rolling[ i ] = ( line[ ( i + 1 ) % n ] - line[ i ] + MAX ) % MAX
        h = ( h * A + rolling[ i ] ) % B
        big_int = big_int * A % B

    big_int = ( B + 1 - big_int ) % B
    res = h

    for i in range( n ):
        h = ( h * A + big_int * rolling[ i ] ) % B
        res = min( res, h )

    return res

n = int( sys.stdin.readline() )

line_1 = sys.stdin.readline().rstrip('\n').split(" ")
line_2 = sys.stdin.readline().rstrip('\n').split(" ")
for i in range( n ):
    line_1[i] = int( line_1[ i ] )
    line_2[i] = int( line_2[ i ] )

line_1.sort()
line_2.sort()

if compute( line_1 ) == compute( line_2 ):
    print( "possible" )
else:
    print( "impossible" )



#
