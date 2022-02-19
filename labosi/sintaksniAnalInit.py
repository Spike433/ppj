input=['IDN\n', 'BROJ\n', 'OP_PRIDRUZI\n', 'OP_PLUS','OP_MINUS\n', 'OP_PUTA\n', 'OP_DIJELI\n', 'L_ZAGRADA\n', 'D_ZAGRADA\n', 'KR_ZA\n', 'KR_OD\n', 'KR_DO\n', 'KR_AZ\n', '!\n']

print(input[0].strip())

bindInputDict={}

i=0
for word in input:
    bindInputDict.update({word.strip():i})
    i=i+1
print(bindInputDict)

dict2={'IDN': 0, 'BROJ': 1, 'OP_PRIDRUZI': 2, 'OP_PLUS': 3, 'OP_MINUS': 4, 'OP_PUTA': 5, 'OP_DIJELI': 6, 'L_ZAGRADA': 7, 'D_ZAGRADA': 8, 'KR_ZA': 9, 'KR_OD': 10, 'KR_DO': 11, 'KR_AZ': 12, '!': 13}

print(dict2)