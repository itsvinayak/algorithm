def knapsack(W,w,v,n):
    
    #base case
    if n == 0 or W == 0:
        return 0
    elif w[n-1] > W:
        return knapsack(W,w,v,n-1)
    else:
        return max(v[n-1]+knapsack(W-w[n-1],w,v,n-1),knapsack(W,w,v,n-1))

def main():
    v = [60,100,120]
    w = [10,20,30]

    W = 50

    print(knapsack(W,w,v,len(v)))

if __name__ == '__main__':
    main()
