import os
import sys
import re

def readCSV(filename):
    if type(filename) is str:
        filename = open(filename)
    for line in filename:
        x = line.split('//')[0].rstrip()
        if len(x):
            if x[-1] == ',':
                x = x[:-1]
            yield x.split(',')

idmap = {
        "E": 4,
        "N": 0,
        "S": 1,
        "C": 2,
        "CH": 3,
        "T": 6,
        "V": 7,
        "R": 11,
        "M": 12,
        "A": 13,
        "B": 14,
        "RA": 24,
        "H": 25,
        "CA": 27,
        "Q": 31,
        "L": 33,
        "ND": 34
}

MapColcs = {}
pattern = re.compile('\\d+')

class Stage:
    def __init__(self, id, stm, file, type):
        f = readCSV(file)
        self.id = id
        self.maxMaterial = 0
        self.exConnection = False
        self.exChance = 0
        self.exMapID = -1
        self.exStageIDMin = -1
        self.exStageIDMax = -1
        if type == 0:
            line = next(f)
            self.setData(line)
    def __repr__(self):
        return '<stage>'
    def setData(self, strs):
        chance = int(strs[2])
        self.exConnection = chance != 0
        self.exChance = chance
        self.exMapID = int(strs[3])
        self.exStageIDMin = int(strs[4])
        self.exStageIDMax = int(strs[5])
    def setInfo(self, data):
        self.energy = int(data[0])
        self.xp = int(data[1])
        self.mus0 = int(data[2])
        self.mush = int(data[3])
        self.mus1 = int(data[4])
        self.once = data[-1]
        isTime = data.length > 15
        if isTime:
            for i in range(8, 15):
                if data[i] != '-2':
                    isTime = False
                    break
        self.time = []
        if isTime:
            l = (len(data) - 17) // 3
            for i in range(l):
                self.time.append([])
                for j in range(3):
                    self.time[-1].append(int(data[16 + i * 3 + j]))
        isMulti = not isTime and data.length > 9
        self.drop = []
        self.rand = 0
        if data.length != 6:
            pass
        elif not isMulti:
            self.drop.append(None)
        else:
            l = (len(data) - 7) / 3
            self.drop.append(None)
            for i in range(1, l):
                self.drop.append([])
                for j in range(3):
                    self.drop[-1][j] = data[6 + i * 3 + j]
        if len(self.drop):
            self.drop[0] = [data[5], data[6], data[7]]

class StageMap:
    def __init__(self, file, ID):
        self.id = ID
        self.materialDrop = []
        self.multiplier = []
        self.list = {}
        self.file = readCSV(file)
        line = next(self.file)
        if len(line) > 3:
            self.rand = int(line[1])
            self.time = int(line[2])
            self.lim = int(line[3])
        self.waitTime = 0
        self.clearLimit = 0
        self.resetMode = 0
        next(self.file)
    def __repr__(self):
        return '<%d stages>' % len(self.list)
    def getData(self, stage):
        stage.setInfo(next(self.file))
    def setDrop(self, line):
        for i in range(13, len(line)):
            self.materialDrop.append(int(line[i]))
        for i in range(1, 5):
            self.multiplier.append(float(line[i]))
        for idx, stage in self.list.items():
            stage.maxMaterial = int(line[5 + idx])

class DefMapColc:
    def __init__(self, st, ID, stages, maps):
        self.name = st
        self.id = ID
        self.maps = {}
        MapColcs[ID] = self
        for m in maps:
            _id = int(m[1][-7:-4:])
            with open('/'.join(m)) as f:
                self.maps[_id] = StageMap(f, _id)
        for s in stages:
            ms = re.findall(pattern, s[1])
            if len(ms) != 2:
                continue
            stm = self.maps[int(ms[0])]
            with open('/'.join(s)) as f:
                stm.list[int(ms[1])] = Stage(ms[1], stm, f, 0)
    def __repr__(self):
        L = []
        for i in sorted(self.maps.keys()):
            L.append(str(self.maps[i]))
        return '{%s}' % ','.join(L)
    @staticmethod
    def getMap(mid):
        if type(mid) is str:
            mid = int(mid)
        s = MapColcs.get(mid // 1000)
        if s:
            return s.maps.get(mid % 1000)
        return None
    @staticmethod
    def read():
        map_option = readCSV('./org/data/Map_option.csv') # 
        ex_lottery = readCSV('./org/data/EX_lottery.csv') #
        ex_group = readCSV('./org/data/EX_group.csv') # 
        drop_item = readCSV('./org/data/DropItem.csv') # drop items(rewards)
        lock_skip = readCSV('./org/data/LockSkipData.csv') # can't use gold CP
        
        for fi in os.listdir('./org/stage'):
            if fi in ("CH", "D", "DM") or fi == "N":
                continue
            _list = os.listdir('./org/stage/' + fi)
            _list.sort(key=lambda x: 'MSD' in x, reverse=True)
            _map = _list[0]
            stage = []
            for i in range(1, len(_list)):
                if "stageRN-1" in _list[i]:
                    continue
                stage.extend(map(lambda x: ('./org/stage/' + fi + '/' + _list[i] + '/', x), os.listdir('./org/stage/' + fi + '/' + _list[i])))
            DefMapColc(fi, idmap[fi], stage, map(lambda x: ('./org/stage/' + fi + '/' + _map + '/', x), os.listdir('./org/stage/' + fi + '/' + _map)))

        next(map_option)
        for line in map_option:
            strs = line
            _id = int(strs[0])
            stars_len = int(strs[1])
            stars = []
            for i in range(stars_len):
                stars.append(int(strs[2 + i]))
            starMask = int(strs[12])
            resetMode = int(strs[13])
            clearLimit = int(strs[8])
            hiddenUponClear = strs[13] != '0'
            waitTime = int(strs[10])
        exLottery = []
        for line in ex_lottery:
            if len(line) >= 2:
                m = DefMapColc.getMap(line[0])
                if not m: continue
                s = m.list[int(line[1])]
                exLottery.append(s)
        for line in ex_group:
            maxPercentage = int(line[0])
            m = DefMapColc.getMap(line[1])
            if not m:
                continue
            s = m.list[int(line[2])]
            if not s:
                continue
            exLength = len(line) - 3
            if exLength & 1:
                print("Invalid Ex group format", line, file=sys.stderr)
                continue
            exLength >>= 1
            exStage = []
            exChance = []
            for i in range(exLength):
                _id = int(line[i+i+3])
                exStage.append(exLottery[_id])
                c = maxPercentage * (int(line[i+i+4])/100);
                exChance.append(c)
                maxPercentage -= c
            maxPercentage = int(line[0])
            for i in range(exLength):
                exChance[i] /= maxPercentage / 100;
        next(drop_item)
        for line in drop_item:
            if len(line) != 22 and len(line) != 30:
                continue
            m = DefMapColc.getMap(line[0])
            if m:
                m.setDrop(line)

DefMapColc.read()
for key, val in MapColcs.items():
    print('===================================================================================================================== %d =====================================================================================================================' % key)
    print(val, end='\n\n')
