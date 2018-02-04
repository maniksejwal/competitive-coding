n, k = input().split()
a = input().strip().split()
b = input().strip().split()

a = [int(i) for i in a]
b = [int(i) for i in b]
n = int(n)
k = int(k)

maxVal = 0
i = 0
while i < len(b):
    if b[maxVal] < abs(b[i]):
        maxVal = i
    i += 1

if b[maxVal] > 0:
    a[maxVal] -= k * 2
elif b[maxVal] < 0:
    a[maxVal] += k * 2

minSum = 0
i = 0
while i < len(b):
    minSum += a[i] * b[i]
    i+=1

print(minSum)
