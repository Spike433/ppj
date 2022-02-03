currentLine=5

def printRightSide(rightSide, currLine):
    splitBySpace = rightSide.split(' ')

    for word in splitBySpace:
        variable = 'IDN '+currLine+' '
        number='BROJ '+ currLine+ ' '
        isVariable = False
        isNumber = False
        firstLetter = True

        for char in word:
            if char == '/':
                return
            if char == '(':
                if isVariable:
                    isVariable = False
                    print(variable)
                    variable = 'IDN ' + currLine + ' '
                elif isNumber:
                    isNumber = False
                    print(number)
                    number='BROJ '+ currLine+ ' '

                print('L_ZAGRADA '+currLine+' (')
            elif char == ')':
                if isVariable:
                    isVariable=False
                    print(variable)
                    variable = 'IDN ' + currLine + ' '
                elif isNumber:
                    isNumber = False
                    print(number)
                    number='BROJ '+ currLine+ ' '

                print('R_ZAGRADA ' + currLine + ' )')
            elif char == '+':
                if isVariable:
                    isVariable=False
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
                    firstLetter = False
                elif (char.isalpha() or char.isdigit() ) and isVariable:
                    variable += char
                else:
                    number+=char
                    isNumber = True
        if isVariable:
            print(variable)
        elif isNumber:
            print(number)

printRightSide('rez +  /10+ 10 + ( i22s * i*i + 10',str(currentLine))