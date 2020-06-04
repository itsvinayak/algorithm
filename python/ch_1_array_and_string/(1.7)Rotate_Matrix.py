#  List = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
#
#  Ans = [[1,4,7],
#         [2,5,8],
#         [3,6,9]]


def RotateMatrix(List):
    for i in range(int(len(List))):
        for j in range(i, int(len(List))):
            List[i][j], List[j][i] = List[j][i], List[i][j]
    return List


if __name__ == "__main__":
    print(RotateMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
