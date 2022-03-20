def num_diff_char(chengyu):
    appear_char = []
    for i in range(4):
        for j in chengyu[i][0]:
            if j not in appear_char:
                appear_char.append(j)
    return len(appear_char)


def num_diff_char2(chengyu):
    appear_con = []
    appear_vo = []
    for i in range(4):
        if chengyu[i][0] not in appear_con:
            appear_con.append(chengyu[i][0])
        if chengyu[i][1] not in appear_vo:
            appear_vo.append(chengyu[i][1])
    return len(appear_con) + len(appear_vo)
