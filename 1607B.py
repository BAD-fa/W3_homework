def grasshopper(x0: int, n: int):
    for i in range(1, n+1):
        if x0 % 2:
            x0 += i
        else:
            x0 -= i

    return x0


t = int(input())
for i in range(t):
    x0, n = tuple(map(int, input().split(' ')))
    print(grasshopper(x0, n))
