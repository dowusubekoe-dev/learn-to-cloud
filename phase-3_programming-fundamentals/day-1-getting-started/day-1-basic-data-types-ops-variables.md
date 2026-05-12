# Day 1 - Introduction to Python

## Basic Data Types

Python has a number of built-in data types for storing and manipulating data. They include;

* **Numbers:** integers, floating-point numbers, and complex numbers
* **Strings** are character sequences.
* **Lists** are ordered groups of elements.
* **Tuples** are ordered immutable collections of elements.
* **Dictionaries** are collections of key-value pairs that are not ordered.

## Operations and Expressions

A variety of operations in Python, including **arithmetic**, **comparison**, and **logical operations** can be performed on the data types mentioned above.
Expressions can also be used to manipulate data, such as combining multiple values into a new value.

## Variables

A variable is declared and assigned a value in Python by using the assignment operator =.
The variable is on the left side of the operator, and the value being assigned is on the right.
For example:

```py
a = 7         # assign variable a the value 7
b = x + 3     # assign variable b the value of a plus 3
c = b         # assign variable c the value of b

```
There is no type declaration for the variables. This is due to the fact that Python is a dynamically typed language, which means that the variable type is determined by the data assigned to it.

Variable names are case sensitive and can contain any letter, number, or underscore ( ). They cannot, however, begin with a number.

A string is a sequence of one or more characters. Strings are typically declared with single quotation marks, but they can also be declared with double quotation marks:

```py
a = 'My name is Rishab'
b = "This is also a string"

```
You can add strings to other strings — an operation known as "concatenation" — with the same + operator that adds two numbers:

```py
x = 'My name is' + ' ' + 'Rishab'
print(x) # outputs: My name is Rishab

```

## Printing to the console

