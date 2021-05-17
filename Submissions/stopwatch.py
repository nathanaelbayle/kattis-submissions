import sys

n = int( sys.stdin.readline() )

times = []
for i in range( n ):
    times.append( int( sys.stdin.readline() ) )

if n % 2 == 1:
    print( "still running" )
    exit( 0 )

ans = 0
while times:
    ans += times[1] - times[0]
    times.remove( times[1] )
    times.remove( times[0] )

print(ans)


#
