#!/usr/bin/python
import os

outs = []
class Part:
    def __init__(self, f):
        ss = next(f).strip().split(',')
        self.ints = []
        for i in range(5):
            self.ints.append(int(ss[i]))
        self.n = int(next(f).strip())
        self.moves = []
        for i in range(self.n):
            x = next(f).strip().split(',')
            y = []
            for i in range(4):
                y.append(int(x[i]))
            self.moves.append(y)
        self.validate()
    def getMax(self):
        return self.fir + (self.max - self.fir) * self.ints[2] if self.ints[2] > 1 else self.max
    def validate(self):
        doff = 0
        if self.n and (self.moves[0][0] < 0 or self.ints[2] > 1):
            doff -= self.moves[0][0]
        for i in range(self.n):
            self.moves[i][0] += doff
        self.off = doff
        self.fir = self.moves[0][0] if len(self.moves) else 0
        self.max = self.moves[self.n - 1][0] if self.n > 0 else 0

class MaAnim:
    def __init__(self, path):
        f = open(path)
        next(f)
        next(f)
        n = int(next(f).strip())
        self.parts = []
        for i in range(n):
            self.parts.append(Part(f))
        self.validate()
    def validate(self):
        self.len = 1
        for part in self.parts:
            x = part.getMax() - part.off
            if x > self.len:
                self.len = x

unit_file = list(map(lambda x: x.split(','), open('./org/data/t_unit.csv').read().replace('\r', '').split('\n')))
i = 2
for ID in sorted(os.listdir('./org/enemy')):
    if ID == '0' or ID == '1':
        continue
    S = ID.rjust(3, '0')
    try:
        frame = MaAnim(f'./org/enemy/{S}/{S}_e02.maanim').len
    except FileNotFoundError:
        outs.append((100, 0))
        continue
    L = unit_file[i]
    i += 1
    pre = int(L[12])
    long_pre = pre
    pre2 = 0
    pre1 = 0
    pre2 = int(L[58])
    pre1 = int(L[57])
    if pre2:
      long_pre = pre2
    elif pre1:
      long_pre = pre1
    tba = int(L[4]) * 2
    backswing = frame + 1 - long_pre
    atkfreq = long_pre + max(backswing, tba - 1)
    outs.append((backswing, atkfreq))

print('[%s]' % ','.join(map(lambda x: '[%d,%d]' % x , outs)))

