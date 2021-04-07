def MaxSumSubarray(array,k):
    i = 0
    j = 0
    
    Wsum = 0
    
    while j < k:
        Wsum += array[j]
        j+=1 
    sum = 0
    
    for i in range(k,len(array)):
        Wsum += array[i] - array[i-k]
        sum = max(sum,Wsum)
    return sum

def MaxSumSubarray2(array,k):
    i = 0
    j = 0
    max_sum = 0
    sum = 0
    while j < len(array):
        sum += array[j]
        if j-i+1 < k:
            j+=1
        elif j-i+1 == k:
            max_sum = max(max_sum,sum)
            sum -= array[i]
            i+=1
            j+=1
    return max_sum    


def main():
    array = [1,2,3,4,5,6,7,8,9]
    k = 3
    print(MaxSumSubarray(array,k))
    print(MaxSumSubarray2(array,k))


if __name__ == "__main__":
    main()
