def uglyrec(n, z):
    if n == 1:
        return z
    else:
        return min(uglyrec(n - 1, z * 2), uglyrec(n - 1, z * 3), uglyrec(n - 1, z * 5))


print(uglyrec(6, 1))
