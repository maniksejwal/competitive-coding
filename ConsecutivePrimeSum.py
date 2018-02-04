primeRange = int(input())

primeList = [2]
i = 3
primeSum = 2
index = 0
primeCount = 0
while i < primeRange:
    isPrime = True
    for j in primeList:
        if i % j == 0:
            isPrime = False
            break
    if isPrime:
        primeList.append(i)
        while primeSum + primeList[index] <= i:
            primeSum += primeList[index]
            index += 1
        if primeSum == i:
            primeCount += 1
    i += 2
print(primeCount)
