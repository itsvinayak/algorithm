def fistNegativeNumber(array,k):
    i = 0
    j = 0
    negativeArray = []
    while j < len(array):
        if j-i+1 < k:
            j+= 1
        elif j-i+1 == k:
            if array[i] < 0:
                negativeArray.append(array[i])
            else:
                negativeArray.append(0)
            j += 1
            i += 1

    return negativeArray


def main():
    array = [12,-1,-7,8,-15,30,18,28]
    # -1 -1 -7 -15 -15 0
    k = 3
    print(fistNegativeNumber(array,k))


if __name__ == "__main__":
    main()









