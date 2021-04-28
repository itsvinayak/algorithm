#    question is to find all PowerSet for a given set
#
#  {1,2} == total no. of PowerSet is 2**n, where n in no. of element
#
##########################################
#   [1, 2, 3]
#      |
#   [1, 2, 3]
#   [1, 2]
#   [1, 3]
#   [1]
#   [2, 3]
#   [2]
#   [3]
#   []
#
##########################################
#
#     {}
#      |
#     / \
#    {1} {}
#     |   |
#    / \   \
#   {1,2}  {2}
#
##########################################


def PowerSet(s, subset, index):
    if index == len(s):
        print(subset)
        return
    PowerSet(s, subset + [s[index]], index + 1)
    PowerSet(s, subset, index + 1)


if __name__ == "__main__":
    PowerSet([1, 2], [], 0)
