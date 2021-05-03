import sys

class Point:
  def __init__( self, x, y ):
    self.x = x
    self.y = y

def dist( p_1, p_2 ):
  return (( p_1.x - p_2.x )**2 + ( p_1.y - p_2.y )**2 )** 0.5

n, t = map( int, sys.stdin.readline().rstrip('\n').split(" ") )

pos = []
for i in range( n ):
    x, y, tmp = map( int, sys.stdin.readline().rstrip('\n').split(" ") )
    pos.append( (Point( x, y ), tmp) )

GPS_dist = 0
for i in range( n - 1 ):
    GPS_dist += dist( pos[ i ][0], pos[ i + 1 ][0] )

pts = [ pos[0][0] ]

previous = 0
current  = 1
for time in range( t, pos[-1][1], t ):
    currentTime = pos[current][1]
    while time > currentTime:
        current += 1
        previous = currentTime
        currentTime = pos[current][1]
    D = ( time - previous ) / ( currentTime - previous )
    pts.append( Point( (pos[current - 1][0].x + (pos[current][0].x - pos[current - 1][0].x) * D),
                       (pos[current - 1][0].y + (pos[current][0].y - pos[current - 1][0].y) * D) ) )

pts.append( pos[-1][0] )

REAL_dist = 0
for i in range(len(pts) - 1):
    REAL_dist += dist( pts[i], pts[i+1] )

print( 100 - ( 100 * REAL_dist / GPS_dist ) )
