from utils.vowel_consonant_to_list import convert_vowel_consonant_to_list
from utils.diff_char import num_diff_char2

chengyu_path = open("chengyu_introText.csv", "r", encoding="utf-8")
chengyu_set = chengyu_path.read().split("\n")
chengyu_dict = []
for idx in range(len(chengyu_set) // 2):
    temp = []
    chengyu = chengyu_set[idx * 2]
    duyin = chengyu_set[idx * 2 + 1]
    convert_cv = convert_vowel_consonant_to_list(duyin)
    convert_cv.append(chengyu)
    chengyu_dict.append(convert_cv)


tone = [-1, -1, -1, -1]
correct_con = ["", "", "", ""]
correct_vo = ["", "", "", ""]
con_not_in_word = []
vo_not_in_word = []
poss_con_in_word = []
poss_vo_in_word = []


tone = [-1, -1, -1, -1]
correct_con = ["", "", "", ""]
correct_vo = ["", "", "", ""]
con_not_in_word = []
vo_not_in_word = []
poss_con_in_word = []
poss_vo_in_word = []


possible_result = {}
for c in chengyu_dict:
    is_match = True
    cur_chengyu = c[4]
    for i in range(len(tone)):
        if tone[i] != -1 and c[i][2] != tone[i]:
            is_match = False

    for i in range(len(correct_con)):
        if correct_con[i] and correct_con[i] != c[i][0]:
            is_match = False

    for i in range(len(correct_vo)):
        if correct_vo[i] and correct_vo[i] != c[i][1]:
            is_match = False

    for i in con_not_in_word:
        for j in range(4):
            if i == c[j][0]:
                is_match = False

    for i in vo_not_in_word:
        for j in range(4):
            if i == c[j][1]:
                is_match = False

    poss_in_word = True
    for i in poss_con_in_word:
        temp = False
        for j in range(4):
            if i == c[j][0]:
                temp |= True
        poss_in_word &= temp

    for i in poss_vo_in_word:
        temp = False
        for j in range(4):
            if i == c[j][1]:
                temp |= True
        poss_in_word &= temp
    if not poss_in_word:
        is_match = False

    if is_match:
        num_of_char = num_diff_char2(c)
        if num_of_char not in possible_result.keys():
            possible_result[num_of_char] = []
        possible_result[num_of_char].append(cur_chengyu)


for i in sorted(possible_result.keys()):
    print(i, possible_result[i])
