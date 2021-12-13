import copy

BUS_LOC = ["北校門口", "綜二館", "楓林小徑", "奕園停車場", "南門停車場", "人社院", "台積館"]

BUS_SCHED_DICT = {
    "green_climb": ["北校門口", "綜二館", "楓林小徑", "奕園停車場", "南門停車場", "台積館"],
    "red_climb": ["北校門口", "綜二館", "楓林小徑", "人社院", "台積館"],
    "green_descend": ["台積館", "人社院", "楓林小徑", "綜二館", "北校門口"],
    "red_descend": ["台積館", "南門停車場", "奕園停車場", "楓林小徑", "綜二館", "北校門口"]
}

BUS_LOC_MAP_EN = {
    "north_main_gate": "北校門口",
    "general_building": "綜二館",
    "maple_path": "楓林小徑",
    "yi_pavilion_parking_lot": "奕園停車場",
    "south_gate_parking_lot": "南門停車場",
    "college_of_human_building": "人社院",
    "tsmc_building": "台積館"
}

BUS_LOC_MAP_CH = {
    "北校門口": "north_main_gate",
    "綜二館": "general_building",
    "楓林小徑": "maple_path",
    "奕園停車場": "yi_pavilion_parking_lot",
    "南門停車場": "south_gate_parking_lot",
    "人社院": "college_of_human_building",
    "台積館": "tsmc_building"
}

def hasBusLoc(loc):
    if loc in BUS_LOC:
        return True
    else:
        return False

# 取得geton地點後，回覆可能的下車地點
def geton_map_getoff(geton_loc):
    temp = copy.deepcopy(BUS_LOC)
    temp.remove(BUS_LOC_MAP_EN[geton_loc])
    return temp

# 檢查是 上山或下山 & 綠線或紅線
def check_direction_and_line(geton, getoff):
    # 取得方向合理(getoff在geton後面) 的key
    proper_route_key = []
    for k in BUS_SCHED_DICT.keys():
        route = BUS_SCHED_DICT[k]

        geton_flag = False
        getoff_flag = False
        for r in route:
            if geton == r:
                geton_flag = True
            if geton_flag==True and getoff==r:
                getoff_flag = True
        
        if geton_flag==True and getoff_flag==True:
            proper_route_key.append(k)

    
    # 整理方向 及 line
    direction = ''
    line = []
    for k in proper_route_key:
        k_list = k.split('_')
        l = k_list[0] # line
        d = k_list[1] # direction

        line.append(l)
        direction = d

    return direction, line