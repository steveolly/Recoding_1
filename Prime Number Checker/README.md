## 1. Prime Number Checker — Optimized

**Suggested Time:** 12–15 minutes

### Problem Description

Given an integer `N`, determine whether it is a prime number. Then, find and print all prime numbers from `2` up to `N` and calculate their sum.

### Examples

**Example 1**

**Input:**
```python
N = 10
```

**Output:**
```text
10 is not prime.
Primes up to 10: [2, 3, 5, 7]
Sum of primes: 17
```

**Example 2**

**Input:**
```python
N = 7
```

**Output:**
```text
7 is prime.
Primes up to 7: [2, 3, 5, 7]
Sum of primes: 17
```

### Constraints

- Do not use `range()` to iterate from `2` to `N` directly when checking whether a number is prime. Use a `while` loop for the primality check.
- Optimize the primality check by stopping at the square root of the number. Use the condition `i * i <= num` without importing the `math` module.
- Do not use the built-in `sum()` function.
- Do not import any libraries.
- Do not hardcode the answers. Your solution must work dynamically for different input values.

### Skills Tested

- Loops and nested loops
- Conditional statements
- Mathematical logic and prime number detection
- Square root optimization using `i * i <= num`
- Accumulators for calculating totals
- Writing efficient and optimized Python code