def mapping(location):
    title = ''
    address =' '
    latitude = ''
    longitude = ''
    flag = True # 此地點是否存在

    if location == '研發大樓':
        latitude=24.795331
        longitude=120.997054

    elif location == '創新育成中心':
        latitude=24.795236
        longitude=120.996590
    
    elif location in ['工程一館','工一']:
        latitude=24.795094
        longitude=120.996176
    
    elif location == '科儀中心':
        latitude=24.794479
        longitude=120.996259
    
    elif location == '化學館':
        latitude=24.796424
        longitude=120.995975

    elif location == '動機化學實驗室':
        latitude=24.796772
        longitude=120.995355

    elif location == '化工館':
        latitude=24.796396
        longitude=120.995007

    elif location in ['學習資源中心','旺宏館','行政中心','國際會議廳','藝術創新中心','亞洲政策中心','斯麥爾咖啡','圖書館','採編組','資訊系統組','典閱組','服務與創新組','綜合館務組','特藏組','秘書處']:
        latitude=24.795523
        longitude=120.994670
    
    elif location in ['教育館','師資培育中心','通識教育中心','共同教育委員會','華德福教育中心']:
        latitude=24.795727
        longitude=120.993952

    elif location in ['第一綜合大樓','綜一','行政大樓','綜合學務組','學務處','總務處','全球事務處','招生組','註冊組','人事室','主計室','研究發展處' ,'校園規劃組','綜合企劃組','計畫管理組','事務組','保管組','採購組','文書組','出納組','營繕組','教務處']:
        latitude=24.794765
        longitude=120.994444

    elif location in ['第二綜合大樓','綜二','藝術中心','計算機與通訊中心','會議廳','校務資訊組','網路系統組','學習科技組']:
        latitude=24.794308
        longitude=120.993361
    
    elif location in ['第三綜合大樓','綜三']:
        latitude=24.794931
        longitude=120.993404
        
    elif location in ['工程三館','工三']:
        latitude=24.796418
        longitude=120.992671
    
    elif location == '材料科技館':
        latitude=24.796545
        longitude=120.991807

    elif location == '材料實驗館':
        latitude=24.796556
        longitude=120.990883

    elif location == '合金實驗館':
        title='合金實驗館'
        address='合金實驗館'
        latitude=24.796685
        longitude=120.990180

    elif location == '台達館':
        latitude=24.795998
        longitude=120.992134
    
    elif location in ['資訊電機館','資電館','數學圖書館']:
        latitude=24.794943
        longitude=120.992145
    
    elif location in ['物理館','物理圖書分館']:
        latitude=24.794183
        longitude=120.992370
    
    elif location == '工科館':
        latitude=24.790958
        longitude=120.990893

    elif location in ['綠色低碳能源教學研究大樓','李存敏館','綠能大樓','綠能館']:
        latitude=24.790746
        longitude=120.991351

    elif location == '原子爐':
        latitude=24.789893
        longitude=120.992099
    
    elif location == '同位素館':
        latitude=24.789240
        longitude=120.992317
    
    elif location == '加速器館':
        latitude=24.788835
        longitude=120.992271

    elif location == '高能光電實驗室':
        latitude=24.788704
        longitude=120.991853
    
    elif location == '生物科技館':
        latitude=24.789701
        longitude=120.991151
    
    elif location == '生醫工程與環境科學館':
        latitude=24.789202
        longitude=120.991274
    
    elif location == '生命科學一館':
        latitude=24.789779
        longitude=120.990391

    elif location == '生命科學二館':
        latitude=24.789285
        longitude=120.989778
    
    elif location in ['人文社會學館','人文社會學院','人社院']:
        latitude=24.790031
        longitude=120.989070
    
    elif location in ['台積館','科技管理學院']:
        latitude=24.786815
        longitude=120.988265
    
    elif location in ['創新育成大樓','國際產學營運總中心','行政組','產學企劃組','智財技轉組','技轉中心']:
        latitude=24.786239
        longitude=120.988760

    elif location == '清華實驗室':
        latitude=24.785724
        longitude=120.989839
    
    elif location == '醫輔大樓':
        latitude=24.796307
        longitude=120.994396
    
    elif location == '郵局':
        latitude=24.795638
        longitude=120.997007

    elif location == '清華大草坪':
        latitude=24.795375
        longitude=120.995573
    
    elif location in ['清華名人堂','名人堂']:
        latitude=24.793923
        longitude=120.993054
    
    elif location == '水漾餐廳':
        latitude=24.794095
        longitude=120.993356
    
    elif location == '大禮堂':
        latitude=24.793379
        longitude=120.993839
    
    elif location == '社團辦公室':
        latitude=24.793023
        longitude=120.994142
    
    elif location in ['水木生活中心','學生住宿組','生活輔道組']:
        latitude=24.792239
        longitude=120.994365
    
    elif location == '水木餐廳':
        latitude=24.792271
        longitude=120.994345
    
    elif location == '水木書苑':
        latitude=24.792364
        longitude=120.994656
    
    elif location == '風雲樓':
        latitude=24.792066
        longitude=120.994743
    
    elif location in ['小吃部','麥當勞','統一超商','711']:
        latitude=24.793194
        longitude=120.993083
    
    elif location == '室內網球場':
        latitude=24.796371
        longitude=120.990364
    
    elif location == '游泳池':
        latitude=24.794929
        longitude=120.991487
    
    elif location in ['舊體育館','桌球館']:
        latitude=24.794267
        longitude=120.991565
    
    elif location in ['體育館','體育室']:
        latitude=24.793562
        longitude=120.991667
    
    elif location in ['蒙民偉樓','學生活動中心','課外活動組']:
        latitude=24.793656
        longitude=120.992071
    
    elif location == '駐警隊':
        latitude=24.791579
        longitude=120.991832
    
    elif location == '土地公廟':
        latitude=24.787417
        longitude=120.990924
    
    elif location == '校友體育館':
        latitude=24.795336
        longitude=120.989802
    
    elif location == '自強樓':
        latitude=24.796958
        longitude=120.991888
    
    elif location == '西院宿舍':
        latitude=24.797500
        longitude=120.991722
    
    elif location == '莊敬樓':
        latitude=24.797304
        longitude=120.990759
    
    elif location == '第二招待所':
        latitude=24.797080
        longitude=120.991218
    
    elif location == '教職員單身宿舍':
        latitude=24.797905
        longitude=120.991342
    
    elif location == '清華會館':
        latitude=24.797998
        longitude=120.991082
    
    elif location == '東院宿舍':
        latitude=24.794698
        longitude=120.997451
    
    elif location == '學人宿舍':
        latitude=24.790161
        longitude=120.998310
    
    elif location == '碩齋':
        latitude=24.791243
        longitude=120.996792
    
    elif location == '信齋':
        latitude=24.790876
        longitude=120.995779

    elif location == '禮齋':
        latitude=24.791056
        longitude=120.995406
    
    elif location == '仁齋':
        latitude=24.791448
        longitude=120.995755
    
    elif location == '實齋':
        latitude=24.791477
        longitude=120.995173
    
    elif location == '實齋交誼廳':
        latitude=24.791592
        longitude=120.994768
    
    elif location == '華齋':
        latitude=24.791721
        longitude=120.994135
    
    elif location == '誠齋':
        latitude=24.791355
        longitude=120.994012
    
    elif location == '義齋':
        latitude=24.790982
        longitude=120.993993
    
    elif location == '鴻齋':
        latitude=24.790487
        longitude=120.993819
    
    elif location == '學齋':
        latitude=24.789987
        longitude=120.993089
    
    elif location == '明齋':
        latitude=24.792692
        longitude=120.993147
    
    elif location == '平齋':
        latitude=24.792534
        longitude=120.993260
    
    elif location == '善齋':
        latitude=24.792069
        longitude=120.993504
    
    elif location == '新齋':
        latitude=24.791757
        longitude=120.992784
    
    elif location == '清齋':
        latitude=24.790951
        longitude=120.993441
    
    elif location == '雅齋':
        latitude=24.792790
        longitude=120.991919
    
    elif location == '靜齋':
        latitude=24.792518
        longitude=120.991340
    
    elif location == '慧齋':
        latitude=24.792136
        longitude=120.991276
    
    elif location == '文齋':
        latitude=24.792007
        longitude=120.990847
    
    elif location == '女宿':
        latitude=24.792479
        longitude=120.991892
    
    elif location in ['立體機車停車場','機車塔']:
        latitude=24.797310
        longitude=120.995583
    
    elif location == '北校區實驗室廢水處理廠':
        latitude=24.796810
        longitude=120.992503
    
    elif location == '電工房':
        latitude=24.792843
        longitude=120.992679
    
    elif location == '機車塔':
        latitude=24.797339
        longitude=120.995588
    
    elif location == '清交小徑':
        latitude=24.790607
        longitude=120.995653
    
    elif location == '大禮堂':
        latitude=24.793466
        longitude=120.993770
    
    elif location == '室外排球場':
        latitude=24.793916
        longitude=120.990957
    
    elif location in ['田徑場','操場']:
        latitude=24.794126
        longitude=120.990020
    
    elif location == '游泳池':
        latitude=24.794963
        longitude=120.991483
    
    elif location == '棒球場':
        latitude=24.796049
        longitude=120.990807
    
    elif location == '網球場':
        latitude=24.796370
        longitude=120.989863
    
    elif location in ['醫輔中心','衛生保健組','諮詢諮詢中心']:
        latitude=24.796370
        longitude=120.994380
    
    elif location in ['診所','清華大學附設診所','附設診所']:
        latitude=24.795730
        longitude=120.996922
    
    elif location == '奕園停車場':
        latitude=24.788315
        longitude=120.991918
    
    elif location == '奕園':
        latitude=24.787872
        longitude=120.990715
    
    elif location == '梅園':
        latitude=24.792371
        longitude=120.990010

    elif location == '合勤演藝中心':
        latitude=24.794669
        longitude=120.994415
    
    elif location == '成功湖':
        latitude=24.793493
        longitude=120.995342
    
    elif location == '大草皮':
        latitude=24.795433
        longitude=120.995564
    
    elif location in ['北校門口','北校門']:
        latitude=24.796607
        longitude=120.997033
    
    elif location in ['南校門口','南校門']:
        latitude=24.786080
        longitude=120.988363
    
    elif location == '蝴蝶園':
        latitude=24.790629
        longitude=120.988586
    
    elif location in ['全家','全家便利商店']:
        latitude=24.792249
        longitude=120.994236
    
    elif location == '荷塘':
        latitude=24.790613
        longitude=120.992277
    
    elif location == '客運站':
        latitude=24.795669
        longitude=120.998127
    
    elif location in ['火車站','新竹火車站']:
        latitude=24.801602
        longitude=120.971597
    
    elif location in ['醫院','馬偕醫院']:
        latitude=24.800374
        longitude=120.990775
    
    #===========================南大校區===============================

    elif location in ['計通中心','推廣教育大樓']:
        latitude=24.792841
        longitude=120.966480
    
    elif location == '校使館':
        latitude=24.793892
        longitude=120.965863
    
    elif location in ['圖書館南大分館','南大圖書館']:
        latitude=24.794182
        longitude=120.965478
    
    elif location in ['教學大樓','通識中心','教與學中心']:
        latitude=24.793782
        longitude=120.965108
    
    elif location in ['綜合教育大樓','資源教室']: #行政大樓
        latitude=24.793784
        longitude=120.965097
    
    elif location == '迎曦軒':
        latitude=24.793874
        longitude=120.964091
    
    elif location == '崇善樓':
        latitude=24.793699
        longitude=120.963933
    
    elif location == '鳴鳳樓':
        latitude=24.793463
        longitude=120.963753
    
    elif location in ['諮商中心','原資中心','衛保組','學務處聯合辦公室']:
        latitude=24.793463
        longitude=120.963753
    
    elif location == '綜合體育館':
        latitude=24.792898
        longitude=120.963626
    
    elif location == '體育健康教學大樓':
        latitude=24.792952
        longitude=120.963163

    elif location == '學生第二活動中心':
        latitude=24.792587
        longitude=120.963238

    elif location == '樹德樓':
        latitude=24.792356
        longitude=120.963391
    
    elif location == '掬月齋':
        latitude=24.792125
        longitude=120.963447
    
    elif location == '音樂二館':
        latitude=24.792349
        longitude=120.964208
    
    elif location == '運動場':
        latitude=24.792690
        longitude=120.965246
    
    elif location in ['南大校區正門','南大校門','南大正門','南大校門口']:
        latitude=24.792349
        longitude=120.964208
    
    else:
        flag = False


    # return map information 
    mapInfo = {
        'isExist': flag,
        'info': {
            'title': location,
            'address': location,
            'latitude': latitude,
            'longitude': longitude
        },
        'errMsg': None
    }

    if not flag:
        mapInfo['errMsg'] = '汪汪，我聽不懂還在學習中。你可以到「選單」→「神奇海螺」→「問題反饋」教我。如果還想再問我問題可以回到「選單」再問一次喔！'

    return mapInfo
