# Implement an algorithm to determine if a string has all unique characters. What if you
#   cannot use additional data structures?


def is_unique(s):
    s = list(s)
    s.sort()

    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return 0
    else:
        return 1


if __name__ == "__main__":
    print(is_unique(input()))
