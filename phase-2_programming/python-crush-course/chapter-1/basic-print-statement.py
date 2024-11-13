# 1. Hello, World!
print("Hello, World!")

# 2. Print a simple greeting
print("Welcome to Python!")

# 3. Print a number
print(5)

# 4. Print a floating-point number
print(3.14)

# 5. Print a mathematical expression
print(2 + 3)

# 6. Print a variable
name = "Alice"
print(name)

# 7. Print multiple values
print("Hello", "Alice")

# 8. Print with a custom separator
print("Python", "is", "fun", sep="-")

# 9. Print with an end character
print("Learning Python", end="!")
print(" It's great!")

# 10. Print a list of numbers
print([1, 2, 3, 4, 5])

# 11. Print a dictionary
print({"name": "Alice", "age": 25})

# 12. Print a multi-line string
print("""This is a
multi-line
string.""")

# 13. Print an escape sequence
print("This is a \"quote\".")

# 14. Print a tabbed line
print("Python\tRocks!")

# 15. Print Unicode characters
print("\u2602 Rainy")

# 16. Print boolean values
print(True)
print(False)

# 17. Print using f-strings
age = 25
print(f"Age is {age}")

# 18. Print with format method
print("Age is {}".format(age))

# 19. Print a large number with underscores
print(1_000_000)

# 20. Print a simple addition
print(10 + 5)

# 21. Print a subtraction
print(15 - 3)

# 22. Print a multiplication
print(4 * 5)

# 23. Print a division
print(10 / 2)

# 24. Print integer division
print(10 // 3)

# 25. Print modulus
print(10 % 3)

# 26. Print exponentiation
print(2 ** 3)

# 27. Print a rounded number
print(round(3.14159, 2))

# 28. Print a square root
print(16 ** 0.5)

# 29. Print a comparison
print(5 > 3)

# 30. Print a complex comparison
print(5 > 3 and 2 < 4)

# 31. Print using logical OR
print(5 > 3 or 2 > 4)

# 32. Print using logical NOT
print(not (5 > 3))

# 33. Print uppercase
print("hello".upper())

# 34. Print lowercase
print("HELLO".lower())

# 35. Print a string slice
print("Hello"[0:2])

# 36. Print the length of a string
print(len("Hello"))

# 37. Print type of data
print(type(3.14))

# 38. Print input value
name = input("Enter your name: ")
print("Hello, " + name)

# 39. Print a boolean conversion
print(bool(""))

# 40. Print an integer conversion
print(int("5"))

# 41. Print a float conversion
print(float("3.14"))

# 42. Print string concatenation
print("Cloud" + " " + "Support")

# 43. Print list creation
print(list("hello"))

# 44. Print a tuple
print((1, 2, 3))

# 45. Print a set
print(set("mississippi"))

# 46. Print elements of a list
languages = ["Python", "Java", "C++"]
print(languages[0])

# 47. Print elements of a dictionary
info = {"name": "Alice", "age": 25}
print(info["name"])

# 48. Print using a loop
for i in range(5):
    print("Count:", i)

# 49. Print with conditionals
x = 10
if x > 5:
    print("x is greater than 5")

# 50. Print a function result
def greet():
    return "Hello from function"
print(greet())

# 51. Print by calling a function with parameters
def greet(name):
    return f"Hello, {name}"
print(greet("Alice"))

# 52. Print multiple results in a loop
for i in range(3):
    print("Hello", i)

# 53. Print sum of two numbers
a, b = 5, 10
print("Sum:", a + b)

# 54. Print even numbers from 1 to 10
for i in range(1, 11):
    if i % 2 == 0:
        print("Even:", i)

# 55. Print elements of a nested list
matrix = [[1, 2], [3, 4]]
print(matrix[0][1])

# 56. Print using enumerate
for i, language in enumerate(languages):
    print(f"{i}: {language}")

# 57. Print characters of a string
for char in "Python":
    print(char)

# 58. Print multiplication table of 5
for i in range(1, 6):
    print(f"5 * {i} = {5 * i}")

# 59. Print countdown from 10 to 1
for i in range(10, 0, -1):
    print(i)

# 60. Print factorial of a number
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
print("Factorial of 5:", factorial(5))

# 61. Print elements in reversed order
fruits = ["apple", "banana", "cherry"]
print(fruits[::-1])

# 62. Print index of an element in a list
print(fruits.index("banana"))

# 63. Print sorted list
numbers = [4, 2, 9, 1]
print(sorted(numbers))

# 64. Print list with elements doubled
print([x * 2 for x in numbers])

# 65. Print list comprehension with condition
print([x for x in numbers if x % 2 == 0])

# 66. Print dictionary comprehension
squares = {x: x * x for x in range(5)}
print(squares)

# 67. Print using zip
names = ["Alice", "Bob", "Charlie"]
ages = [24, 25, 26]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# 68. Print sorted dictionary
print(sorted(squares.items()))

# 69. Print JSON string
import json
data = {"name": "Alice", "age": 25}
print(json.dumps(data))

# 70. Print the sum of list elements
print(sum(numbers))

# 71. Print reversed string
print("Python"[::-1])

# 72. Print maximum of a list
print(max(numbers))

# 73. Print minimum of a list
print(min(numbers))

# 74. Print type of variable
print(type(fruits))

# 75. Print hexadecimal value
print(hex(255))

# 76. Print binary value
print(bin(10))

# 77. Print ASCII character
print(chr(65))

# 78. Print ASCII code of a character
print(ord('A'))

# 79. Print all uppercase letters
import string
print(string.ascii_uppercase)

# 80. Print sorted list in descending order
print(sorted(numbers, reverse=True))

# 81. Print nested dictionary value
people = {"Alice": {"age": 25}}
print(people["Alice"]["age"])

# 82. Print a tuple of values
print((10, 20, 30))

# 83. Print file contents (if file exists)
# with open("file.txt") as file:
#     print(file.read())

# 84. Print string repeated
print("Python! " * 3)

# 85. Print list from 0 to 9
print(list(range(10)))

# 86. Print if a substring exists
print("Python" in "I love Python")

# 87. Print square of elements in list
print([x ** 2 for x in numbers])

# 88. Print each word in a sentence
sentence = "Python is awesome"
for word in sentence.split():
    print(word)

# 89. Print string center-aligned
print("Python".center(10))

# 90. Print string padded with zeroes
print("5".zfill(3))

# 91. Print capitalized string
print("hello world".capitalize())

# 92. Print total length of words in a list
print(sum(len(word) for word in sentence.split()))

# 93. Print sorted words in alphabetical order
print(sorted(sentence.split()))

# 94. Print list of even numbers
print([x for x in range(20) if x % 2 == 0])

# 95. Print cube of numbers from 1 to 5
print([x ** 3 for x in range(1, 6)])

# 96. Print square root of numbers in list
import math
print([math.sqrt(x) for x in range(1, 6)])

# 97. Print transpose of a matrix
matrix = [[1, 2, 3], [4, 5, 6]]
print(list(zip(*matrix)))

# 98. Print the count of a letter in a string
print("hello".count("l"))

# 99. Print concatenated strings with separator
words = ["Python", "is", "fun"]
print(" ".join(words))

# 100. Print average of a list
print(sum(numbers) / len(numbers))
