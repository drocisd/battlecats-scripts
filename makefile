python=python3

all:
	mkdir -p out
	mkdir -p out/lang
	mkdir -p out/lang/zh
	mkdir -p out/lang/jp
	python backswingMaker.py > out/anim1
	python backswingMaker1.py > out/anim2
	python comboMaker.py > out/combo.js
	python gachaPool.py out
	python makeName.py assets/lang/zh/UnitName.txt out/lang/zh/UnitName.js
	python makeStage.py assets/lang/jp/UnitName.txt out/lang/jp/UnitName.js
	python makeName.py assets/lang/zh/UnitExplanation.txt out/lang/zh/UnitExplanation.js
	python makeName.py assets/lang/jp/UnitExplanation.txt out/lang/jp/UnitExplanation.js
	python makeStage.py
	mv stages.zip out/stages.zip

