#!/usr/bin/python
csvData = (line for line in filter(len, open('./org/data/unitlevel.csv').read().replace('\r', '').replace(' ', '').split('\n')))

groups = {}
curve_index = 0
curMap = []
i = 0

for it in csvData:
    x = groups.get(it, None)
    if x is None:
        x = ([i], curve_index)
        groups[it] = x
        curve_index += 1
    else:
        x[0].append(i)
    curMap.append(str(x[1]))
    i += 1

print('const curveMap=[%s];' % ','.join(curMap))

for k, v in groups.items():
    print('const curveData%i=[%s];' % (v[1], k))

