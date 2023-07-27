def imgcut(filename = './org/page/img015.imgcut'):
    lines = open(filename).readlines()[2::]
    name = lines[0]
    n = int(lines[1])
    cuts = []
    for i in range(n):
        x = lines[i + 2].strip().split(',')
        cuts.append([int(x[k]) for k in range(4)] + [x[4] if len(x) > 4 else ''])
    return cuts

import sys

counter = 0

def css(name, l=None):
    #print('<span class="bc-icon bc-icon-%s"></span>' % name)
    #return
    if l is None:
      l = counter + 1
    globals()['counter'] = l
    l = imgs[l]
    width = max(l[2] + 2, 1)
    height = max(l[3] + 2, 1)
    x = - max(l[0] - 1, 0)
    y = - max(l[1] - 1, 0)
    sys.stdout.write(
'''.bc-icon-''' + name +  ''' {
  width: ''' + str(width) +  '''px;
  height: ''' + str(height) + '''px;
  background-position: ''' + str(x) +  '''px ''' + str(y) + '''px;
}\n'''
    )
sys.stdout.write('''\
.bc-icon {
    display: inline-block;
    background-image: url(/data/page/img015.png);  
    vertical-align: bottom;
}\n''')
imgs = imgcut()
css('trait-red', 77)
css('trait-float')
css('trait-black')
css('trait-metal')
css('trait-angel')
css('trait-alien')
css('trait-zombie')
css('trait-relic')
css('trait-demon')
css('trait-white')
css('imu-curse', 116)
css('weak', 195)
css('strong')
css('stop')
css('slow')
css('lethal')
css('atkbase')
css('crit', 201)
css('bsthunt', 302)
css('kb', 207)
css('wave', 208)
css('imu-wave', 210)
css('area-atk', 211)
css('ld-atk', 212)
css('single-atk', 217)
css('omni-atk', 112)
css('imu-atk', 231)
css('imu-volc', 243)
css('massive', 206)
css('metalic', 209)
css('only', 202)
css('good', 203)
css('resist', 204)
css('resists', 122)
css('bounty', 205)
css('imu-weak', 213)
css('imu-stop', 214)
css('imu-slow', 215)
css('imu-kb', 216)
css('imu-poiatk', 237)
css('mini-wave', 293)
css('curse', 289)
css('shieldbreak', 296)
css('volc', 239)
css('warp', 266)
css('break', 264)
css('imu-warp', 262)
css('mini-volc', 310)
css('z-kill', 260)
css('waves', 218)
css('wkill', 258)
css('s', 229)
css('bail', 297)
css('ckill', 300)
css('shield-break', 296)
css('ekill', 110)
css('massives', 114)
css('res-weak', 42)
css('res-freeze', 44)
css('res-slow', 46)
css('res-kb', 48)
css('res-wave', 50)
css('res-warp', 52)
css('res-curse', 108)
css('res-toxic', 234)
css('res-surge', 240)
css('res-weak2', 43)
css('res-freeze2', 45)
css('res-slow2', 47)
css('res-kb2', 49)
css('res-wave2', 51)
css('res-warp2', 53)
css('res-curse2', 109)
css('res-toxic2', 235)
css('res-surge2', 241)
css('toxic', 233)


