import sys

n = int(input())


class Counter:
    count = 1
    a = [[0 for x in range(n)] for y in range(n)]
    pp = 1
    ppv = []

    def __init__(self):
        self.ppv.append(0)
        self.ppv.append(0)
        for i in range(n - 1):
            self.stage(n, i)
        self.output()
        print("Total Power points : " + str(self.pp))
        i = 0
        while 2*self.pp > i:
            s = str(self.ppv[i])
            t = str(self.ppv[i + 1])
            print("(" + s + "," + t + ")")
            i += 2

    def stage(self, size, round):
        for i in range(size - 1 - round):
            if self.a[round][i + round] != 0: continue
            self.a[round][i + round] = self.count
            if self.count % 11 == 0:
                self.pp += 1
                self.ppv.append(round)
                self.ppv.append(round + i)
            if self.count >= n * n: return
            self.count += 1
        # print(self.count)

        for i in range(size - 1 - round):
            if self.a[i + round][size - round - 1] != 0: continue
            self.a[i + round][size - round - 1] = self.count
            if self.count % 11 == 0:
                self.pp += 1
                self.ppv.append(i + round)
                self.ppv.append(size - round - 1)
            if self.count >= n * n: return
            self.count += 1
        # print(self.count)

        for i in range(size - 1 - round):
            if self.a[size - round - 1][size - round - i - 1] != 0: continue
            self.a[size - round - 1][size - round - i - 1] = self.count
            if self.count % 11 == 0:
                self.pp += 1
                self.ppv.append(size - round - 1)
                self.ppv.append(size - round - i - 1)
            if self.count >= n * n: return
            self.count += 1
        # print(self.count)

        for i in range(size - 1 - round):
            if self.a[size - i - round - 1][round] != 0: continue
            self.a[size - i - round - 1][round] = self.count
            if self.count % 11 == 0:
                self.pp += 1
                self.ppv.append(size - i - round - 1)
                self.ppv.append(round)
            if self.count >= n * n: return
            self.count += 1
            # print(self.count)

    def output(self):
        for i in range(n):
            for j in range(n):
                print(self.a[i][j], end='\t')
                #if j != n - MockVita: print("\t", end="")
            print("")


my_counter = Counter()
