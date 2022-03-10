# map (final) constanant+tone to tone+constanan
mapConstTone2ToneConst = {
    "n1": "1n",
    "n2": "2n",
    "n3": "3n",
    "n4": "4n",
    "ng1": "1ng",
    "ng2": "2ng",
    "ng3": "3ng",
    "ng4": "4ng",
    "r1": "1r",
    "r2": "2r",
    "r3": "3r",
    "r4": "4r",
}

# map vowel+vowel+tone to vowel+tone+vowel
mapVowelVowelTone2VowelToneVowel = {
    "ai1": "a1i",
    "ai2": "a2i",
    "ai3": "a3i",
    "ai4": "a4i",
    "ao1": "a1o",
    "ao2": "a2o",
    "ao3": "a3o",
    "ao4": "a4o",
    "ei1": "e1i",
    "ei2": "e2i",
    "ei3": "e3i",
    "ei4": "e4i",
    "ou1": "o1u",
    "ou2": "o2u",
    "ou3": "o3u",
    "ou4": "o4u",
}

# map vowel-number combination to unicode
mapVowelTone2Unicode = {
    "a1": "ā",
    "a2": "á",
    "a3": "ǎ",
    "a4": "à",
    "e1": "ē",
    "e2": "é",
    "e3": "ě",
    "e4": "è",
    "i1": "ī",
    "i2": "í",
    "i3": "ǐ",
    "i4": "ì",
    "o1": "ō",
    "o2": "ó",
    "o3": "ǒ",
    "o4": "ò",
    "u1": "ū",
    "u2": "ú",
    "u3": "ǔ",
    "u4": "ù",
    "v1": "ǖ",
    "v2": "ǘ",
    "v3": "ǚ",
    "v4": "ǜ",
}


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
