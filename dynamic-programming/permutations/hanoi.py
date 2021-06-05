def pmove(f, t):
    print(f"Move disk from {f} to {t}!")


def move(f, t):
    t.append(f.pop())


def hanoi(n, f, h, t):
    if n == 0:
        return

    hanoi(n - 1, f, t, h)
#    pmove(f, t)
    move(f, t)
    hanoi(n - 1, h, f, t)


a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = []
c = []

print(a, b, c)
hanoi(len(a), a, b, c)
print(a, b, c)
