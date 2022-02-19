# inputArr = ['IDN 1 n\n', 'OP_PRIDRUZI 1 =\n', 'BROJ 1 5\n', 'IDN 2 rez\n', 'OP_PRIDRUZI 2 =\n', 'BROJ 2 0\n',
#             'KR_ZA 3 za\n', 'IDN 3 i\n', 'KR_OD 3 od\n', 'IDN 3 n\n', 'KR_DO 3 do\n', 'IDN 3 n\n', 'OP_PLUS 3 +\n',
#             'BROJ 3 5\n', 'IDN 4 rez\n', 'OP_PRIDRUZI 4 =\n', 'IDN 4 rez\n', 'OP_MINUS 4 -\n', 'IDN 4 i\n',
#             'OP_PUTA 4 *\n', 'IDN 4 i\n', 'OP_PLUS 4 +\n', 'IDN 4 i\n', 'OP_DIJELI 4 /\n', 'BROJ 4 3\n', 'KR_AZ 5 az\n']
import sys

#inputArr = ['IDN 1 a\n', 'OP_PRIDRUZI 1 =\n', 'BROJ 1 1\n', 'OP_PUTA 1 *\n', 'BROJ 1 2\n']

inputArr =[]

stack = []
rowInput = ['<program>\n', '<lista_naredbi>\n', '<naredba>\n', '<naredba_pridruzivanja>\n', '<za_petlja>\n', '<E>\n',
            '<E_lista>\n', '<T>\n', '<T_lista>\n', '<P>\n', 'IDN\n', 'OP_PRIDRUZI\n', 'KR_OD\n', 'KR_DO\n', 'KR_AZ\n',
            'D_ZAGRADA\n', '#\n']
stack.append('#')
stack.append('<program>')

bindInputDict = {'IDN': 0, 'BROJ': 1, 'OP_PRIDRUZI': 2, 'OP_PLUS': 3, 'OP_MINUS': 4, 'OP_PUTA': 5, 'OP_DIJELI': 6,
                 'L_ZAGRADA': 7,
                 'D_ZAGRADA': 8, 'KR_ZA': 9, 'KR_OD': 10, 'KR_DO': 11, 'KR_AZ': 12, '!': 13}

i = 0
for line in sys.stdin:
    inputArr.insert(i, line)
    i = i + 1

ERR = False
stop = False
current = 0
shifted = False
skipDuplicate = False
spaces = 0
final = []


def replace(input, keepInput):
    popAndExtendStack(input)
    keep(keepInput)


def keep(keepInput):
    global current, isPulled

    if keepInput and isPulled == 1:  # zadrzi i izvuci
        final.append('$')
        isPulled = False

    elif not keepInput and isPulled == 1:  # pomakni i izvuci
        final.append(inputArr[current].strip())
        current += 1

    elif not keepInput:
        final.append(inputArr[current].strip())
        current += 1


def popAndExtendStack(input):
    global stack, skipDuplicate

    if not skipDuplicate:
        final.append(getStackTop())

    stack.pop()
    stack.extend(input)


def popAndExtendStackNoInput():
    global stack, isPulled, skipDuplicate

    if not skipDuplicate:
        final.append(getStackTop())

    stack.pop()
    isPulled = 1


def one():
    replace(['<lista_naredbi>'], True)


def two():
    replace(['<lista_naredbi>', '<naredba>'], True)


def three():
    popAndExtendStackNoInput()
    keep(True)


def fourteen():
    popAndExtendStackNoInput()
    keep(False)


def four():
    replace(['<naredba_pridruzivanja>'], True)


def five():
    replace(['<za_petlja>'], True)


def six():
    replace(['<E>', 'OP_PRIDRUZI'], False)


def seven():
    replace(['KR_AZ', '<lista_naredbi>', '<E>', 'KR_DO', '<E>', 'KR_OD', 'IDN'], False)


def eight():
    replace(['<E_lista>', '<T>'], True)


def nine():
    replace(['<E>'], False)


def ten():
    replace(['<T_lista>', '<P>'], True)


def eleven():
    replace(['<T>'], False)


def twelve():
    replace(['<P>'], False)


def thirteen():
    replace(['D_ZAGRADA', '<E>'], False)


def initDict():
    global bindInputDict
    bindInputDict.update(
        {'IDN': 0, 'BROJ': 1, 'OP_PRIDRUZI': 2, 'OP_PLUS': 3, 'OP_MINUS': 4, 'OP_PUTA': 5, 'OP_DIJELI': 6,
         'L_ZAGRADA': 7, 'D_ZAGRADA': 8, 'KR_ZA': 9, 'KR_OD': 10, 'KR_DO': 11, 'KR_AZ': 12, '!': 13})


def err():
    global ERR
    ERR = True
    showFinal()


def acc():
    showFinal()


def extractInput(inputArr):
    inputString = inputArr[current].strip()
    key = inputString.split(' ')  # IDN
    return key


def printSpaces():
    global spaces
    print(" " * spaces, end='')


def set(input, action):
    global stack
    if input == None:
        if (getStackTop() != "#"):
            final.append(getStackTop())
            final.append("$")
        stack.pop()
    else:
        columnRowDictTable[bindInputDict.get(input)][action]()


columnRowDictTable = [
    {
        rowInput[0].strip(): one,
        rowInput[1].strip(): two,
        rowInput[2].strip(): four,
        rowInput[3].strip(): six,
        rowInput[4].strip(): err,
        rowInput[5].strip(): eight,
        rowInput[6].strip(): three,
        rowInput[7].strip(): ten,
        rowInput[8].strip(): three,
        rowInput[9].strip(): fourteen,
        rowInput[10].strip(): fourteen,
        rowInput[11].strip(): err,
        rowInput[12].strip(): err,
        rowInput[13].strip(): err,
        rowInput[14].strip(): err,
        rowInput[15].strip(): err,
        rowInput[16].strip(): err
    },
    {  # BROJ
        rowInput[0].strip(): err,
        rowInput[1].strip(): err,
        rowInput[2].strip(): err,
        rowInput[3].strip(): err,
        rowInput[4].strip(): err,
        rowInput[5].strip(): eight,
        rowInput[6].strip(): err,
        rowInput[7].strip(): ten,
        rowInput[8].strip(): err,
        rowInput[9].strip(): fourteen,
        rowInput[10].strip(): err,
        rowInput[11].strip(): err,
        rowInput[12].strip(): err,
        rowInput[13].strip(): err,
        rowInput[14].strip(): err,
        rowInput[15].strip(): err,
        rowInput[16].strip(): err

    },
    {  # OP_PRIDRUZI 2
        rowInput[0].strip(): err,
        rowInput[1].strip(): err,
        rowInput[2].strip(): err,
        rowInput[3].strip(): err,
        rowInput[4].strip(): err,
        rowInput[5].strip(): err,
        rowInput[6].strip(): err,
        rowInput[7].strip(): err,
        rowInput[8].strip(): err,
        rowInput[9].strip(): err,
        rowInput[10].strip(): err,
        rowInput[11].strip(): fourteen,
        rowInput[12].strip(): err,
        rowInput[13].strip(): err,
        rowInput[14].strip(): err,
        rowInput[15].strip(): err,
        rowInput[16].strip(): err
    },
    {  # OP PLUS 3
        rowInput[0].strip(): err,
        rowInput[1].strip(): err,
        rowInput[2].strip(): err,
        rowInput[3].strip(): err,
        rowInput[4].strip(): err,
        rowInput[5].strip(): eight,
        rowInput[6].strip(): nine,
        rowInput[7].strip(): ten,
        rowInput[8].strip(): three,
        rowInput[9].strip(): twelve,
        rowInput[10].strip(): err,
        rowInput[11].strip(): err,
        rowInput[12].strip(): err,
        rowInput[13].strip(): err,
        rowInput[14].strip(): err,
        rowInput[15].strip(): err,
        rowInput[16].strip(): err
    },
    {  # OP_MINUS
        rowInput[0].strip(): err,
        rowInput[1].strip(): err,
        rowInput[2].strip(): err,
        rowInput[3].strip(): err,
        rowInput[4].strip(): err,
        rowInput[5].strip(): eight,
        rowInput[6].strip(): nine,
        rowInput[7].strip(): ten,
        rowInput[8].strip(): three,
        rowInput[9].strip(): twelve,
        rowInput[10].strip(): err,
        rowInput[11].strip(): err,
        rowInput[12].strip(): err,
        rowInput[13].strip(): err,
        rowInput[14].strip(): err,
        rowInput[15].strip(): err,
        rowInput[16].strip(): err
    },
    {  # OP_PUTA
        rowInput[0].strip(): err,
        rowInput[1].strip(): err,
        rowInput[2].strip(): err,
        rowInput[3].strip(): err,
        rowInput[4].strip(): err,
        rowInput[5].strip(): err,
        rowInput[6].strip(): err,
        rowInput[7].strip(): err,
        rowInput[8].strip(): eleven,
        rowInput[9].strip(): err,
        rowInput[10].strip(): err,
        rowInput[11].strip(): err,
        rowInput[12].strip(): err,
        rowInput[13].strip(): err,
        rowInput[14].strip(): err,
        rowInput[15].strip(): err,
        rowInput[16].strip(): err
    },
    {  # OP_DIJELI
        rowInput[0].strip(): err,
        rowInput[1].strip(): err,
        rowInput[2].strip(): err,
        rowInput[3].strip(): err,
        rowInput[4].strip(): err,
        rowInput[5].strip(): err,
        rowInput[6].strip(): err,
        rowInput[7].strip(): err,
        rowInput[8].strip(): eleven,
        rowInput[9].strip(): err,
        rowInput[10].strip(): err,
        rowInput[11].strip(): err,
        rowInput[12].strip(): err,
        rowInput[13].strip(): err,
        rowInput[14].strip(): err,
        rowInput[15].strip(): err,
        rowInput[16].strip(): err
    },
    {  # L_ZAGRADA
        rowInput[0].strip(): err,
        rowInput[1].strip(): err,
        rowInput[2].strip(): err,
        rowInput[3].strip(): err,
        rowInput[4].strip(): err,
        rowInput[5].strip(): eight,
        rowInput[6].strip(): err,
        rowInput[7].strip(): ten,
        rowInput[8].strip(): err,
        rowInput[9].strip(): thirteen,
        rowInput[10].strip(): err,
        rowInput[11].strip(): err,
        rowInput[12].strip(): err,
        rowInput[13].strip(): err,
        rowInput[14].strip(): err,
        rowInput[15].strip(): err,
        rowInput[16].strip(): err
    },
    {  # D_ZAGRADA
        rowInput[0].strip(): err,
        rowInput[1].strip(): err,
        rowInput[2].strip(): err,
        rowInput[3].strip(): err,
        rowInput[4].strip(): err,
        rowInput[5].strip(): err,
        rowInput[6].strip(): three,
        rowInput[7].strip(): err,
        rowInput[8].strip(): three,
        rowInput[9].strip(): err,
        rowInput[10].strip(): err,
        rowInput[11].strip(): err,
        rowInput[12].strip(): err,
        rowInput[13].strip(): err,
        rowInput[14].strip(): err,
        rowInput[15].strip(): fourteen,
        rowInput[16].strip(): err
    },
    {  # KR_ZA
        rowInput[0].strip(): one,
        rowInput[1].strip(): two,
        rowInput[2].strip(): five,
        rowInput[3].strip(): err,
        rowInput[4].strip(): seven,
        rowInput[5].strip(): err,
        rowInput[6].strip(): three,
        rowInput[7].strip(): err,
        rowInput[8].strip(): three,
        rowInput[9].strip(): err,
        rowInput[10].strip(): err,
        rowInput[11].strip(): err,
        rowInput[12].strip(): err,
        rowInput[13].strip(): err,
        rowInput[14].strip(): err,
        rowInput[15].strip(): err,
        rowInput[16].strip(): err
    },
    {  # KR_OD
        rowInput[0].strip(): err,
        rowInput[1].strip(): err,
        rowInput[2].strip(): err,
        rowInput[3].strip(): err,
        rowInput[4].strip(): err,
        rowInput[5].strip(): err,
        rowInput[6].strip(): err,
        rowInput[7].strip(): err,
        rowInput[8].strip(): err,
        rowInput[9].strip(): err,
        rowInput[10].strip(): err,
        rowInput[11].strip(): err,
        rowInput[12].strip(): fourteen,
        rowInput[13].strip(): err,
        rowInput[14].strip(): err,
        rowInput[15].strip(): err,
        rowInput[16].strip(): err
    },
    {  # KR_DO
        rowInput[0].strip(): err,
        rowInput[1].strip(): err,
        rowInput[2].strip(): err,
        rowInput[3].strip(): err,
        rowInput[4].strip(): err,
        rowInput[5].strip(): err,
        rowInput[6].strip(): three,
        rowInput[7].strip(): err,
        rowInput[8].strip(): three,
        rowInput[9].strip(): err,
        rowInput[10].strip(): err,
        rowInput[11].strip(): err,
        rowInput[12].strip(): err,
        rowInput[13].strip(): fourteen,
        rowInput[14].strip(): err,
        rowInput[15].strip(): err,
        rowInput[16].strip(): err
    },
    {  # KR_AZ
        rowInput[0].strip(): err,
        rowInput[1].strip(): three,
        rowInput[2].strip(): err,
        rowInput[3].strip(): err,
        rowInput[4].strip(): err,
        rowInput[5].strip(): err,
        rowInput[6].strip(): three,
        rowInput[7].strip(): err,
        rowInput[8].strip(): three,
        rowInput[9].strip(): err,
        rowInput[10].strip(): err,
        rowInput[11].strip(): err,
        rowInput[12].strip(): err,
        rowInput[13].strip(): err,
        rowInput[14].strip(): fourteen,
        rowInput[15].strip(): err,
        rowInput[16].strip(): err
    },
    {  # !
        rowInput[0].strip(): one,
        rowInput[1].strip(): three,
        rowInput[2].strip(): err,
        rowInput[3].strip(): err,
        rowInput[4].strip(): err,
        rowInput[5].strip(): err,
        rowInput[6].strip(): three,
        rowInput[7].strip(): err,
        rowInput[8].strip(): three,
        rowInput[9].strip(): err,
        rowInput[10].strip(): err,
        rowInput[11].strip(): err,
        rowInput[12].strip(): err,
        rowInput[13].strip(): err,
        rowInput[14].strip(): err,
        rowInput[15].strip(): err,
        rowInput[16].strip(): acc
    }

]


def getStackTop():
    global stack
    topOfStack = stack[len(stack) - 1]  # <program>
    return topOfStack


def setPulledandDuplicateBools():
    global isPulled, skipDuplicate
    isPulled = -1
    skipDuplicate = False


def checkInputLength():
    global current, inputArr
    if current != len(inputArr):
        return True
    return False


def stackHasOneEl():
    global stack
    if len(stack) > 0:
        return True
    return False


def showFinal():
    global final, shortInput, ERR, stop
    if ERR and shortInput == "!":
        print("err kraj")
        exit()
    elif ERR:
        print("err " + inputArr[current].strip())
        exit()
    stop = True


while checkInputLength() or stackHasOneEl():
    if stop:
        break
    setPulledandDuplicateBools()
    shortInput = '!'
    topOfStack = getStackTop()

    if checkInputLength():
        inputKey = extractInput(inputArr)
        shortInput = inputKey[0]

        if shortInput == topOfStack:
            skipDuplicate = True

    set(shortInput, topOfStack)

dictPrint = {'<program>': [['<lista_naredbi>']],
             '<lista_naredbi>': [['<naredba>', '<lista_naredbi>'], ['$']],
             '<naredba>': [['<naredba_pridruzivanja>'], ['<za_petlja>']],
             '<naredba_pridruzivanja>': [['IDN', 'OP_PRIDRUZI', '<E>']],
             '<za_petlja>': [['KR_ZA', 'IDN', 'KR_OD', '<E>', 'KR_DO', '<E>', '<lista_naredbi>', 'KR_AZ']],
             '<E>': [['<T>', '<E_lista>']],
             '<E_lista>': [['OP_PLUS', '<E>'], ['OP_MINUS', '<E>'], ['$']],
             '<T>': [['<P>', '<T_lista>']],
             '<T_lista>': [['OP_PUTA', '<T>'], ['OP_DIJELI', '<T>'], ['$']],
             '<P>': [['OP_PLUS', '<P>'], ['OP_MINUS', '<P>'], ['L_ZAGRADA', '<E>', 'D_ZAGRADA'], ['IDN'], ['BROJ']]
             }

index = 0


def findKey(key):
    if key in dictPrint:
        t = dictPrint.get(key)
        return t
    return None


def rek(pov):
    global index
    for ii in range(pov):
        print(' ', end='')
    print(final[index])

    if findKey(final[index]):
        for j in range(len(dictPrint[final[index]])):
            if dictPrint[final[index]][j][0] == final[index + 1].split(' ')[0]:
                break
            j += 1
        for ii in range(len(dictPrint[final[index]][j])):
            index += 1
            rek(pov + 1)


rek(0)
