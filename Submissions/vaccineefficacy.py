import sys


n = int( sys.stdin.readline() )


placebo = []
vaccine = []
for i in range( n ):
    input = sys.stdin.readline().rstrip('\n')
    if input[0] == "Y":
        vaccine.append( input )
    else:
        placebo.append( input )

for j in range( 1, 4 ):
    stat_1 = 0
    stat_2 = 0
    for i in range( len(vaccine) ):
        if vaccine[i][j] == "Y":
            stat_1 += 1
    for i in range( len(placebo) ):
        if placebo[i][j] == "Y":
            stat_2 += 1

    proba_1 = ( stat_1 * 100 ) / len( vaccine )
    proba_2 = ( stat_2 * 100 ) / len( placebo )

    if proba_1 > proba_2 :
        print("Not Effective")
        continue

    res =  round( ( ( 1 - ( proba_1 / proba_2 ) ) * 100 ) , 6 )
    if res == 0.0:
        print("Not Effective")
        continue
    else:
        print( res )


#
