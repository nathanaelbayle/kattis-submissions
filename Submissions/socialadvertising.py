import sys

nb_test_case = int( sys.stdin.readline() )

for i in range( nb_test_case ):

    n = int( sys.stdin.readline() )

    adj = { i : 0 for i in range( n ) }

    for i in range( n ):
        input = sys.stdin.readline().rstrip('\n').split(" ")
        for j in range( 1, int( input[0] ) + 1 ):
            adj[i] |= 1 << int( input[j] ) - 1
        adj[i] |= 1 << i

    ans = n

    for i in range( 2 ** n - 1 ):
        x = 0
        y = 0

        for j in range( n ):
            if i & 1 << j:
                y |= adj[j]
                x += 1

        count = 0
        while y:
            count += y & 1
            y >>= 1

        if count == n and ans > x:
            ans = x

    print( ans )
