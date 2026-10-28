## 4. Matrix Multiplication

**Suggested Time:** 20–25 minutes

### Problem Description

Given two matrices, `A` and `B`, calculate their product matrix.

Matrix multiplication is possible only when the number of columns in matrix `A` equals the number of rows in matrix `B`.

The resulting matrix will have the same number of rows as matrix `A` and the same number of columns as matrix `B`.

### Example

**Matrix A:**
```python
A = [[1, 2],
     [3, 4]]
```

**Matrix B:**
```python
B = [[5, 6],
     [7, 8]]
```

**Output:**
```text
Product Matrix:
[19, 22]
[43, 50]
```

**Explanation:**

Each element in the product matrix is calculated by multiplying the elements of a row in matrix `A` by the corresponding elements of a column in matrix `B`, then adding the results.

For example:

- First row, first column: `(1 × 5) + (2 × 7) = 19`
- First row, second column: `(1 × 6) + (2 × 8) = 22`
- Second row, first column: `(3 × 5) + (4 × 7) = 43`
- Second row, second column: `(3 × 6) + (4 × 8) = 50`

### Constraints

- Use nested loops. Three levels of loops are required.
- Do not import libraries such as `numpy`.
- Do not use list comprehensions.
- Dynamically build the result matrix based on the dimensions of matrices `A` and `B`.
- Do not hardcode the answer.
- Ensure that the matrices have compatible dimensions before performing multiplication.

### Skills Tested

- Advanced nested loops
- Matrix dimensions and compatibility
- List indexing
- Accumulators for calculating matrix elements
- Dynamic list creation and manipulation
- Mathematical logic and problem-solving