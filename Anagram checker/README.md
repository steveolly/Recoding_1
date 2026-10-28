## 6. Anagram Checker

**Suggested Time:** 15–20 minutes

### Problem Description

Given two strings, determine whether they are anagrams of each other.

An **anagram** is a word or phrase formed by rearranging the letters of another word or phrase, using every original letter exactly once.

For this exercise, uppercase and lowercase letters should be treated as the same.

### Examples

**Example 1**

**Input:**
```python
str1 = "listen"
str2 = "silent"
```

**Output:**
```text
Anagram
```

**Example 2**

**Input:**
```python
str1 = "hello"
str2 = "world"
```

**Output:**
```text
Not an anagram
```

**Example 3**

**Input:**
```python
str1 = "Dormitory"
str2 = "dirtyroom"
```

**Output:**
```text
Anagram
```

### Constraints

- Treat uppercase and lowercase letters as the same.
- Do not use the built-in `sort()` or `sorted()` functions.
- Do not use `set()`.
- Build a character-frequency dictionary manually for each string.
- Compare the two dictionaries to determine whether the strings are anagrams.
- Do not import any libraries.

### Skills Tested

- Dictionary creation and manipulation
- Character-frequency counting
- String iteration and normalization
- Comparing dictionaries and data structures
- Conditional statements
- Logical problem-solving