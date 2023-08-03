def load_gacha(): #todo: eventGacha
    gacha = []
    cats = [i for i in range(718)]
    for eachGachaType in ['R', 'E', 'N']:
        gachaContent = open(f"GatyaDataSet{eachGachaType}1.csv")

        for index_, line in enumerate(gachaContent):
            unitInLine_list = []
            line = filter(len, line.split('//')[0].replace('\n', '').replace('\t', '').replace(' ', '').split(','))
            for unitEach in line:
                try:
                    unitEach = int(unitEach)
                except ValueError:
                    continue
                if unitEach in [-1, "-1"]: continue
                unitInLine_list.append(str(cats[unitEach]))

            unitInLine = ', '.join(unitInLine_list)
            gachaType_tl = eachGachaType.translate({ord("R"): "稀有", ord('E'): "活動", ord('N'): "普通"})

            if eachGachaType == "R": imagefile = f'Image/gatya_bnr{index_}.png'
            elif eachGachaType == "E": imagefile = f'Image/gatya_e_bnr{index_}.png'
            elif eachGachaType == "N": imagefile = "無"

            gacha.append((index_, gachaType_tl, unitInLine, imagefile))

    return gacha

print(load_gacha())