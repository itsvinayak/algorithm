def recursiveUnboundedKnapsack(val, wt, W, n):
    if n == 0 or W == 0:
        return 0
    elif wt[n - 1] > W:
        return recursiveUnboundedKnapsack(val, wt, W, n - 1)
    else:
        return max(
            val[n - 1] + recursiveUnboundedKnapsack(val, wt, W - wt[n - 1], n),
            recursiveUnboundedKnapsack(val, wt, W, n - 1),
        )


if __name__ == "__main__":
    val = [40, 60, 50]
    wt = [12, 20, 15]
    n = 3
    W = 45
    print(recursiveUnboundedKnapsack(val, wt, W, n))
