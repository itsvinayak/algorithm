

# There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.


def oneAway(s1,s2):
    c=0
    for i in s1:
        if i not in s2:
            c+=1
    if c>1:
        return False
    else:
        return True



if __name__ == "__main__":
    s1,s2 = map(str,input().split())
    print(oneAway(s1,s2))


 
