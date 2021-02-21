import sys

for i in sys.stdin:
    print(abs(int(i.split(" ")[0])-int(i.split(" ")[1])))
