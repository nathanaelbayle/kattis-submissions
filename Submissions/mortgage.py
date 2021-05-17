import sys

def mortgage( X, Y, N, r ):
    month_rate = r / 12 / 100

    if X * month_rate >= Y:
        return False

    elif r < 0.001:
        if Y * N * 12 < X:
            return False
    else:
        balance = ( X - Y / month_rate ) * pow( 1 + month_rate , N * 12 ) + Y / month_rate
        if balance > 0:
            return False
    return True


while True:
    data = sys.stdin.readline().rstrip('\n').split(" ")

    X, Y, N, r = int( data[0] ), int( data[1] ), int( data[2] ), float( data[3] )

    if X == Y == N == r == 0:
        exit()

    if mortgage( X, Y, N, r ):
        print( "YES" )
    else:
        print( "NO" )

#
