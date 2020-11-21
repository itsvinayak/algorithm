
def MaxSumSubarray(array,k):
    i = 0
    j = 0
    while i != len(array):
        window = j - i + 1




def MaxSumSubarray2(array,k):
    ans = []
    for i in range(len(array)-k+1):
        ans.append(sum(array[i:i+k]))
    return ans

def main():
    array = [1,2,3,4,5,6,7,8,9]
    k = 3
    print(*MaxSumSubarray(array,k))


if __name__ == "__main__":
    main()
