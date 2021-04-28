# Given two strings, write a method to decide if one is a permutation of the
#  other.


def checkPremutation(s1, s2):
    s1 = list(s1)
    s2 = list(s2)
    s1.sort()
    s2.sort()
    if len(s1) == len(s2):
        if s1 == s2:
            return 1
    return 0


if __name__ == "__main__":
    print(checkPremutation(input(), input()))
