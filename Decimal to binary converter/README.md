## 3. Decimal to Binary Converter

**Suggested Time:** 15–20 minutes

### Problem Description

Given a positive integer, convert it to its binary representation without using Python's built-in binary conversion functions.

### Examples

**Example 1**

**Input:**
```python
N = 10
```

**Output:**
```text
1010
```

**Example 2**

**Input:**
```python
N = 25
```

**Output:**
```text
11001
```

**Example 3**

**Input:**
```python
N = 1
```

**Output:**
```text
1
```

### Constraints

- Do not use the built-in `bin()` function.
- Do not use string formatting such as `f"{num:b}"`.
- Use the mathematical method of repeatedly dividing the number by `2` and tracking the remainders.
- Build the final binary string manually using string concatenation.
- Do not import any libraries.

### Skills Tested

- Mathematical algorithms
- Modulo operator (`%`)
- Integer division (`//`)
- String concatenation and manipulation
- Loops and conditional statements
- Converting decimal numbers to binary manually