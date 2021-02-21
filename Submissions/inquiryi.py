import sys

n = int(sys.stdin.readline())

data = []
for i in range(n):
    data.append(int(sys.stdin.readline()))

def somme( tab ):
    res = 0
    for i in range(n):
        res += tab[i]
    return res

def fonction( data ):
    droite = 0
    gauche = somme( data )
    res = []
    for i in range(n):
        droite = droite + data[i]**2
        gauche = gauche - data[i]
        res.append( gauche * droite )
    return( res )

def maximum( data ):
    res = 0
    for i in range(n):
        if data[i] > res:
            res = data[i]
    return res

print( maximum( fonction( data ) ) )
