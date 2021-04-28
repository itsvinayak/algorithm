#         0 1 2
# m = 0 [[1,2,3],
#     1  [4,5,6],
#     2  [6,7,8]]
#
# m'= [[1,4,6],
#      [2,5,7],
#      [3,6,8]]


def transpose(m):
    for i in range(len(m)):
        for j in range(i, len(m)):
            m[i][j], m[j][i] = m[j][i], m[i][j]
    return m


if __name__ == "__main__":
    print(transpose([[1, 2, 3], [4, 5, 6], [6, 7, 8]]))
