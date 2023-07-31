combos = []
comboNames = {}

def readNames():
    for line in open("./assets/lang/zh/ComboName.txt"):
        x = line.replace('\n', '').replace('\r', '').split('\t')
        if len(x) != 2: continue
        comboNames[int(x[0])] = x[1]

readNames()

with open('./org/data/NyancomboData.csv') as f:
    for line in f:
        x = tuple(map(int, line.replace('\n', '').replace('\r', '').rstrip(',').split(',')))
        if len(x) <= 13: continue
        if x[1] <= 0: continue
        y = []
        for i in range(5):
            a1 = x[2 + 2 * i]
            a2 = x[3 + 2 * i]
            if a1 == -1 or a2 == -1:
                break
            y.append(a1)
            y.append(a2)
        combos.append('[%s]' % (','.join(map(str, ('"%s"' % comboNames.get(int(x[0]), ''), x[12], x[13], '[%s]' % ','.join(map(str, y)))))))

print('const combos=[%s];' % ','.join(combos))

