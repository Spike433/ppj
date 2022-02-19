rowInput = ['<program>\n', '<lista_naredbi>\n', '<naredba>\n', '<naredba_pridruzivanja>\n', '<za_petlja>\n', '<E>\n',
         '<E_lista>\n', '<T>\n', '<T_lista>\n', '<P>\n', 'IDN\n', 'OP_PRIDRUZI\n', 'KR_OD\n', 'KR_DO\n', 'KR_AZ\n',
         'D_ZAGRADA\n', '#\n']

inputArr = []

stack = []
stack.append('#')
stack.append('<program>')
ERR = False

bindInputDict = {}
bindInputDict.update(
    {'IDN': 0, 'BROJ': 1, 'OP_PRIDRUZI': 2, 'OP_PLUS': 3, 'OP_MINUS': 4, 'OP_PUTA': 5, 'OP_DIJELI': 6, 'L_ZAGRADA': 7,
     'D_ZAGRADA': 8, 'KR_ZA': 9, 'KR_OD': 10, 'KR_DO': 11, 'KR_AZ': 12, '!': 13})


def replace(input, keep):
    global stack
    stack.pop()
    stack.extend(input)
    # Todo implement keep


def one():
    replace(['<lista_naredbi>'], True)


def two():
    replace(['<lista_naredbi>', '<naredba>'], True)


def three():
    global stack
    stack.pop()
    # todo keep=true


def fourteen():
    global stack
    stack.pop()
    # todo keep=false --> shift input


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


def err():
    global ERR
    ERR = True


def acc():
    global ERR
    ERR = False
    # Todo avoid this


lista = [
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

print(stack)
lista[9]['<za_petlja>']()
print(stack)

# usage lista[pickRowInputInt][findInColumnAction]() --> lista[0]['<program>']()
