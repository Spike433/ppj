import sys
buffer = []
run = True
while run:
    line = sys.stdin.readline().rstrip('\n')
    if line == '$':
        run = False
    else:
        if line.isnumeric():
            buffer.append(line)
        else:
            buffer.append('\''+line+'\'')

value=0
endResult = []
for item in buffer:
    if item.__contains__("{2}"):
        oneLine = ','.join(endResult)
        oneLine = ('('*1)+oneLine + ('),'*1)
        print(oneLine)
        endResult = []

    if item.__contains__(":") and not item.__contains__("http") :
        endResult.append(buffer[value+1])
    value=value+1
