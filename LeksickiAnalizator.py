import sys

def printRightSide(rightSide, currLine):
    splitBySpace = rightSide.split(' ')

    if rightSide.strip() == "do":
        print('KR_DO ' + str(currLine) + ' ' + rightSide.strip())
        return

    elif rightSide.strip() == "od":
        print('KR_OD ' + str(currLine) + ' ' + rightSide.strip())
        return

    for word in splitBySpace:
        variable = 'IDN '+currLine+' '
        number='BROJ '+ currLine+ ' '
        isVariable = False
        isNumber = False
        firstLetter = True
        word = word.strip()

        for char in word:
            if word.__contains__('//'):
                return
            if char == '(':
                if isVariable:
                    isVariable = False
                    firstLetter = True
                    print(variable)
                    variable = 'IDN ' + currLine + ' '
                elif isNumber:
                    isNumber = False
                    firstLetter = True
                    print(number)
                    number='BROJ '+ currLine+ ' '

                print('L_ZAGRADA '+currLine+' (')
            elif char == ')':
                if isVariable:
                    isVariable=False
                    firstLetter = True
                    print(variable)
                    variable = 'IDN ' + currLine + ' '
                elif isNumber:
                    isNumber = False
                    print(number)
                    number='BROJ '+ currLine+ ' '

                print('D_ZAGRADA ' + currLine + ' )')
            elif char == '+':
                if isVariable:
                    isVariable=False
                    firstLetter = True
                    print(variable)
                    variable = 'IDN ' + currLine + ' '
                elif isNumber:
                    isNumber = False
                    print(number)
                    number='BROJ '+ currLine+ ' '

                print('OP_PLUS '+currLine+' +')
            elif char == '-':
                if isVariable:
                    isVariable=False
                    firstLetter = True
                    print(variable)
                    variable = 'IDN ' + currLine + ' '
                elif isNumber:
                    isNumber = False
                    print(number)
                    number='BROJ '+ currLine+ ' '

                print('OP_MINUS '+currLine+' -')
            elif char == '/':
                if isVariable:
                    isVariable=False
                    firstLetter = True
                    print(variable)
                    variable = 'IDN ' + currLine + ' '
                elif isNumber:
                    isNumber = False
                    print(number)
                    number='BROJ '+ currLine+ ' '
                print('OP_DIJELI '+currLine+' /')
            elif char == '*':
                if isVariable:
                    isVariable=False
                    firstLetter = True
                    print(variable)
                    variable = 'IDN ' + currLine + ' '
                elif isNumber:
                    isNumber = False
                    print(number)
                    number='BROJ '+ currLine+ ' '
                print('OP_PUTA '+currLine+' *')
            else:
                if char.isalpha() and firstLetter:
                    isVariable = True
                    variable += char
                    firstLetter = True

                    if isNumber:  # additional check if 5xys encounters
                        print(number)
                        isNumber = False

                elif (char.isalpha() or char.isdigit() ) and isVariable:
                    variable += char
                else:
                    number+=char
                    isNumber = True
        if isVariable:
            print(variable)
        elif isNumber:
            print(number)


arr = []

i=0
for line in sys.stdin:
    arr.insert(i, line)
    i = i+1

#arr = [ 'do = od\n', 'od = 3+zaz\n']

currentLine = 0

for string in arr:

    string = string.strip()
    currentLine = currentLine+1

    if string.__contains__('//') and string.index('//')==0:
        continue

    if string.__contains__('='):
        identifikAndConst = string.split('=')
        if identifikAndConst[0].strip() !='':
            leftSide = identifikAndConst[0].strip()

            if leftSide == "do":
                print('KR_DO ' + str(currentLine) + ' ' + identifikAndConst[0].strip())
            elif leftSide == "od":
                print('KR_OD ' + str(currentLine) + ' ' + identifikAndConst[0].strip())
            elif leftSide == "za":
                print('KR_ZA ' + str(currentLine) + ' ' + identifikAndConst[0].strip())
            elif leftSide == "az":
                print('KR_AZ ' + str(currentLine) + ' ' + identifikAndConst[0].strip())
            else:
                if leftSide[0].isnumeric():
                    print('BROJ ' + str(currentLine) + ' ' + identifikAndConst[0].strip())
                else:
                    print('IDN '+str(currentLine)+' '+identifikAndConst[0].strip())

        print('OP_PRIDRUZI '+str(currentLine)+' =')

        printRightSide(identifikAndConst[1], str(currentLine))

    elif string.__contains__('za'):
        print('KR_ZA '+str(currentLine)+' za')
        findIteratorVariable = string[string.index('za')+2:string.index('od'):1].strip()
        printRightSide(findIteratorVariable,str(currentLine))

        print('KR_OD '+str(currentLine)+' od')
        findStart = string[string.index('od')+2:string.index('do'):1].strip()
        printRightSide(findStart,str(currentLine))

        print('KR_DO ' + str(currentLine) + ' do')
        findN = string[string.index('do')+2:len(string):1]
        printRightSide(findN,str(currentLine))

    elif string.__contains__('az'):
        print('KR_AZ '+str(currentLine)+' az')
    else:
        printRightSide(string, str(currentLine))

