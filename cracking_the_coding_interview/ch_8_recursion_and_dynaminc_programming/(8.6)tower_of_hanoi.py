def hanoi(n, From, to, using):
    if n > 0:
        hanoi(n - 1, From, to, using)
        print("move disc from ", From, " to ", to)
        hanoi(n - 1, From, using, to)


if __name__ == "__main__":
    hanoi(3, "A", "B", "C")
