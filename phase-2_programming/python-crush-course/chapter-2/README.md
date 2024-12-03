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

#### Difference between Syntax and Semantic errors in Programming.
**Syntax - the Rules of the Road**

- In Python, even small typos like a missing bracket or an extra comma can lead to syntax errors, preventing your code from running.
- Pay close attention to details and be mindful of potential syntax errors like misspellings, incorrect indentations, and mismatched data types.

**Semantics - Ensuring Your Code Does What You Want**

- Semantics deals with the meaning and logic of your code. Even if your code is syntactically correct, it might not produce the desired output if the logic is flawed.
- Common semantic errors include unintended output due to incorrect code logic and poorly structured code design.

* Syntax errors occur when you violate these rules, like misspelling a word or forgetting a punctuation mark.

* Semantic errors occur when your code is syntactically correct and runs without issues, but it doesn't produce the intended output because of flawed logic.


#### Arithmetic operators
Python can calculate numbers using common mathematical operators, along with some special operators, too:  

- x + y            Addition + operator returns the sum of x plus y
- x - y             Subtraction - operator returns the difference of x minus y
- x * y            Multiplication * operator returns the product of x times y
- x / y             Division / operator returns the quotient of x divided by y
- x**y            Exponent ** operator returns the result of raising x to the power of y 
- x**2            Square expression returns x squared
- x**3            Cube expression returns x cubed
- x**(1/2)    Square root (½) or (0.5) fractional exponent operator returns the square root of x
- x // y           Floor division operator returns the integer part of the integer division of x by y
- x % y          Modulo operator returns the remainder part of the integer division of x by y

#### Order of operations
The order of operations are to be calculated from left to right in the following order: 

- Parentheses ( ), { }, [ ]
- Exponents xy   (x**y)
- Multiplication * and Division /  
- Addition + and Subtraction -    

You might find the PEMDAS mnemonic device to be helpful in remembering the order.


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
