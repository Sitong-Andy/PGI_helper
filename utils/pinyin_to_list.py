from utils.dict import (
    mapConstTone2ToneConst,
    mapVowelVowelTone2VowelToneVowel,
    mapVowelTone2Unicode,
)


def ConvertToneNumbersPinyin(lineIn):
    assert type(lineIn) is str
    lineOut = lineIn

    for x, y in mapVowelTone2Unicode.items():
        lineOut = lineOut.replace(y, x).replace(y.upper(), x.upper())

    for x, y in mapVowelVowelTone2VowelToneVowel.items():
        lineOut = lineOut.replace(y, x).replace(y.upper(), x.upper())

    for x, y in mapConstTone2ToneConst.items():
        lineOut = lineOut.replace(y, x).replace(y.upper(), x.upper())

    return lineOut.replace("Ü", "V").replace("ü", "v")


def convert_pinyin_to_list(pinyin):
    lineOut = ConvertToneNumbersPinyin(pinyin)
    result = []
    temp = []
    pinyin_list = lineOut.split(" ")
    for i in pinyin_list:
        num = 0
        for j in i:
            if j.isdigit():
                num = int(j)
            elif j.isalpha():
                temp.append(j)
        result.append([temp, num])
        temp = []
    return result


# Test
# print(convert_pinyin_to_list("ēn bù fàng zhai"))
