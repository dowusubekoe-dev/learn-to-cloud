# **Day 1: Getting Started with Python**


## **Objective** 

Set up Python and run a basic script.


### Steps:

1. Install Python from [python.org](https://www.python.org/).
2. Install an IDE like [VS Code](https://code.visualstudio.com/docs/python/python-quick-start) and the Python extension.
3. Write and execute your first Python script.


### **Brief Description**

Python is a versatile and beginner-friendly programming language. On this day, you will learn to install Python, configure a code editor, and write simple programs. By completing this lesson, you’ll have a fully functional Python environment and confidence to execute basic scripts.

**Python Environment Check**:

```bash
python --version
```

**Open Python Terminal**:

```bash
python3 # Hit Enter
```

**Create a Python File**:

```bash
echo 'print("Hello, Python!")' > hello.py
```

**Running Interactive Shell**:

```py
>>> print("Interactive Python Shell")
```


### **Code Snippets**

1. Basic Hello World Program:

```py
print("Hello, World!")
```

2. Assigning Variables:

```py
name = "Alice"
age = 25
print(f"My name is {name}, and I am {age} years old.")
```

3. Arithmetic Operations:

```py
Copy code
num1 = 10
num2 = 5
print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
```

4. Running Python in the Terminal:

```bash
python
```

5. Writing a Python Script File:

```bash
echo 'print("Welcome to Python!")' > script.py
python script.py
```

6. Using Comments:

```py
# This is a comment
print("Comments are ignored by Python.")
```

7. Checking Python Version:

```bash
python --version
```

8. Using Input:

```py
name = input("What is your name? ")
print(f"Hello, {name}!")
```

9. Handling Errors:

```py
try:
    print(undefined_variable)
except NameError:
    print("Variable is not defined.")
```

10. Importing Modules:

```py
import math
print(math.sqrt(16))  # Prints the square root of 16
```

### **Exercises**

1. Write a script that:

    - Prints your name.
    - Prints your favorite programming language. Example:

    ```py
    print("My name is John.")
    print("My favorite programming language is Python.")
    ```


2. Modify the Hello World program to greet you by name:

    ```py
    print("Hello, Alice! Welcome to Python programming.")
    ```

3. Create a Python script (first_script.py) that:

    - Prints "I am learning Python!".
    - Calculates and prints the sum of 10 and 20.
    
4. Use Python’s interactive shell to:

    - Compute the square of 4 using ** operator.
    - Divide 15 by 4 and print the result.
    
5. Experiment with running invalid code (e.g., print(5 / 0)) and observe the error messages.

