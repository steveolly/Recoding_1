def matrix_mul(A, B):
    if len(A[0]) != len(B):
        return "You can not multiply Matrix A & B"

    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            total = 0
            for k in range(len(B)):
                total += A[i][k] * B[k][j]
            row.append(total)
        result.append(row)
    return result


def main():
    product = matrix_mul([[1, 2], [3, 4]], [[5, 6], [7, 8]])

    for row in product:
        print(row)


if __name__ == "__main__":
    main()
