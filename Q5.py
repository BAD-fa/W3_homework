def blue_red(numbers: list, colors: list):
    colored_number = sorted(zip(colors, numbers))
    for i, (c, n) in enumerate(colored_number, 1):
        if c == 'B' and i > n or c == 'R' and i < n:
            return 'NO'
    return 'YES'


t = int(input())
for j in range(t):
    l = int(input())
    numb = list(map(int, input().split(' ')))
    color = input()
    print(blue_red(numb, color))
