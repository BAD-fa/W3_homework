def linear_keyboard(order: str, word: str, time=0):
    if len(word) < 2:
        return time

    t1 = order.index(word[:1])
    t2 = order.index(word[1:2])

    time += abs(t1 - t2)

    return linear_keyboard(order, word[1:], time)


t = int(input())
for i in range(t):
    order = input()
    word = input()
    print(linear_keyboard(order, word))
