import math


def round_up(num):
    temp = round(num, 2)
    if temp < num:
        temp += 0.01
    return temp


t = int(input())
if 1 <= t <= 100:
    for i in range(t):
        n = int(input())
        sv = float(input())
        csv = float(input())
        r = float(input())
        cr = float(input())

        if 20000 > n or n > 10000000 or 0.00 > sv or sv > 10000.00 or -2000.00 > csv \
                or csv > 2000.00 or 0.01 > r or r > 99.99 or -10.00 > r > 10.00 or (csv < 0.00 < cr):
            print("Invalid Input")
            continue

        psv = sv - csv

        pr = r - cr
        if 0.01 > pr or pr > 99.99 or psv < 0 or 20.00 > psv or psv > 10000.00:
            print("Invalid Input")
            continue
        print("%.2f" % round_up(psv))
        print("%.2f" % round_up(pr))

        cv = n * min(sv, psv)
        print("%.2f" % round_up(cv))

        ce = cv / 2
        print("%.2f" % round_up(ce))

        ca = ce * (min(pr, r) / 100)
        print("%.2f" % round_up(ca))

else:
    print("invalid input")
