python=python3

all: icon anim2 anim1 combo name stage level

pre:
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
	$(python) makeName.py assets/lang/zh/UnitName.txt > out/data/lang/zh/UnitName.js
	$(python) makeName.py assets/lang/jp/UnitName.txt > out/data/lang/jp/UnitName.js
	$(python) makeName.py assets/lang/zh/UnitExplanation.txt > out/data/lang/zh/UnitExplanation.js
	$(python) makeName.py assets/lang/jp/UnitExplanation.txt > out/data/lang/jp/UnitExplanation.js

stage: pre
	$(python) makeStage.py

level: pre
	$(python) levelMaker.py > out/unitlevels.js

version: all
	cp -r --update out ../battlecatsinfo.github.io

clean:
	rm -r out
