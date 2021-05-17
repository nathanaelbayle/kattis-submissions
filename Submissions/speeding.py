import sys

n = int( sys.stdin.readline() )

data = []
for i in range( n ):
    t, d = map(int, sys.stdin.readline().rstrip('\n').split(" "))
    data.append( (t,d) )

max_speed = 0
for i in range( 1, n ):

    tmp = (data[i][1] - data[i-1][1]) // (data[i][0] - data[i-1][0])

    if tmp > max_speed:
        max_speed = tmp

print( max_speed )
