final = ['<program>', '<lista_naredbi>', '<naredba>', '<naredba_pridruzivanja>', 'IDN 1 a', 'OP_PRIDRUZI 1 =', '<E>',
         '<T>', '<P>', 'BROJ 1 1', '<T_lista>', 'OP_PUTA 1 *', '<T>', '<P>', 'BROJ 1 2', '<T_lista>', '$', '<E_lista>',
         '$', '<lista_naredbi>', '$']

#final = ['<program>', '<lista_naredbi>', '<naredba>', '<naredba_pridruzivanja>', 'IDN 1 a', 'OP_PRIDRUZI 1 =', '<E>', '<T>', '<P>', 'BROJ 1 0', '<T_lista>', '$', '<E_lista>', '$', '<lista_naredbi>', '$']

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
    for i in range(pov):
        print(' ', end='')
    print(final[index])

    if findKey(final[index]):
        for j in range(len(dictPrint[final[index]])):
            if dictPrint[final[index]][j][0] == final[index + 1].split(' ')[0]:
                break
            j += 1
        for i in range(len(dictPrint[final[index]][j])):
            index += 1
            rek(pov + 1)


rek(0)