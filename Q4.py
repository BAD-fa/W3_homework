def era(sequence: list, i=1, res=0):
    if not len(sequence):
        return res

    else:
        ai = sequence[0]
        if ai <= (i + res):
            i += 1

        else:
            res += ai - (i + res)
            i += 1

        return era(sequence[1:], i, res)


t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split(' ')))
    print(era(a))
