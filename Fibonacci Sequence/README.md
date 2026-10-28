## 2. Fibonacci Sequence — Even Sum

**Suggested Time:** 15–20 minutes

### Problem Description

Given a positive integer `N`, print the first `N` numbers of the Fibonacci sequence. Calculate and print the sum of all even numbers in the sequence. Finally, print the sequence in reverse order.

The Fibonacci sequence starts with `0` and `1`. Each subsequent number is the sum of the two preceding numbers.

### Example

**Input:**
```python
N = 8
```

**Output:**
```text
Sequence: 0, 1, 1, 2, 3, 5, 8, 13
Even Sum: 10
Reversed: 13, 8, 5, 3, 2, 1, 1, 0
```

**Explanation:**

- The first 8 Fibonacci numbers are `0, 1, 1, 2, 3, 5, 8, 13`.
- The even numbers are `0, 2, 8`, and their sum is `10`.
- The reversed sequence is `13, 8, 5, 3, 2, 1, 1, 0`.

### Constraints

- Generate the Fibonacci sequence using a loop. Do not use recursion.
- Do not store the sequence in a list or array for reversing.
- Print the reversed sequence using mathematical logic or string-building techniques. Do not use slicing (`[::-1]`) or the `.reverse()` method.
- Do not use the built-in `sum()` function.
- Do not import any libraries.

### Skills Tested

- Variable management and state swapping
- Loops and conditional statements
- Fibonacci sequence generation
- Accumulators for calculating sums
- Identifying even numbers using the modulo operator (`%`)
- String and number manipulation
- Reversing output without storing the sequence in a list