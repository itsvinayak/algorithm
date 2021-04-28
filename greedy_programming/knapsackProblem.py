class Sack:
    def __init__(self, wt, val):
        self.wt = wt
        self.val = val
        self.cost = val // wt

    def __lt__(self, other):
        return self.cost < other.cost


def knapsack(wt, val, W):
    item = []
    for i in range(len(wt)):
        item.append(Sack(wt[i], val[i]))

    item.sort(reverse=True)

    totalValue = 0
    for i in range(len(item)):
        curWt = item[i].wt
        curVal = item[i].val

        if W - curWt >= 0:
            W -= curWt
            totalValue += curVal
        else:
            fraction = W / curWt
            totalValue += curVal * fraction
            W = int(W - (curWt * fraction))
            break
    return totalValue


def main():
    wt = [10, 40, 20, 30]
    val = [60, 40, 100, 120]
    W = 50
    print(knapsack(wt, val, W))


if __name__ == "__main__":
    main()
