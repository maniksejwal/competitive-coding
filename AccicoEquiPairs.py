a = [int(i) for i in input().split()]
sum0 = sum2 = 0
sum1 = a[1]
i = k = 0
j = 1
while i < len(a) - 4:
    sum0 += a[i]
    sum1 -= a[i + 1]
    while j + 2 < len(a) and sum1 + a[j + 1] <= sum0 or j <= i + 1:
        j += 1
        sum1 += a[j]
    if sum1 == sum0:
        sum2 += sum(a[j + 2:])
    if sum0 == sum1 == sum2:
        print("{%d,%d}" % (i+1, j+1))
        print("{0,%d},{%d,%d},{%d,%d}" % ((i), (i + 2), j, (j + 2), (len(a) - 1)))
        break
    i += 1
else:
    print("Array does not contain any equi pair")
