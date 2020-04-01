# Assume you have a method isSubstring which checks if one word is a substring
# of another. Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one
# call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat").


def isSubstring(s1: str, s2: str) -> int:
    for i in range(len(s1)):
        for j in range(i, len(s1)):
            if s1[i : j + 1] == s2:
                return 1

    return 0


def isRotation(s1: str, s2: str) -> int:
    if len(s1) == len(s2) and len(s1) > 0:
        s1s1 = s1 + s1
        return isSubstring(s1s1, s2)
    return 0


if __name__ == "__main__":
    print(isRotation("waterbottle", "erbottlewat"))

