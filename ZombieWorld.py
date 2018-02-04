k = int(input())
for i in range(k):
    n, T = [int(j) for j in input().split()]
    e = [int(j) for j in input().split()]
    p, d = [int(j) for j in input().split()]
    t = 0

    for j in range(n):
        if e[j] > p:
            k = 1
            while e[j + k] > p:
                k += 1
            else:
                temp = e[j + k]
                e[j + k] = e[j]
                e[j] = temp
        p += p - e[j]
        t += 1

    if p >= d and t <= T:
        print("Yes")
    else:
        print("No")
