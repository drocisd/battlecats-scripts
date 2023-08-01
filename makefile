python=python3

all: icon anim2 anim1 combo name stage level units

pre:
	mkdir -p stages
	mkdir -p out
	mkdir -p out/data/lang
	mkdir -p out/gacha
	mkdir -p out/data/lang/zh
	mkdir -p out/data/lang/jp

icon: pre
	$(python) iconMaker.py > out/icons.css

anim2: pre
	$(python) backswingMaker.py > out/anim2

anim1: pre
	$(python) backswingMaker1.py > out/anim1

combo: pre
	$(python) comboMaker.py > out/combo.js

gacha: pre
	$(python) gachaPool.py

name: pre
	$(python) makeName.py '' assets/lang/zh/EnemyName.txt > out/enemyName.json
	$(python) makeName.py '' assets/lang/jp/EnemyName.txt > out/enemyNameJP.json
	$(python) makeName.py 'const unit_names='  assets/lang/zh/UnitName.txt > out/data/lang/zh/UnitName.js
	$(python) makeName.py 'const unit_names_jp=' assets/lang/jp/UnitName.txt > out/data/lang/jp/UnitName.js
	$(python) makeName.py 'const unit_descs=' assets/lang/zh/UnitExplanation.txt > out/data/lang/zh/UnitExplanation.js

stage: pre
	$(python) makeStage.py

level: pre
	$(python) levelMaker.py > out/unitlevels.js

units:
	mkdir -p all
	$(python) makeUnits.py
	zip ../battlecatsinfo.github.io/all_units all -r
	rm -r all

update:
	cp org/data/SkillAcquisition.csv ../battlecatsinfo.github.io/data/data/SkillAcquisition.csv
	cp org/data/t_unit.csv ../battlecatsinfo.github.io/data/data/t_unit.csv
	cp org/data/unitexp.csv ../battlecatsinfo.github.io/data/data/unitexp.csv
	cp org/data/SkillLevel.csv ../battlecatsinfo.github.io/data/data/SkillLevel.csv
	cp org/data/unitbuy.csv ../battlecatsinfo.github.io/data/data/unitbuy.csv
	cp org/data/unitlevel.csv ../battlecatsinfo.github.io/data/data/unitlevel.csv
	cp org/data/unitlevel.csv ../battlecatsinfo.github.io/data/data/unitlevel.csv
	cp org/enemy ../battlecatsinfo.github.io/data/ -r -u
	cp org/unit ../battlecatsinfo.github.io/data/ -r -u
	cp org/img ../battlecatsinfo.github.io/data/ -r -u
clean:
	rm -r stages
	rm -r out
	rm -r all
