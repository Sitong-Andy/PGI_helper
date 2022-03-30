from utils.pinyin_to_list import ConvertToneNumbersPinyin
from utils.dict import consontant_dict, vowel_dict


def get_consontant(pinyin):
    for i in consontant_dict:
        if pinyin.startswith(i):
            return i
    return ""


def get_vowel(pinyin):
    consontant = get_consontant(pinyin)
    vowel = pinyin[len(consontant) :]
    if vowel not in vowel_dict:
        return ""
    return vowel


def convert_vowel_consonant_to_list(pinyin):
    result = []
    lineOut = ConvertToneNumbersPinyin(pinyin)
    pinyin_list = lineOut.split(" ")
    for i in pinyin_list:
        num = 0
        py = ""
        for j in i:
            if j.isdigit():
                num = int(j)
            elif j.isalpha():
                py += j
        con = get_consontant(py)
        vo = get_vowel(py)
        result.append([con, vo, num])
    return result


# Test
# print(convert_vowel_consonant_to_list("zhàng lǚ xiāng cóng"))
