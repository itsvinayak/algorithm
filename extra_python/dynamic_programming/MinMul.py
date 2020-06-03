######################## too slow ####################
def MinMulRec(n):
    if n <= 3:
        return n
    ans = n
    for i in range(1, n + 1):
        temp = i * i
        if temp < n:
            ans = min(ans, 1 + MinMulRec(n - temp))
        else:
            break
    return ans


######################################################


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        print(MinMulRec(n))
