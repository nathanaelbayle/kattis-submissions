import sys

def factorial( n ):
    res = [ 0 ] * n
    for i in range( n ):
        if i == 0 or i == 1:
            res[ i ] = 1
            continue
        res[ i ] = res[ i - 1 ] * i
    return res

def euclidian( x, y ):
    return ( x // y, x % y )

while True:
    data = sys.stdin.readline().rstrip('\n')
    if data == '':
        exit(0)

    n, k = map( int, data.split(" ") )

    number_list = [ i for i in range( 1, n + 1 ) ]

    res = []

    fact = factorial( n )

    ith_perm = k
    y = ith_perm

    for i in range( 1, n + 1 ):
        x, y = euclidian( y, fact[ n - i ] )
        res.append( number_list[ x ] )
        number_list.remove( number_list[x] )

    print( * res )


#
