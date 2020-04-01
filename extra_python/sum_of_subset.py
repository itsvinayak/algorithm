# to find any subset whose sum will equal to n
# s = (1,2) n=2
#            ()
#            |
#           / \
#          (1) ()
#           |  |
#          / \  \
#       (1,2)(1) (2)=ans



def subsetSum(subset,n,index):
    if n != 0 and index == len(subset) :
        return False
    elif n == 0:
        return True 
    else:
        return subsetSum(subset,n-subset[index],index+1) or subsetSum(subset,n,index+1)

if __name__ == "__main__":
    print(subsetSum([1,2],2,0))

