def shouldSwap(string, start, curr):
    for i in range(start, curr):
        if string[i] == string[curr]:
            return 0
    return 1

def findPermutations(string,index,n):
    if index >= n:
        print(''.join(string))
        return
    for i in range(index,n):
        check = shouldSwap(string,index,i)
        if check:
            string[i],string[index] = string[index],string[i]
            findPermutations(string,index+1,n)
            string[i],string[index] = string[index],string[i]

def main():
    string = "ABCA"
    findPermutations(list(string),0,len(string))


if __name__ == "__main__":
    main()
