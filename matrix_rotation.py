def matrix_rotation(A):
    for i in range(len(A)):
        for j in range(i, len(A)):
            A[i][j], A[j][i] = A[j][i], A[i][j]
    for i in range(len(A)):
        left = 0
        right = len(A)-1
        while left < right:
            A[i][left], A[i][right] = A[i][right], A[i][left]
            left += 1
            right -= 1
    return A


def main():
    rotation = matrix_rotation([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    for row in rotation:
        print(row)
    rotation2 = matrix_rotation(
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
    for row in rotation2:
        print(row)


if __name__ == "__main__":
    main()
