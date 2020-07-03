def deleteMiddleElement(stack,k):
    # k = n//2 + 1
    if k == 1:
        stack.pop()
        return
    temp = stack.pop()
    deleteMiddleElement(stack,k-1)
    stack.append(temp)

def main():
    array = [3,5,6,7,8]
    k = (len(array) // 2) + 1
    print("before del :",*array)
    deleteMiddleElement(array,k)
    print("after del :",*array)

if __name__ == "__main__":
    main()
