a = input()
a = a[3:len(a) - 3]
a = a.split("11")

for i in a:
    x = i.split("1")

    print('delta(', end="")

    print('q' + str(len(x[0]) - 1), end="")

    print(', ', end="")

    if (len(x[1]) == 3):
        print('B', end="")
    else:
        print(str(len(x[1]) - 1), end="")

    print(') = (', end="")

    print('q' + str(len(x[2]) - 1), end="")

    print(', ', end="")

    if (len(x[3]) == 3):
        print('B', end="")
    else:
        print(str(len(x[3]) - 1), end="")

    print(', ', end="")

    if (len(x[4]) == 1):
        print('L', end="")
    else:
        print('R', end="")

    print(")")