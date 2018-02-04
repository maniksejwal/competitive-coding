t = int(input())
for i in range(t):
    letters = [0] * 26
    s = input()
    for j in s:
        letters[ord(j) - ord('a')] += 1
    j = 0
    isSuper = True
    for j in range(len(letters)):
        if j == letters[j] - 1 or letters[j] == 0:
            continue
        else:
            isSuper = False
            break
    if isSuper:
        print("Yes")
    else:
        print("No")
