import os

outs = []

def getFile(name):
    return list(map(lambda x: x.split(','), open(name).read().replace('\r', '').split('\n')))

for ID in sorted(os.listdir('./org/unit')):
    outs.append([])
    unit_file = getFile(f'./org/unit/{ID:03}/unit{ID:03}.csv')
    for lvc in range(3):
        p = 'fcs'[lvc]
        try:
            anim_file = getFile(f'./org/unit/{ID:03}/{p}/{ID:03}_{p}02.maanim')
        except FileNotFoundError:
            outs[-1].append((44, 471))
            continue
        L = unit_file[lvc]
        pre = int(L[13])
        long_pre = pre
        pre2 = 0
        pre1 = 0
        if len(L) >= 63:
          pre2 = int(L[62])
          pre1 = int(L[61])
        if pre2:
          long_pre = pre2
        elif pre1:
          long_pre = pre1
        tba = int(L[4]) * 2
        frame = 0
        for line in anim_file:
            if len(line) == 4:
                frame = max(frame, int(line[0]))
        backswing = frame + 1 - long_pre
        atkfreq = long_pre + max(backswing, tba - 1)
        outs[-1].append((backswing, atkfreq))

print('[%s]' % ','.join(map(lambda x: '[%s]' % ','.join(map(lambda y: '[%s]' % ','.join(map(str, y)), x)), outs)))

