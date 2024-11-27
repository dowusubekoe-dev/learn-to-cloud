# Variables and Simple Data Types

## Variables
Variables are containers for storing data values.
A **variable** is created when a **value** is assigned to it.

```py
message = "Python Crush Course"
print(message)
```
## Naming and Using Variables
Naming **variables** involves some rules that needs to be followed.

1. **Rules for Variable Names in Python**:
   - Variable names can contain letters, numbers, and underscores.
   - Must start with a letter or an underscore, not a number.
   - No spaces allowed; use underscores to separate words.
   - Avoid using Python keywords and built-in function names (e.g., `print`).
   - Names should be short but descriptive (e.g., `student_name` is better than `s_n`).
   - Avoid lowercase `l` and uppercase `O` to prevent confusion with `1` and `0`.

2. **Good Practices**:
   - Use lowercase letters for variable names.
   - Uppercase letters in variable names have special meanings.

3. **Debugging Name Errors**:
   - A common error is misspelling variable names (e.g., `mesage` instead of `message`).
   - Python provides a **traceback** to help locate errors.

4. **Improving Variable Naming Skills**:
   - With practice and exposure to others’ code, you can create more meaningful names.

### **Strings Overview:**
1. **Definition**: A string is a series of characters enclosed in quotes (`'` or `"`), e.g., `"This is a string"` or `'This is also a string'`.
2. **Flexibility**: Strings can contain quotes or apostrophes if appropriate quoting is used, e.g., `'I said, "Hello!"'` or `"Python's strength lies in its community."`.

---

#### **Manipulating Strings with Methods:**
1. **Changing Case**:
   - `title()`: Capitalizes the first letter of each word.
   - `upper()`: Converts all characters to uppercase.
   - `lower()`: Converts all characters to lowercase (useful for standardized storage).

2. **Whitespace Handling**:
   - **Tabs/Newlines**:
     - `\t`: Adds a tab.
     - `\n`: Moves to a new line.
   - **Stripping Extra Whitespace**:
     - `rstrip()`: Removes trailing whitespace.
     - `lstrip()`: Removes leading whitespace.
     - `strip()`: Removes both leading and trailing whitespace.

3. **Removing Prefixes**:
   - `removeprefix()`: Removes a specified prefix, e.g., `url.removeprefix('https://')`.

---

#### **Using Variables in Strings:**
1. **f-strings**:
   - Embed variable values in strings using `{}` with an `f` prefix, e.g., `f"Hello, {name}!"`.
   - Supports method chaining, e.g., `f"{name.title()}"`.

2. **Combining Variables**:
   - Combine first and last names for formatting:  
     ```python
     full_name = f"{first_name} {last_name}"
     print(f"Hello, {full_name.title()}!")
     ```
---

#### **Avoiding Syntax Errors:**
1. **Correct Usage of Quotes**:
   - Double quotes can contain apostrophes, e.g., `"Python's strengths"`.
   - Mixing single quotes and apostrophes without escaping (`\'`) leads to syntax errors.

2. **Error Example**:  
   ```python
   message = 'Python's strengths'
   # Produces a SyntaxError
   ```

## Numbers
Integer: Whole numbers, e.g., 2, 10.
Float: Decimal numbers, e.g., 3.14, 0.5.
Arithmetic Operators:
+: Addition
-: Subtraction
*: Multiplication
/: Division (always returns a float)
**: Exponentiation
 %: Modulus (remainder)