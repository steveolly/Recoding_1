## 7. Roman to Integer

**Suggested Time:** 20–25 minutes

### Problem Description

Given a string representing a Roman numeral, convert it into its corresponding integer.

Roman numerals use the following symbols and values:

| Symbol | Value |
|---|---:|
| `I` | 1 |
| `V` | 5 |
| `X` | 10 |
| `L` | 50 |
| `C` | 100 |
| `D` | 500 |
| `M` | 1000 |

When a smaller numeral appears before a larger numeral, subtract the smaller value from the larger one. Otherwise, add the values together.

For example, `IV` represents `4` because `I` comes before `V`, so `1` is subtracted from `5`.

### Examples

**Example 1**

**Input:**
```python
roman = "III"
```

**Output:**
```text
3
```

**Example 2**

**Input:**
```python
roman = "LVIII"
```

**Output:**
```text
58
```

**Explanation:** `L = 50`, `V = 5`, and `III = 3`. The total is `50 + 5 + 3 = 58`.

**Example 3**

**Input:**
```python
roman = "MCMXCIV"
```

**Output:**
```text
1994
```

**Explanation:** `M = 1000`, `CM = 900`, `XC = 90`, and `IV = 4`. The total is `1000 + 900 + 90 + 4 = 1994`.

### Constraints

- Store Roman numeral symbols and their corresponding values in a dictionary.
- Use a `while` loop to traverse the string.
- Use string indexing and look-ahead logic to compare the current numeral with the next numeral.
- Apply subtraction when a smaller numeral appears before a larger numeral; otherwise, add the current value.
- Do not import any libraries.
- Do not hardcode the answers. The solution must work dynamically for different inputs.

### Skills Tested

- Dictionary creation and lookup
- String indexing
- Look-ahead logic
- `while` loops
- Conditional statements
- Addition and subtraction logic
- Translating mathematical rules into Python code