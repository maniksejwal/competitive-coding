t = int(input())
for i in range(t):
    n = int(input())
    mod = n % 8
    if mod == 1 or mod == 3 or mod == 4 or mod == 6:
        print("Yes")
    else:
        print("No")
