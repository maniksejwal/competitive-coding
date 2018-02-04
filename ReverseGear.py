N = int(input())
for i in range(N):
    pos = 0
    time = 0
    f, b, t, d = [int(j) for j in input().split()]
    while pos < d:
        pos += b
        if pos <= d:
            time += t * b
            if pos == d:
                break
            else:
                time += t * f
                pos -= f
        else:
            time += t * (d - pos + b)
    print(time)
