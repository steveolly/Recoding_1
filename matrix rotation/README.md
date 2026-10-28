## 8. Matrix Rotation (90 Degrees Clockwise)

**Suggested Time:** 20–25 minutes

### Problem Description

Given an `N × N` two-dimensional matrix, rotate it 90 degrees clockwise **in-place**.

In-place means modifying the original matrix directly without creating a new matrix to store the rotated result.

### Example

**Input:**
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

**Output:**
```text
[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]
```

### Constraints

- Modify the original matrix in-place. Do not create a new matrix.
- Swap values within the existing two-dimensional list.
- First, transpose the matrix by swapping rows and columns. Then, reverse each row to complete the clockwise rotation.
- Do not use slicing (`[::-1]`) to reverse rows.
- Use nested loops to perform the required operations.
- Do not import any libraries.
- Do not hardcode the result.

### Skills Tested

- Two-dimensional list manipulation
- In-place swapping
- Nested loops and indexing
- Matrix transposition
- Reversing lists without slicing
- Breaking a complex algorithm into smaller steps
- Efficient memory usage