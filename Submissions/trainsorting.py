import sys

def find_max( after, before ):
    nbMax = 0
    for i in range(n):
        tmp = after[i] + before[i] -1
        if tmp > nbMax:
            nbMax = tmp
    return nbMax

def compute( n, weights ):
    after = [0] * ( n + 1 )
    before = [0] * ( n + 1 )
    for i in range( n-1, -1, -1 ):
        for j in range( i+1, n+1 ):
            if j == n or weights[j] > weights[i]:
                newTrain = after[j] + 1
                if newTrain > after[i]:
                    after[i] = newTrain
            if j == n or weights[j] < weights[i]:
                newTrain = before[j] + 1
                if newTrain > before[i]:
                    before[i] = newTrain
    return after, before

n = int( sys.stdin.readline() )

weights = []
for i in range(n):
    tmp = int( sys.stdin.readline() )
    weights.append( tmp )

after, before = compute( n, weights )
print( find_max( after, before ) )
