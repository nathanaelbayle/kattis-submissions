import sys

data = sys.stdin.readline()

n = int(data.split(" ")[0])
m = int(data.split(" ")[1])

liste = []

def split(word):
    return [char for char in word]

for i in range(n):
    liste.append(split(sys.stdin.readline().rstrip('\n').upper()))

for x in range(n*m):
    for i in range(n):
        for j in range(m):
            if liste[i][j] == 'V' :
                if i < n - 1:
                    if liste[i+1][j] == '.':
                        liste[i+1][j] = 'V'
                    if liste[i+1][j] == '#':
                        if j > 0 and liste[i][j-1] == '.':
                            liste[i][j-1] = 'V'
                        if j < m - 1 and liste[i][j+1] == '.':
                            liste[i][j+1] = 'V'

for i in range(len(liste)):
    for j in range(len(liste[i])):
        print(liste[i][j],end='')
    print()
