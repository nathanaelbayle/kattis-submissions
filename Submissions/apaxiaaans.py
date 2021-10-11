import sys

word = sys.stdin.readline().rstrip("\n")

res = word[0]

for c in range(1,len(word)):
    if word[c-1] != word[c]:
        res += word[c]

print( res )