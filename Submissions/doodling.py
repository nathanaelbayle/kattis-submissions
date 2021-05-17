import sys

def compute_gcd( x, y ):
   while( y ):
       x, y = y, x % y
   return x

def compute_lcm( x, y ):
   return ( x * y ) // compute_gcd( x, y )

def compute( x, y ):
    L = compute_lcm( x-1, y-1)
    return L + 1 - (1/2) * (L /(x-1)-1)*(L/(y-1)-1)

n = int( sys.stdin.readline() )

for i in range( n ):
    x, y = map(int, sys.stdin.readline().rstrip('\n').split(" "))
    print( int( compute( x, y ) ) )
