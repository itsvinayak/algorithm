def lisRec(arr,n):
    c=0
    maxx=-1
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] <= arr[j]:
                c+=1
        maxx = max(maxx,c)
    return maxx


if __name__ == "__main__":
    arr = [10 , 22 , 9 , 33 , 21 , 50 , 41 , 60]
    print(lisRec(arr,len(arr)))



