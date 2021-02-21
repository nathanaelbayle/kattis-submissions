import sys

C, A = map(int, sys.stdin.readline().split(" "))

S = []
x = sys.stdin.readline().rstrip('\n').split(" ")
for i in range(A):
    S.append([int(x[i]), i])

answer = []

S.sort()

R = [0] * C

def search( element ):
    global right, left, max_iter

    while left <= right and max_iter > 0:

        median = (right + left) // 2

        if right == left+1:
            median = right

        if R[median] == 0:
            print("Q", median+1)
            sys.stdout.flush()
            R[median] = int(sys.stdin.readline())
            max_iter -= 1

        if R[median] == element:
            R[median] = element
            right = left

        if element < R[median]:
            right = median - 1
        else:
            left = median + 1

    max = 0
    for i in R:
        if i <= element:
            if i > max:
                max = i

    return R.index(max)+1

max_iter = 1500

for element in S:
    left = 0
    right = len(R) - 1
    answer.append([search(element[0]), element[1]])

answer.sort(key=lambda x:x[1])

print("A ", sep='', end='')
for i in answer:
    print(i[0], " ", sep='', end='')
