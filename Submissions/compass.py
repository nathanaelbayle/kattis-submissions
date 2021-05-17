import sys

n_1 = int( sys.stdin.readline() )
n_2 = int( sys.stdin.readline() )

x =  ( (360 - n_1) + (n_2) ) % 360

y =  ( (360 - n_2) + ( n_1) ) % 360

if x <= y:
    print(x)
else:
    print( - y )

#
