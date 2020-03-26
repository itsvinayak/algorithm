#   {1,2} == total no. of PowerSet is 2**n, where n in no. of element
#
#     {}
#      |
#     / \
#    {1} {}    |
#     |   |
#    / \   \
#   {1,2}  {2}
#
#

#
#
# def PowerSet(s):
#     subset = []
#     helper(list(s),subset,0)
#
# def helper(s,subset,i):
#     if i == len(s)-1:
#         print(subset)
#     else:
#         helper(s,subset,i+1)
#         print('--> ',i)
#         subset.append(s[i])
#         helper(s,subset,i+1)


def PowerSet(s):
    subset = [{}]
    s = lsit(s)
    for i in range(len(s)):
        for j in range(i):
            subset.append(s[j])


if __name__ == "__main__":
    PowerSet({1, 2})
