# There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.


def oneAway(s1,s2):
    if len(s1) == len(s2):
        return oneEditReplace(s1,s2)
    elif abs(len(s1)-len(s2)) == 1 :
        return oneEditInsert(s1,s2)
    return 0


# function to see only one element is different
def oneEditReplace(s1,s2):
    foundDifferent = False
    for i in range(len(s1)):
        if s1[i] != s2[i] :
            if foundDifferent:
                return 0
            foundDifferent = True
    return 1


def oneEditInsert(s1,s2):
    
