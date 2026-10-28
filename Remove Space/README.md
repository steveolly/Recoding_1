## 5. Remove Spaces & Capitalize Words

**Suggested Time:** 15–20 minutes

### Problem Description

Given a sentence, capitalize the first letter of every word and then create a second version of the sentence with all spaces removed.

You must perform both operations manually using loops, conditionals, and ASCII conversion.

### Example

**Input:**
```python
sentence = "hello world from python"
```

**Output:**
```text
Capitalized: "Hello World From Python"
No Spaces: "HelloWorldFromPython"
```

### Constraints

- Do not use the built-in `.replace()` method to remove spaces.
- Do not use the `.title()` or `.capitalize()` methods.
- Use loops and conditional statements to process the sentence.
- Use ASCII logic to capitalize the first letter of each word:
  - Check whether the character is between `'a'` and `'z'`.
  - Convert it to uppercase by subtracting `32` from its ASCII value using `ord()` and `chr()`.
- Do not import any libraries.
- Build both output strings manually.

### Skills Tested

- String manipulation
- ASCII character codes using `ord()` and `chr()`
- Loops and conditional statements
- Tracking the beginning of a word using flags
- String concatenation
- Building multiple outputs from a single input