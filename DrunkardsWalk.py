n = int(input())
for i in range(n):
    d, FM, BM, T, FBS, BBS = input().split()
    fm = int(FM)
    bm = int(BM)
    t = int(T)
    fbs = int(FBS)
    bbs = -int(BBS)
    pos = oldPos = 0
    time = 0
    slipped = False

    if d == 'B':
        if pos - bm <= bbs:
            slipped = True
            time += (pos - bbs) * t
        else:
            time += bm * t
            pos -= bm

    while not slipped:
        if pos + fm >= fbs:
            slipped = True
            time += (fbs - pos) * t
            break
        else:
            time += fm * t
            pos += fm

        if pos - bm <= bbs:
            slipped = True
            time += (pos - bbs) * t
            break
        else:
            time += bm * t
            pos -= bm
        if pos == oldPos:
            slipped = False
            break
        else:
            oldPos = pos

    if slipped:
        print("%d %c" % (time, 'B' if pos < 0 else 'F'))
    else:
        print("Hurray")
