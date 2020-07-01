class Sort:
    def __init__(self, array):
        self.array = array

    def __str__(self):
        return f"array is {self.array}"

    def bubbleSort(self):
        length = len(self.array)

        for i in range(length):
            for j in range(length - i - 1):
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]


def main():
    array = [1, 0, 2, 9, 3, 4, 6, 7, 8]
    s = Sort(array)
    print(s)
    s.bubbleSort()
    print(s)


if __name__ == "__main__":
    main()
