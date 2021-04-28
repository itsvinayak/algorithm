# recursion
def TripleStep(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return TripleStep(n - 1) + TripleStep(n - 2) + TripleStep(n - 3)


if __name__ == "__main__":
    print(TripleStep(3))
