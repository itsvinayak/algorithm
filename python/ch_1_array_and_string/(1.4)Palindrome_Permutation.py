# Given a string, write a function to check if it is a permutation of a palin­
# drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.


def checkMaxOneOdd(map):
    foundOdd = False
    for i in map.keys():
        if map[i] % 2 == 1:
            if foundOdd:
                return 0
            foundOdd = True
    return 1


def palindromePermutation(s):
    map = {}
    c = 0
    for i in s:
        if i != " ":
            if i in map.keys():
                map[i] += 1
            else:
                map[i] = 1
    print(map)

    return checkMaxOneOdd(map)


if __name__ == "__main__":
    print(palindromePermutation(input()))
