
inp = input()

if len(inp) % 2 == 0:

    isPalin = True

    done = []
    counts = []

    for x in inp:

        if x not in done:

            counts.append(inp.count(x))
            done.append(x)

    num = counts[0]

    for x in counts:

        if x % 2 == 1:
            isPalin = False

    if isPalin is False:
        print("NO")
    else:
        print("YES")

if len(inp) % 2 == 1:

    isPalin = 0

    done = []
    counts = []

    for x in inp:

        if x not in done:

            counts.append(inp.count(x))
            done.append(x)

    num = counts[0]

    for x in counts:

        if x != num:
            isPalin += 1

    if isPalin != 1:
        print("NO")
    else:
        print("YES")
