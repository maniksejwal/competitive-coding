import math

N = int(input())
n = 2
bricks = 0
brick = 0
while bricks < N:
    if brick == 0:
        for j in range(N - bricks - 1):
            print(' ', end='')
    num = n * (2 * n - 1)
    for k in range(5 - int(math.log(num, 10))):
        print('0', end='')
    print(num, end='')
    n += 2
    if brick < bricks:
        print(' ', end='')
        brick += 1
    else:
        print('')
        bricks += 1
        brick = 0
