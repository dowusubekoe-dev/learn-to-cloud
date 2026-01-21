# **Day 4: Numbers and Arithmetic**

## **Objective**

Understand Python's number types and perform arithmetic operations.

### **Steps**:

1. Learn about integers, floats, and type conversion.
2. Perform basic arithmetic operations.
3. Explore mathematical functions using the math module.

### **Brief Description**

Python supports both integers and floating-point numbers. Arithmetic operations such as addition, subtraction, multiplication, and division are essential for programming. Python also provides built-in and module-based functions for advanced calculations.

### **Code Snippets**

**Basic Arithmetic**:

```py
print(5 + 3)  # 8
print(10 - 7)  # 3
print(4 * 2)  # 8
print(16 / 4)  # 4.0
```

**Exponents**:

```py
print(2**3)  # 8
```

**Floor Division and Modulus**:

```py
print(15 // 4)  # 3
print(15 % 4)  # 3
```

**Type Conversion**:

```py
age = "25"
print(int(age) + 5)  # 30
```

**Using the math Module**:

```py
import math
print(math.sqrt(16))  # 4.0
print(math.pi)  # 3.141592653589793
```

**Rounding Numbers**:

```py
print(round(5.678, 2))  # 5.68
```

**Absolute Values**:

```py
print(abs(-7))  # 7
```

**Min and Max Functions**:

```py
numbers = [3, 5, 2, 8, 6]
print(min(numbers))  # 2
print(max(numbers))  # 8
```

**Power Function**:

```py
print(pow(2, 3))  # 8
```

**Random Numbers**:

```py
import random
print(random.randint(1, 10))  # Random number between 1 and 10
```

### **Exercises**

1. Write a program to calculate and print the area of a circle given its radius.

2. Create a program that converts a temperature from Celsius to Fahrenheit.

3. Use the math module to compute the square root and logarithm of a number.

4. Generate 5 random numbers between 1 and 100 and print them.

5. Given two numbers, calculate their:

      - Sum.
      - Difference.
      - Product.
      - Quotient.
