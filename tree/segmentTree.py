from math import ceil, log2


def getMid(start, end):
    return start + (end - start) // 2


class segmentTree:
    def __init__(self, array):
        self.array = array
        length = len(array)
        self.height = int(ceil(log2(length)))
        # no. of node = size of array
        self.max_array_size = 2 * int(2 ** self.height) - 1
        self.SegmentTree = [0] * self.max_array_size
        self.constructTreeUtil(0, length - 1, 0)

    def constructTreeUtil(self, start, end, current):
        if start == end:
            self.SegmentTree[current] = self.array[start]
            return self.array[start]
        mid = getMid(start, end)

        self.SegmentTree[current] = self.constructTreeUtil(
            start, mid, (current * 2) + 1
        ) + self.constructTreeUtil(mid + 1, end, (current * 2) + 2)

        return self.SegmentTree[current]

    def update(self, index, val):
        n = len(self.array)
        if index < 0 or index > n - 1:
            print(f"index {index} is not valid !!")
            return

        diff = val - self.array[index]
        self.array[index] = val
        self.__updateUtil(0, n - 1, index, diff, 0)

    def __updateUtil(self, start, end, index, diff, current):
        if index < start or index > end:
            return

        self.SegmentTree[current] += diff

        if start != end:
            mid = getMid(start, end)
            self.__updateUtil(start, mid, index, diff, (2 * current) + 1)
            self.__updateUtil(mid + 1, end, index, diff, (2 * current) + 2)

    def sum(self, a, b):
        n = len(self.array)
        if a < 0 or b > n - 1 or a > b:
            return -1  # not valid range
        return self.__sumUtil(0, n - 1, a, b, 0)

    def __sumUtil(self, start, end, a, b, current):
        if a <= start and b >= end:
            return self.SegmentTree[current]
        if end < a or start > b:
            return 0

        mid = getMid(start, end)
        return self.__sumUtil(start, mid, a, b, (2 * current) + 1) + self.__sumUtil(
            mid + 1, end, a, b, (2 * current) + 2
        )

    def __str__(self):
        return f"Tree ==> {self.SegmentTree}"


def main():
    array = [1, 3, 5, 7, 9, 11]
    st = segmentTree(array)
    print(st.sum(1, 3))
    st.update(1, 10)
    print(st.sum(1, 3))


if __name__ == "__main__":
    main()
