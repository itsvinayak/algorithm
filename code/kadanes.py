def findMaxSubarraySum(l):
    maxSum = l[0]
    tempSum = l[0]

    for i in range(len(l)):
        tempSum = max(l[i], tempSum + l[i])

        if maxSum < tempSum:
            maxSum = tempSum

    return maxSum


if __name__ == "__main__":
    print(findMaxSubarraySum([-2, 3, 4, 2]))
