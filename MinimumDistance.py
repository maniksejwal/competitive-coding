import math

X = int(input())
Y = int(input())
vx = int(input())
vy = int(input())

if X <= 0 or Y <= 0 or vx <= 0 or vy <= 0:
    print("Invalid Input")
    exit()

t = (X * vx + Y * vy) / (vx ** 2 + vy ** 2)
t = round(t, 11)
d = ((X - vx * t) ** 2 + (Y - vy * t) ** 2)
d = math.sqrt(d)
d = round(d, 11)
print(d)
