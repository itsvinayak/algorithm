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


def PowerSet(s,subset,index):

      if index == len(s):
        print(subset)
        return
      print(s[index])
      print("-> ", index)
      PowerSet(s, subset.append(s[index-1]), index + 1)
      PowerSet(s, subset, index + 1)



if __name__ == "__main__":
    PowerSet([1,2,3],[],0)
