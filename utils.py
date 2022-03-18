def num_diff_char(chengyu):
    appear_char = []
    for i in range(4):
        for j in chengyu[i][0]:
            if j not in appear_char:
                appear_char.append(j)
    return len(appear_char)
