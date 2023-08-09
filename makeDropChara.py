m = {}
with open('drop_chara.csv') as f:
    next(f)
    for line in f:
        line = line.rstrip().replace('\n', '').split(',')
        if len(line) < 3: continue
        m[int(line[0])] = int(line[2])


print('const drop_chara=' + str(m).replace(' ', '') + ';')

