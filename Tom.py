import sys
import math

nk = input().strip().split()
n = int(nk[0])
k = int(nk[1])
total = 0

i = 0
nfac = math.factorial(n)
nifac = nfac

while i <= k:
    total += nfac / nifac  # (math.factorial(n - i))
    i += 2
    nfac /= (i - 1) * i
    if n > i:
        nifac /= ((n - i +1) * (n - i + 2))
    else:
        break

if n <= i:
    total += nfac

print(int(total))
