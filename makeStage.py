#!/usr/bin/python
import os
import sys
import re
import json

opened_fds = []

_listdir = os.listdir
os.listdir = lambda x: sorted(_listdir(x))

def getFile(filename):
    return open(filename, encoding='utf-8-sig')

class readCSV:
    def __init__(self, path):
        if type(path) is str:
            self.fd = open(path, encoding='utf-8-sig')
        else:
            self.fd = path
    def __iter__(self):
        return self
    def __next__(self):
        x = next(self.fd).split('//')[0].rstrip()
        if len(x):
            while len(x) and x[-1] == ',':
                x = x[:-1]
            if len(x):
                return x.split(',')
        raise StopIteration()
    def close(self):
        self.fd.close()
    @property
    def name(self):
        return self.fd.name

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
CH_CASTLES = [45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28,
            27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 46,
            47, 45, 47, 47, 45, 45]
class Stage:
    def __init__(self, id, stm, file, type):
        stm.getData(self)
        self.name = ''
        f = readCSV(file)
        self.id = id
        self.mM = 0 # maxMaterial
        self.eC = 0
        self.eI = -1
        self.eM = -1
        self.eA = -1
        if type == 0:
            line = next(f)
            self.setData(line)
            self.castle = int(line[0])
            if self.castle == -1:
                self.castle = CH_CASTLES[id]
            if stm.cast != -1:
                self.castle += stm.cast * 1000
            if line[1] == '1':
                self.nC = 1
        else:
            self.castle = stm.cast * 1000 + CH_CASTLES[id]
        line = next(f)
        self.len = int(line[0])
        self.H = int(line[1]) # health
        self.iS = int(line[2]) # minSpawn
        self.aS = int(line[3]) # maxSpawn
        self.bg = int(line[4])
        self.max = min(50, int(line[5]))
        self.timeLimit = max(int(line[7]), 0) if len(line) >= 8 else 0
        isBase = int(line[6]) - 2
        ll = []
        intl = 9 if type == 2 else 10
        for line in f:
            if not line[0].isdigit() or line[0] == '0':
                break
            data = [0] * 15
            for i in range(intl):
                if i >= len(line):
                    data[i] = (100)
                else:
                    data[i] = int(line[i])
            data[0] -= 2
            data[2] *= 2
            data[3] *= 2
            data[4] *= 2
            if not self.timeLimit and intl > 9 and data[5] > 100 and data[9] == 100:
                data[9] = data[5]
                data[5] = 100
            if len(line) > 11 and line[11].isdigit():
                data[13] = int(line[11])
                if not data[13]:
                    data[13] = data[9]
            else:
                data[13] = data[9]
            if len(line) > 12 and line[12].isdigit() and int(line[12] == 1):
                data[2] = -data[2]
            if len(line) > 13 and line[13].isdigit():
                data[13] = int(line[13])
            if data[0] == isBase:
                data[5] = 0
            ll.append(data)
        self.l = ll

    def __repr__(self):
        return '<%s>' % self.name

    def toJSON(self, f):
        x = {}
        for k, v in vars(self).items():
            if k != 'id':
                x[k] = v
        json.dump(x, f, separators=(',', ':'), ensure_ascii=False)

    def setData(self, strs):
        chance = int(strs[2])
        self.eC = chance # exChance
        self.eM = int(strs[3]) # exMapID
        self.eI = int(strs[4]) # exStageIDMin
        self.eA = int(strs[5]) # exStageIDMax
    def setInfo(self, data):
        self.e = int(data[0]) # energy
        self.xp = int(data[1])
        self.m0 = int(data[2]) # mus0
        # self.mush = int(data[3])
        self.m1 = int(data[4]) # mus1
        self.once = int(data[-1])
        isTime = len(data) > 15
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
        isMulti = not isTime and len(data) > 9
        self.drop = []
        self.rand = 0
        if len(data) == 6:
            pass
        elif not isMulti:
            self.drop.append(None)
        else:
            l = (len(data) - 7) // 3
            self.drop.append(None)
            self.rand = int(data[8])
            for i in range(1, l):
                self.drop.append([0, 0, 0])
                for j in range(3):
                    self.drop[-1][j] = int(data[6 + i * 3 + j])
        if len(self.drop):
            self.drop[0] = [int(data[5]), int(data[6]), int(data[7])]

class StageMap:
    def __init__(self, file, ID, cast=-1):
        opened_fds.append(self)
        self.name = ''
        self.id = ID
        self.mD = [] # materialDrop
        self.mP = [] # multiplier
        self.list = {}
        self.cast = cast
        self.file = readCSV(file)
        line = next(self.file)
        if len(line) > 3:
            self.rand = int(line[1])
            self.time = int(line[2])
            self.lim = int(line[3])
        self.wT = 0 # waitTime
        self.cL = 0 # clearLimit
        self.rM = 0 # resetMode
        #self.hiddenUponClear = False 
        self.starMask = 0
        self.stars = []
        next(self.file)

    def toJSON(self, f):
        x = {}
        for k, v in vars(self).items():
            if k not in ('id', 'file', 'list'):
                x[k] = v
        json.dump(x, f, separators=(',', ':'), ensure_ascii=False)

    def __repr__(self):
        return '%s:<%d stages>' % (self.name, len(self.list))

    def getData(self, stage):
        try:
            stage.setInfo(next(self.file))
        except StopIteration:
            pass

    def setDrop(self, line):
        for i in range(13, len(line)):
            self.mD.append(int(line[i]))
        for i in range(1, 5):
            self.mP.append(float(line[i]))
        for idx, stage in self.list.items():
            stage.mM = int(line[5 + idx])

class DefMapColc:
    def __init__(self, ID = None, stages = None, maps = None):
        self.name = ''
        self.maps = {}
        if ID is None:
            self.id = 3
            MapColcs[3] = self
            abbr = './org/stage/CH/stageNormal/stageNormal'
            files = (
                getFile(abbr + '0_0_Z.csv'),
                getFile(abbr + '0_1_Z.csv'),
                getFile(abbr + '0_2_Z.csv'),
                getFile(abbr + '1_0.csv'),
                getFile(abbr + '1_1.csv'),
                getFile(abbr + '1_2.csv'),
                getFile(abbr + '2_0.csv'),
                getFile(abbr + '2_1.csv'),
                getFile(abbr + '2_2.csv'),
                getFile(abbr + '0.csv'),
                getFile(abbr + '1_0_Z.csv'),
                getFile(abbr + '2_2_Invasion.csv'),
                getFile(abbr + '1_1_Z.csv'),
                getFile(abbr + "1_2_Z.csv"),
                getFile('./org/stage/DM/MSDDM/MapStageDataDM_000.csv'),
                getFile(abbr + '2_0_Z.csv')
            )
            self.maps[0] = StageMap(files[0], 0, 1)#.name = 'Eoc 1 Zombie';
            self.maps[1] = StageMap(files[1], 1, 1)#.name = 'Eoc 2 Zombie';
            self.maps[2] = StageMap(files[2], 2, 1)#.name = 'Eoc 3 Zombie';
            self.maps[3] = StageMap(files[3], 3, 2)#.name = 'ItF 1';
            self.maps[4] = StageMap(files[4], 4, 2)#.name = 'ItF 2';
            self.maps[5] = StageMap(files[5], 5, 2)#.name = 'ItF 3';
            self.maps[6] = StageMap(files[6], 6, 3)#.name = 'CotC 1';
            self.maps[7] = StageMap(files[7], 7, 3)#.name = 'CotC 2';
            self.maps[8] = StageMap(files[8], 8, 3)#.name = 'CotC 3';
            self.maps[9] = StageMap(files[9], 9, 2)#.name = "EoC 1-3";
            self.maps[10] = StageMap(files[10], 10, 2)#.name = "ItF 1 Zombie";
            self.maps[11] = StageMap(files[11], 11,2)#.name = "CotC 3 Invasion";
            self.maps[12] = StageMap(files[12], 12, 2)#.name = 'ItF 2 Zombie';
            self.maps[13] = StageMap(files[13], 13, 2)#.name = "ItF 3 Zombie";
            self.maps[14] = StageMap(files[14], 14, 0)
            self.maps[15] = StageMap(files[15], 15, 3)#"CotC 1 Zombie'))

            for vf in os.listdir('./org/stage/CH/stageZ/'):
                path = './org/stage/CH/stageZ/' + vf
                ms = re.findall(pattern, vf)
                if len(ms) != 2:
                    continue
                id0 = int(ms[0])
                id1 = int(ms[1])
                with getFile(path) as vf:
                    if id0 < 3:
                        m = self.maps[id0]
                        m.list[id1] = Stage(id1, m, vf, 0)
                    elif id0 == 4:
                        m = self.maps[10]
                        m.list[id1] = Stage(id1, m, vf, 0)
                    elif id0 == 5:
                        m = self.maps[12]
                        m.list[id1] = Stage(id1, m, vf, 0)
                    elif id0 == 6:
                        m = self.maps[13]
                        m.list[id1] = Stage(id1, m, vf, 0)
                    elif id0 == 7:
                        m = self.maps[15]
                        m.list[id1] = Stage(id1, m, vf, 0)

            for vf in os.listdir('./org/stage/CH/stageW/'):
                path = './org/stage/CH/stageW/' + vf
                ms = re.findall(pattern, vf)
                if len(ms) != 2:
                    continue
                id0 = int(ms[0])
                id1 = int(ms[1])
                with getFile(path) as vf:
                    m = self.maps[id0 - 1]
                    m.list[id1] = Stage(id1, m, vf, 1)

            for vf in os.listdir('./org/stage/CH/stageSpace/'):
                with getFile('./org/stage/CH/stageSpace/' + vf) as f:
                    if len(vf) > 20:
                        m = self.maps[11]
                        m.list[0] = Stage(0, m, f, 0)
                    else:
                        ms = re.findall(pattern, vf)
                        if len(ms) == 2:
                            id0 = int(ms[0])
                            id1 = int(ms[1])
                            m = self.maps[id0 - 1]
                            m.list[id1] = Stage(id1, m, f, 1)

            for vf in os.listdir('./org/stage/CH/stage/'):
                ms = re.findall(pattern, vf)
                if len(ms):
                    id0 = int(ms[0])
                    m = self.maps[9]
                    with getFile('./org/stage/CH/stage/' + vf) as f:
                        m.list[id0] = Stage(id0, m, f, 2)
            self.maps[9].stars = [100, 150, 400]
            for vf in os.listdir('./org/stage/DM/StageDM/'):
                ms = re.findall(pattern, vf)
                if len(ms) == 2:
                    id0 = int(ms[0])
                    id1 = int(ms[1])
                    m = self.maps[14]
                    with getFile('./org/stage/DM/StageDM/' + vf) as f:
                        m.list[id1] = Stage(id1, m, f, 0)
            return
        self.name = ''
        self.id = ID
        MapColcs[ID] = self
        for m in maps:
            _id = int(m[1][-7:-4:])
            self.maps[_id] = StageMap(getFile('/'.join(m)), _id)
        for s in stages:
            ms = re.findall(pattern, s[1])
            if len(ms) != 2:
                continue
            stm = self.maps[int(ms[0])]
            with getFile('/'.join(s)) as f:
                stm.list[int(ms[1])] = Stage(ms[1], stm, f, 0)

    def toJSON(self, f):
        x = {}
        for k, v in vars(self).items():
            if k != 'id' and k != 'maps':
                x[k] = v
        json.dump(x, f, separators=(',', ':'), ensure_ascii=False)

    def __repr__(self):
        L = []
        for i in sorted(self.maps.keys()):
            L.append(str(self.maps[i]))
        return ','.join(L)

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
        for fi in os.listdir('./org/stage'):
            if fi in ("CH", "D", "DM"):
                continue
            _list = os.listdir('./org/stage/' + fi)
            _list.sort(key=lambda x: 'MSD' in x, reverse=True)
            _map = _list[0]
            stage = []
            for i in range(1, len(_list)):
                if "stageRN-1" in _list[i] and fi == "N":
                    continue
                stage.extend(map(lambda x: ('./org/stage/' + fi + '/' + _list[i] + '/', x), os.listdir('./org/stage/' + fi + '/' + _list[i])))
            DefMapColc(idmap[fi], stage, map(lambda x: ('./org/stage/' + fi + '/' + _map + '/', x), os.listdir('./org/stage/' + fi + '/' + _map)))
            for fd in opened_fds:
                fd.file.close()
            opened_fds.clear()
        DefMapColc()
        for fd in opened_fds:
            fd.file.close()
        opened_fds.clear()
        map_option = readCSV('./org/data/Map_option.csv')
        ex_lottery = readCSV('./org/data/EX_lottery.csv')
        ex_group = readCSV('./org/data/EX_group.csv')
        drop_item = readCSV('./org/data/DropItem.csv')
        next(map_option)
        for line in map_option:
            strs = line
            sm = DefMapColc.getMap(int(strs[0]))
            if not sm: continue
            stars_len = int(strs[1])
            for i in range(stars_len):
                sm.stars.append(int(strs[2 + i]))
            sm.starMask = int(strs[12])
            sm.rM = int(strs[7])
            sm.cL = int(strs[8])
            #sm.hiddenUponClear = strs[13] != '0'
            sm.wT = int(strs[10])
        exLottery = []
        for line in ex_lottery:
            if len(line) >= 2:
                #m = DefMapColc.getMap(line[0])
                #if not m: continue
                #s = m.list[int(line[1])]
                exLottery.append(line[0] + '/' + line[1])
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
            s.exS = exStage
            s.exC = exChance
        next(drop_item)
        for line in drop_item:
            if len(line) != 22 and len(line) != 30:
                continue
            m = DefMapColc.getMap(line[0])
            if m:
                m.setDrop(line)
        with open('./org/data/LockSkipData.csv') as f:
            for line in f:
                ids = re.findall(pattern, line)
                if len(ids) >= 2:
                    if ids[0] == '0':
                        MapColcs[int(ids[1]) // 1000].gc = 0
                    else:
                        m = DefMapColc.getMap(ids[1])
                        m.gc = 0

def applyNames(file, lang):
    for line in file:
        strs = line.rstrip().split('\t')
        if len(strs) == 1:
            continue
        idstr = strs[0].rstrip()
        name = strs[-1].rstrip()
        if not len(idstr) or not len(name):
            continue
        ids = idstr.split('-')
        mc = MapColcs.get(int(ids[0]))
        if not mc:
            continue
        if len(ids) == 1:
            setattr(mc, lang, name)
            continue
        stm = mc.maps.get(int(ids[1]))
        if stm:
            if len(ids) == 2:
                setattr(stm, lang, name)
                continue
            st = stm.list.get(int(ids[2]))
            if st:
                setattr(st, lang, name)

DefMapColc.read()
with getFile('assets/lang/zh/StageName.txt') as zh:
    applyNames(zh, 'name')
with getFile('assets/lang/jp/StageName.txt') as jp:
    applyNames(jp, 'jpname')
MapColcs[3].name = '主要大章節'
MapColcs[3].jpname = ''

for k1, v1 in MapColcs.items():
    d = './stages/' + str(k1)
    try:
        os.mkdir(d)
    except FileExistsError:
        pass
    with open(d + '/' + 'info', 'w') as f:
        v1.toJSON(f)
    for k2, v2 in v1.maps.items():
        D = d + '/' + str(k2)
        try:
            os.mkdir(D)
        except FileExistsError:
            pass
        with open(D + '/' + 'info', 'w') as f:
            v2.toJSON(f)
        for k3, v3 in v2.list.items():
            with open(D + '/' + str(k3), 'w') as f:
                v3.toJSON(f)

os.system('zip out/stages stages -r > /dev/null')
os.system('rm -r stages')

