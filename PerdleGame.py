from utils.pinyin_to_list import convert_pinyin_to_list
from utils.diff_char import num_diff_char


chengyu_path = open("chengyu_introText.csv", "r", encoding="utf-8")
chengyu_set = chengyu_path.read().split("\n")
chengyu_dict = []
for idx in range(len(chengyu_set) // 2):
    chengyu = chengyu_set[idx * 2]
    duyin = chengyu_set[idx * 2 + 1]
    duyin = convert_pinyin_to_list(duyin)
    for d in duyin:
        d.append(len(d[0]))
    duyin.append(chengyu)
    chengyu_dict.append(duyin)


word = [-1, -1, -1, -1]
correct_pos = [[[]], [[]], [[]], [[]]]
wrong_pos = [
    [[]],
    [[]],
    [[]],
    [[]],
]
poss_char = []


word = [-1, -1, -1, -1]
correct_pos = [[[]], [[]], [[]], [[]]]
wrong_pos = [
    [[]],
    [[]],
    [[]],
    [[]],
]
poss_char = []


possible_result = {}
for c in chengyu_dict:
    is_match = True
    cur_chengyu = c[4]
    for i in range(len(word)):
        if word[i] != -1 and c[i][2] != word[i]:
            is_match = False

    for i in range(len(correct_pos)):
        for j in range(len(correct_pos[i])):
            if (
                correct_pos[i][j]
                and correct_pos[i][j][1] < c[i][2]
                and correct_pos[i][j][0] != c[i][0][correct_pos[i][j][1]]
            ):
                is_match = False

    for i in range(len(wrong_pos)):
        for j in range(len(wrong_pos[i])):
            if (
                wrong_pos[i][j]
                and wrong_pos[i][j][1] < c[i][2]
                and wrong_pos[i][j][0] == c[i][0][wrong_pos[i][j][1]]
            ):
                is_match = False

    is_poss = True
    for i in poss_char:
        temp = False
        for j in range(4):
            if i in c[j][0]:
                temp = True
        is_poss &= temp
    is_match &= is_poss

    if is_match:
        num_of_char = num_diff_char(c)
        if num_of_char not in possible_result.keys():
            possible_result[num_of_char] = []
        possible_result[num_of_char].append(cur_chengyu)


for i in sorted(possible_result.keys()):
    print(i, possible_result[i])
