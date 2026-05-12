# Day 1 - Introduction to Python

## Installation and Setting up the Environment

## Basic Data Types

### Python Basic Data Types

**1. Integer (int)**
Whole numbers, positive or negative, with no decimal point.

```py
age = 25
temperature = -10
count = 0
```
**2. Float (float)**
Numbers with a decimal point.

```py
price = 9.99
pi = 3.14159
weight = -2.5
```
**3. String (str)**
Text — any sequence of characters wrapped in quotes (single or double).

```py
name = "Alice"
greeting = 'Hello, World!'
sentence = "Python is fun"
```

You can combine strings:

`full_name = "Alice" + " " + "Smith"  # "Alice Smith"`

**4. Boolean (bool)**
Only two possible values: True or False. Used for logic and conditions.

```py
is_sunny = True
has_homework = False
```

**5. List (list)**
An ordered collection of items. Can mix types. Items can be changed.

```py
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", True]
fruits[0]  # "apple"
```

**6. Tuple (tuple)**
Like a list, but cannot be changed after creation.

```py
coordinates = (10, 20)
rgb = (255, 128, 0)
```

**7. Dictionary (dict)**
Stores data as key-value pairs, like a real dictionary word → definition.

```py
person = {
    "name": "Alice",
    "age": 25,
    "city": "London"
}
person["name"]  # "Alice"
```

**8. Set (set)**
An unordered collection of unique items (no duplicates).

```py
colors = {"red", "green", "blue"}
numbers = {1, 2, 2, 3}  # stored as {1, 2, 3}
```

**Checking the Type of a Variable**
Use the built-in type() function:

```py
x = 42
print(type(x))        # <class 'int'>
y = "hello"
print(type(y))        # <class 'str'>
z = [1, 2, 3]
print(type(z))        # <class 'list'>
```

## Operations and Expressions

## Variables

## Printing to the console

