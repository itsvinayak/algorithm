def ZeroMatrix(List):
    row = []
    column = []
    for i in range(len(List)):
        for j in range(len(List)):
            if List[i][j] == 0:
                row.append(i)
                column.append(j)

    for i in row:
        for j in range(len(List)):
            List[i][j] = 0

    for i in column:
        for j in range(len(List)):
            List[j][i] = 0

    return List


if __name__ == "__main__":
    print(ZeroMatrix([[1, 0, 3], [4, 5, 6], [7, 8, 9]]))
