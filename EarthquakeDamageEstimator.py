
n = int(input())
a = [input().split() for i in range(n)]
x, y = [int(i) for i in input().split()]
intensity = int(input())
x -= 1
y -= 1

def neighbor(_x, _y, val):
    if a[_x, _y]==1:
        a[_x+1, y]

if intensity > 8:
   a[x, y] = 3
   neighbor(x, y, 3)

