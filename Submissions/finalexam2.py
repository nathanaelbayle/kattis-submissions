n = input()
liste = []
for i in range(int(n)):
    score = 0
    liste.append(input())
for i in range(len(liste)-1):
    if liste[i] == liste[i+1]:
        score += 1
print(score)
