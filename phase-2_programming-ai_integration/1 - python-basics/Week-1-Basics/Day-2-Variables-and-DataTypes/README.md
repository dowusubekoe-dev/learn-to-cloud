# **Day 2: Variables and Data Types**

## **Objective**

Understand variables and explore Python�s basic data types.

### **Steps**

Learn the rules for naming variables.
Explore basic data types: int, float, str, and bool.
Assign values to variables and manipulate them.

### **Brief Description**

Variables in Python are used to store and manipulate data. Python supports various data types, such as integers, floats, strings, and booleans. This lesson will teach you how to create variables, assign values, and use them in basic operations.

### **Code Snippets**

**Defining Variables**:

```py
name = "Alice"
age = 25
height = 5.6
is_student = True
```

**Printing Variables**:

```py
print(f"Name: {name}, Age: {age}, Height: {height}, Student: {is_student}")
```

**Reassigning Variables**:

```py
name = "Bob"
print(f"My name is now {name}.")
```

**Basic Data Types**:

```py
print(type(name))  # <class 'str'>
print(type(age))   # <class 'int'>
print(type(height)) # <class 'float'>
print(type(is_student)) # <class 'bool'>
```

**Constants**:

```py
PI = 3.14159  # By convention, constants are in uppercase
print(f"The value of PI is {PI}.")
```

**Multiple Variable Assignment**:

```py
x, y, z = 1, 2, 3
print(x, y, z)
```

**Underscores in Numbers**:

```py
large_number = 1_000_000
print(large_number)  # Outputs: 1000000
```

**Using Booleans**:

```py
is_raining = False
if not is_raining:
    print("You can go outside!")
```

**String Operations**:

```py
first_name = "Alice"
last_name = "Smith"
full_name = first_name + " " + last_name
print(full_name)
```

**Arithmetic Operations**:

```py
a = 5
b = 2
print(f"Sum: {a + b}, Difference: {a - b}, Product: {a * b}")
```

### **Exercises**

- Create a variable for each of the following and print them:

Your name.
Your age.
Your favorite color.

- Write a program that calculates and prints the area of a rectangle:

```py
length = 10
width = 5
area = length * width
print(f"The area of the rectangle is {area}.")
```

- Write a program to swap the values of two variables:

```py
x = 5
y = 10
x, y = y, x
print(f"x: {x}, y: {y}")
```

- Define constants for the speed of light (299792458 m/s) and gravitational constant (6.674�10^-11 m^3 kg^-1 s^-2). Print their values.

- Create a boolean variable and use it in a conditional statement to print a message based on its value.
