#!/usr/bin/python
unit_names = []
unit_descs = []
unit_names_jp = []
unit_descs_jp = []
for line in open('assets/lang/zh/UnitName.txt'):
    y = line.replace('\n', '').replace('\r', '').split('\t')
    unit_names.append(y[1::])
for line in open('assets/lang/zh/UnitExplanation.txt'):
    y = line.replace('\n', '').replace('\r', '').split('\t')
    unit_descs.append(y[1::])
for line in open('assets/lang/jp/UnitName.txt'):
    y = line.replace('\n', '').replace('\r', '').split('\t')
    unit_names_jp.append(y[1::])
for line in open('assets/lang/jp/UnitExplanation.txt'):
    y = line.replace('\n', '').replace('\r', '').split('\t')
    unit_descs_jp.append(y[1::])

pools = [
#zh-name, jp-name, en-name, collab, Cats tuple, banner, Optional[button image]
('貓咪轉蛋+', 'にゃんこガチャ+', 'Cat Capsules+', False, (0, 1, 2, 3, 4, 5, 6, 7, 8, 643), '/res/0.png', 'https://cdn.discordapp.com/attachments/928637473221922827/928637490988974090/gatya_n_btn08.png'),
('常駐稀有貓', 'レアキャラ', 'Rare Cats', False, (37, 38, 41, 46, 47, 48, 49, 50, 51, 52, 55, 56, 58, 145, 146, 147, 148, 149, 197, 198, 325, 376, 495, 523), '/res/1.png', ''),
('常駐激稀有貓', '激レアキャラ', 'Super Rare Cats', False, (30, 31, 32, 33, 35, 36, 39, 40, 61, 150, 151, 152, 377), '/res/2.png', ''),
('土龍鑽部隊', 'グランドン部隊', 'Grandon Mining Corps', False, (443, 444, 445, 446, 447), '/res/3.png', ''),
('限定激稀有系列', 'キャンペーン', 'Neneko and Gang', False, (129, 131, 144, 200), '/res/4.png', ''),
('貓咪軍團支援隊', 'にゃんこ軍団支援隊', 'Reinforcements', False, (237, 238, 239), '/res/5.png', ''),
('洗腦貓', '洗脳ネコ', 'Brainwashed Cats', False, (629, 636, 645, 654, 662, 667, 684, 688, 694), '/res/6.png', ''),
('狂亂貓', '狂乱のネコ', 'Crazed Cats', False, (91, 92, 93, 94, 95, 96, 97, 98, 99), '/res/7.png', ''),
('殺意貓', '殺意のネコ', 'Killer Cats', False, (319, 695), '/res/8.png', ''),
('小小貓', 'ガチャ（イベント）', 'Li\'l Cats', False, (209, 210, 211, 245, 246, 247, 311, 312, 313), '/res/9.png', ''),
('EX罐頭購買貓', 'ネコカン購入のEXネコ', 'Purchasable Special Cats', False, (18, 21, 20, 19, 14, 22, 12, 13, 10, 9, 23, 15, 11), '/res/13.png', ''),
('世界/未來/宇宙/魔界掉落貓', '世界/未来/宇宙/魔界ドロップネコ', 'Main Chapters Unlockable', False, (16, 123, 24, 25, 437, 462, 622), '/res/10.png', ''),
('傳說關卡掉落貓', 'レジェンドステージドロップネコ', 'Legend Chapters Unlockable', False, (130, 172, 268, 323, 426, 528, 464, 532, 613, 653, 691, ), '/res/11.png', ''),
('風雲貓咪塔掉落貓', '風雲にゃんこ塔ドロップネコ', 'Heavenly Tower Unlockable', False, (352, 383, 554), '/res/14.png', ''),
('遠古的蛋', '古びたタマゴ', 'Ancient Eggs', False, (656, 658, 659, 663, 664, 665, 669, 670, 675, 676, 685, 691, 697, 700, 706, 707, 713, ), '/res/12.png', ''),
('超級貓咪祭', '超ネコ祭', 'Uberfest', False, (269, 318, 380, 529, 585, 641, 690), '/bnr/gatya_bnr813.png', 'https://cdn.discordapp.com/attachments/931422469477244948/931531721562783805/gatya_btn19.png'),
('特級貓咪祭', '極ネコ祭', 'Epicfest', False, (333, 378, 441, 543, 609, 657, 705), 'https://cdn.discordapp.com/attachments/934738752557948968/1121265865392922716/15NP1fQsUdP2XGoA8AAAAASUVORK5CYII.png', 'https://cdn.discordapp.com/attachments/931422469477244948/931531722816901130/gatya_btn27.png'),
('傳說中的不明貓一族', '伝説のネコルガ族', 'Tales of the Nekoluga', False, (461, 34, 168, 169, 170, 171, 240, 436, 546, 625, 519), 'https://cdn.discordapp.com/attachments/934738752557948968/1121265864839282708/fD6H1v8ugkDkFJXRqAAAAAElFTkSuQmCC.png', 'https://cdn.discordapp.com/attachments/931422469477244948/931531418285269022/gatya_btn00.png'),
('超激烈爆彈', '超激ダイナマイツ', 'The Dynamites', False, (42, 455, 447, 446, 445, 444, 443, 427), 'https://cdn.discordapp.com/attachments/934738752557948968/999142985549754368/gatya_bnr741.png', 'https://cdn.discordapp.com/attachments/931422469477244948/931531418608205824/gatya_btn01.png'),
('戰國武神巴薩拉斯', '戦国武神バサラーズ', 'Sengoku Wargods Vajiras', False, (448, 71, 72, 73, 124, 125, 158, 338, 496, 649), 'https://cdn.discordapp.com/attachments/934738752557948968/1022805947132944394/gatya_bnr708.png', 'https://cdn.discordapp.com/attachments/931422469477244948/931531418859872256/gatya_btn02.png'),
('電腦學園銀河美少女', '電脳学園ギャラクシーギャルズ', 'Cyber Academy Galaxy Gals', False, (449, 75, 76, 105, 106, 107, 159, 351, 502, 471), 'https://cdn.discordapp.com/attachments/934738752557948968/956848269928046592/gatya_bnr693.png', 'https://cdn.discordapp.com/attachments/931422469477244948/931531419098972160/gatya_btn03.png'),
('超破壞大帝龍皇因佩拉斯', '超破壊大帝ドラゴンエンペラーズ', 'Lords of Destruction Dragon Emperors', False, (450, 83, 84, 85, 86, 87, 177, 396, 505, 620, 660), 'https://cdn.discordapp.com/attachments/934738752557948968/934741353127096330/gatya_bnr632.png', 'https://cdn.discordapp.com/attachments/931422469477244948/931531419346427924/gatya_btn04.png'),
('超古代勇者超級靈魂勇者', '超古代勇者ウルトラソウルズ', 'Ancient Heroes Ultra Souls', False, (451, 134, 135, 136, 137, 138, 203, 322, 525, 633, 692), 'https://cdn.discordapp.com/attachments/934738752557948968/1002132918921085018/gatya_bnr659.png', ''),
('逆襲的戰士黑暗英雄', '逆襲の英雄ダークヒーローズ', 'Justice Strikes Back: Dark Heroes', False, (481, 194, 195, 196, 212, 226, 261, 431, 533, 634), 'https://cdn.discordapp.com/attachments/934738752557948968/1093139109553373194/B5OyJB4Z414bAAAAAElFTkSuQmCC.png', 'https://cdn.discordapp.com/attachments/931422469477244948/931531420059459604/gatya_btn07.png'),
('究極降臨巨神宙斯', '究極降臨ギガントゼウス', 'The Almighties The Majestic Zeus', False, (493, 257, 258, 259, 271, 272, 316, 439, 534), 'https://cdn.discordapp.com/attachments/934738752557948968/1022805078660350013/gatya_bnr679.png', 'https://cdn.discordapp.com/attachments/931422469477244948/931531721386639410/gatya_btn18.png'),
('革命軍隊鋼鐵戰團', '革命軍隊アイアンウォーズ', 'Frontline Assault Iron Legion', False, (463, 304, 305, 306, 355, 417, 594, 632, 674), 'https://cdn.discordapp.com/attachments/934738752557948968/934741353701707856/gatya_bnr645.png', 'https://cdn.discordapp.com/attachments/931422469477244948/931531722443616256/gatya_btn24.png'),
('古靈精怪元素小精靈', '大精霊エレメンタルピクシーズ', "Nature's Guardians Elemental Pixies", False, (478, 359, 360, 361, 401, 569, 631, 655), 'https://cdn.discordapp.com/attachments/934738752557948968/962935258238566450/gatya_bnr718.png', 'https://cdn.discordapp.com/attachments/931422469477244948/931532097808650260/gatya_btn33.png'),
('絕命美少女怪物萌娘隊', '絶命美少女ギャルズモンスターズ', 'Girls & Monsters: Angels of Terror', True, (544, 334, 335, 336, 337, 357, 358, 607, 682), 'https://cdn.discordapp.com/attachments/934738752557948968/1032943982507999242/gatya_bnr761.png', 'https://cdn.discordapp.com/attachments/931422469477244948/931532096789413918/gatya_btn28.png'),
('情人節淑女們', 'バレンタインギャルズ', 'Valentine Gals', False, (644, 588, 589, 587), 'https://cdn.discordapp.com/attachments/934738752557948968/1075738419231215686/gatya_bnr795.png', 'https://cdn.discordapp.com/attachments/931422469477244948/931532402097012747/gatya_btn48.png'),
('白色情人節轉蛋', 'ホワイトデーガチャ', 'White Day', True, (693, 648), 'https://cdn.discordapp.com/attachments/934738752557948968/1075738416706240632/gatya_bnr786.png', 'https://cdn.discordapp.com/attachments/934738752557948968/952044289628733523/gatya_btn52.png'),
('復活節嘉年華', 'イースターカーニバル', 'Easter Carnival', False, (330, 331, 595, 699, 332), 'https://cdn.discordapp.com/attachments/934738752557948968/962935259169705994/gatya_bnr724.png', 'https://cdn.discordapp.com/attachments/931422469477244948/931531722615578694/gatya_btn26.png'),
('完美新娘', 'ジューンブライド', 'June Bride', False, (661, 711), '/bnr/gatya_bnr731.png', 'https://cdn.discordapp.com/attachments/931422469477244948/988434782281150504/gatya_btn53.png'),
('夏日美少女團', 'サマーガールズ', 'Gals of Summer', False, (274, 275, 354, 438, 494, 563, 564, 614, 666, 714, 276, 565, 566), 'https://cdn.discordapp.com/attachments/934738752557948968/999142987567214652/gatya_bnr750.png', 'https://cdn.discordapp.com/attachments/931422469477244948/931531721806057512/gatya_btn20.png'),
('萬聖節轉蛋', 'ハロウィンガチャ', 'Halloween Capsules', False, (229, 230, 302, 570, 683, 228), 'https://cdn.discordapp.com/attachments/934738752557948968/1032943982889676811/gatya_bnr766.png', 'https://cdn.discordapp.com/attachments/931422469477244948/931531420332085298/gatya_btn08.png'),
('聖誕美少女', 'クリスマスギャルズ', 'Xmas Gals', False, (241, 242, 243, 310, 526, 584, 687), 'https://cdn.discordapp.com/attachments/934738752557948968/1045660833558052934/gatya_bnr776.png', 'https://cdn.discordapp.com/attachments/931422469477244948/931531420587933746/gatya_btn09.png'),
('紅色破壞者', 'レッドバスターズ', ' Red Busters', False, (283,), 'https://cdn.discordapp.com/attachments/934738752557948968/951772656187871232/gatya_bnr696.png', 'https://cdn.discordapp.com/attachments/931422469477244948/931531419593883658/gatya_btn05.png'),
('漂浮破壞者', 'エアバスターズ', 'Air Busters', False, (286,), 'https://cdn.discordapp.com/attachments/934738752557948968/934740788594753576/gatya_bnr452.png', 'https://cdn.discordapp.com/attachments/931422469477244948/931531722238099536/gatya_btn22.png'),
('鋼鐵破壞者', 'メタルバスターズ', 'Red Busters', False, (397,), 'https://cdn.discordapp.com/attachments/934738752557948968/951770971134652416/gatya_bnr717.png', 'https://cdn.discordapp.com/attachments/931422469477244948/931532097531830353/gatya_btn32.png'),
('波動破壞者', '波動バスターズ', 'Wave Busters', False, (559,), 'https://cdn.discordapp.com/attachments/934738752557948968/934740788993200138/gatya_bnr523.png', 'https://cdn.discordapp.com/attachments/931422469477244948/931532099071123496/gatya_btn45.png'),
('超生命體破壞者', '超生命体バスターズ', 'Colossus Busters', False, (686,), 'https://cdn.discordapp.com/attachments/934738752557948968/1045660832845017098/gatya_bnr772.png', 'https://cdn.discordapp.com/attachments/931422469477244948/1051338708462346282/gatya_btn56.png'),
('超國王祭', '超国王祭', 'Dynasty Fest', False, (586,), 'https://cdn.discordapp.com/attachments/934738752557948968/1093139109326901248/8BTlzYY0APPEsAAAAASUVORK5CYII.png', 'https://cdn.discordapp.com/attachments/931422469477244948/931532401551745025/gatya_btn47.png'),
('女王祭', '女王祭', 'Royal Fest', False, (612,), 'https://cdn.discordapp.com/attachments/934738752557948968/961913286230695936/gatya_bnr699.png', 'https://cdn.discordapp.com/attachments/931422469477244948/931532401551745025/gatya_btn47.png'),
('公主踢騎士Sweets', 'ケリ姫スイーツ', 'Princess Punt', True, (530, 486, 485, 337, 161, 160, 64, 65, 66, 67, 68), '/bnr/gatya_bnr482.png', ''),
('梅露可物語', 'メルクストーリ', 'Merc Storia', True, (506, 346, 345, 344, 190, 189, 188, 187, 186, 185, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119), '/bnr/gatya_bnr414.png', ''),
('活下去！曼波魚！', '生きろ！マンボウ！', 'Survive! Mola Mola!', True, (174, 173), 'https://cdn.discordapp.com/attachments/934738752557948968/1006842402218192977/gatya_bnr485.png', ''),
('消滅都市', '消滅都市', 'Shoumetsu Toshi', True, (180, 270, 341, 482, 428, 429), '/bnr/gatya_bnr505.png', ''),
('越南大戰DEFENSE', 'メタルスラッグディフェンス', 'Metal Slug Defense', True, (215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225), '/bnr/gatya_bnr45.png', ''),
('魔法少女小圓', '魔法少女まどか☆マギカ', 'Puella Magi Madoka Magica', True, (288, 289, 291, 290, 292, 293, 440, 294, 296, 297, 298, 295), '/bnr/gatya_bnr621.png', ''),
('Crash Fever', 'クラッシュフィーバー', 'Crash Fever', True, (326, 327), '/bnr/crash.png', ''),
('劇場版 Fate/stay night', '劇場版 Fate/stay night', "Fate/Stay Night: Heaven's Feel", True, (362, 363, 364, 365, 366, 367, 368, 456, 460, 370, 371, 372, 458, 459), 'https://cdn.discordapp.com/attachments/934738752557948968/1093139111533105172/H2mjFsC667QAAAABJRU5ErkJggg.png', ''),
('實況野球', '実況パワフルプロ野球', 'Power Pro Baseball', True, (393, 394, 395, 390, 391, 392), '/bnr/123.png', ''),
('福音戰士', 'エヴァンゲリオンガチャ', 'Neon Genesis Evangelion', True, (412, 413, 414, 487, 415, 416, 488, 709, 409, 410, 411, 489, 490, 491, 406, 407, 408, 552), '/bnr/gatya_bnr818.png', ''),
('福音戰士 2nd', 'エヴァンゲリオンガチャ 2nd', 'Neon Genesis Evangelion 2nd', True, (547, 548, 549, 550, 551, 710, 409, 410, 411, 489, 490, 491, 406, 407, 408, 552), '/bnr/gatya_bnr819.png', ''),
('聖魔大戰', 'ビックリマン', 'Bikkuriman', True, (467, 468, 469, 470, 471, 555, 472, 556), '/bnr/gatya_bnr524.png', ''),
('快打旋風', 'ストリートファイターV', 'Street Fighter V', True, (510, 511, 512, 513, 514, 515, 516, 517, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580), 'https://cdn.discordapp.com/attachments/934738752557948968/1045660867368333342/gatya_bnr777.png', ''),
('初音未來', '初音ミク', 'Hatsune Miku', True, (535, 536, 537, 560, 582, 583, 590, 561, 591, 562, 592, 593), '/bnr/gatya_bnr583.png', ''),
('亂馬1/2', 'らんま1/2', 'Ranma 1/2', True, (596, 597, 598, 599, 600, 671, 605, 601, 602, 603, 672), 'https://cdn.discordapp.com/attachments/934738752557948968/1016726047787601971/gatya_bnr757.png', ''),
]
def gen1(ID):
	ID3 = str(ID).rjust(3, '0')
	egg = unit_buy[ID]
	if egg >= 0:
		g = str(egg).rjust(3, '0')
		img = '/data/img/m/%s/%s_m.png' % (g, g)
	else:
		img = '/data/unit/%s/f/uni%s_f00.png' % (ID3, ID3)
	try:
		name = unit_names[ID][0]
	except IndexError:
		name = unit_names_jp[ID][0]
	try:
		desc = unit_descs[ID][0]
	except IndexError:
		desc = unit_descs_jp[ID][0]
	return '<td><p>%s</p><a class="B" href="/unit.html?id=%d"><img src="%s"></a>%s</td>' % (name, ID, img, desc)

def gen(i, pool):
	x = i + i
	tr = '<tr>' +  gen1(pool[x])
	x += 1
	if x < len(pool):
		tr += gen1(pool[x])
	tr += '</tr>'
	return tr

unit_buy = tuple(map(lambda x: int(x.split(',')[-2]), open('./org/data/unitbuy.csv').read().rstrip().split('\n')))
content = ''
for pool in pools:
  fn = '/gacha/' + pool[2].replace(' ', '_').replace(':', '_').replace('\'', '_').replace('/', '_').replace('&', '_').replace('!', '_').replace('+', '') + '.html'
  names = '%s/%s/%s' % (pool[0], pool[1], pool[2])
  content += '<h2><a class="B" href="%s">%s</a></h2>' % (fn, names)
  content += '<a class="B" href="%s"><img class="A" src="%s"></a>' % (fn, pool[-2]) #pool[5]
  with open('out' + fn, 'w') as f:
    div = ''
    L = len(pool[4])
    if L & 1:
    	L += 1
    c = ''
    for i in range(L >> 1):
    	c += gen(i, pool[4])
    f.write('''\
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>''' + names + '''</title>
  <link rel="stylesheet" type="text/css" href="/w3.css">
  <link rel="stylesheet" type="text/css" href="/dracula.css">
</head>
<style>
html, body { width: 100%%;margin: 0 auto;padding: 0;background-color: aliceblue;text-align: center; }
.B { display: block; }
table { margin: 0 auto;border-collapse: collapse;margin-top: 50px;box-shadow: 0 0 20px rgba(0, 0, 0, 0.15); }
td { width: 300px;border: #cfcfcf 4px solid; }
p { margin-block-start: 0px;margin-block-end: 0px; }
tbody > a { display: block; }
p { font-size: larger;margin-block-start: 0;margin-block-end: 0; }
.topnav { background-color: #333 !important;margin-block:0; display: inline-block;width: 100%;text-align:center; }
.topnav a { display: inline-block;color: #f2f2f2 !important; padding: 5px 20px; text-decoration: none; font-size: 20px; }
.topnav a.active { background-color: #f2bb00 !important; color: white !important; }
.topnav a:visited { text-decoration: none; }
.w3-dropdown-content > a { color: var(--color) !important;  }
</style>
<body>
	<ul class="topnav">
		<a href="/index.html">主頁</a>
		<a href="/search.html">貓咪</a>
		<a href="/esearch.html">敵人</a>
		<a href="/gachas.html">轉蛋</a>
		<a href="/stage.html">關卡</a>
		<a href="/music.html">音效</a>
		<div class="w3-dropdown-hover"><button class="w3-button" style="color: white !important;"><img src="/theme.svg" style="background-color: initial !important;">Theme</button>
		<div class="w3-dropdown-content w3-bar-block w3-card-4">
        	<a href="#" id="theme-system" class="w3-bar-item w3-button">系統</a>
        	<a href="#" id="theme-dark" class="w3-bar-item w3-button">深色</a>
        	<a href="#" id="theme-light" class="w3-bar-item w3-button">白色</a>
      	</div>
      	</div>
	</ul>
	<script src="/dracula.js"></script>
<h1>''' + names + '''</h1>
<img style="display: block;margin: 0 auto;" src="''' + pool[-2] + '''">
<table><tbody>''' + c + '''</tbody></table>
</body>
</html>
''')

with open("out/gachas.html", 'w') as f:
  f.write('''\
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>轉蛋池一覽</title>
  <link rel="stylesheet" type="text/css" href="w3.css">
  <link rel="stylesheet" type="text/css" href="dracula.css">
</head>
<style>
html, body { width: 100%;margin: 0;padding: 0;}
.B { text-align: center;text-decoration: none;display: block;width: 100%; }
.A { display: block;margin: 0 auto; }
.topnav { background-color: #333 !important;margin-block:0; display: inline-block;width: 100%;text-align:center; }
.topnav a { display: inline-block;color: #f2f2f2 !important; padding: 5px 20px; text-decoration: none; font-size: 20px; }
.topnav a.active { background-color: #f2bb00 !important; color: white !important; }
.topnav a:visited { text-decoration: none; }
.w3-dropdown-content > a { color: var(--color) !important;  }
</style>
<body>
	<ul class="topnav">
		<a href="/index.html">主頁</a>
		<a href="/search.html">貓咪</a>
		<a href="/esearch.html">敵人</a>
		<a href="/gachas.html" class="active">轉蛋</a>
		<a href="/stage.html">關卡</a>
		<a href="/music.html">音效</a>
		<div class="w3-dropdown-hover"><button class="w3-button" style="color: white !important;"><img src="theme.svg" style="background-color: initial !important;">Theme</button>
		<div class="w3-dropdown-content w3-bar-block w3-card-4">
        	<a href="#" id="theme-system" class="w3-bar-item w3-button">系統</a>
        	<a href="#" id="theme-dark" class="w3-bar-item w3-button">深色</a>
        	<a href="#" id="theme-light" class="w3-bar-item w3-button">白色</a>
      	</div>
      	</div>
	</ul>
	<script src="dracula.js"></script>
<div style="margin: 0 auto;text-align: center;width: 100%;">''' + content + '''</div>
</body>
</html>
''')