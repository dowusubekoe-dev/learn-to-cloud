# **Day 3: Strings**

## **Objective**

Learn to manipulate and process text data using Python strings.

### **Steps**:

Explore basic string operations like concatenation and slicing.
Use string methods to modify and analyze text.
Format strings using f-strings.

### **Brief Description**

Strings are sequences of characters used to store and manipulate text. Python provides several built-in methods and operations for processing strings, including formatting, slicing, and case conversion. This lesson will cover the essentials of working with text in Python.

### **Code Snippets**

**Defining Strings**:

```py
greeting = "Hello"
name = "Alice"
print(greeting + ", " + name + "!")
```

**String Concatenation with f-strings**:

```py
age = 25
print(f"My name is {name} and I am {age} years old.")
```

**Changing Case**:

```py
print(name.upper())  # ALICE
print(name.lower())  # alice
print(name.title())  # Alice
```

**Removing Whitespace**:

```py
text = "   Hello, Python!   "
print(text.strip())  # "Hello, Python!"
```

**String Slicing**:

```py
word = "Python"
print(word[:3])  # Pyt
print(word[-3:])  # hon
```

**Checking Substrings**:

```py
print("Py" in word)  # True
print("Java" not in word)  # True
```

**Splitting Strings**:

```py
sentence = "Python is fun"
words = sentence.split()
print(words)  # ['Python', 'is', 'fun']
```

**Joining Strings**:

```py
words = ["Learn", "Python", "Fast"]
print(" ".join(words))  # "Learn Python Fast"
```

**String Replacement**:

```py
text = "I love Java"
print(text.replace("Java", "Python"))  # I love Python
```

**String Length**:

```py
print(len(sentence))  # 13
```

### **Exercises**

1. Write a program that:

2. Defines a string with your full name.

3. Prints the name in uppercase, lowercase, and title case.

4. Given the string "Python programming is fun", extract and print the following:

      "Python"

      "programming"

      "fun"

5. Write a program to count the number of words in the sentence:

      "The quick brown fox jumps over the lazy dog."

6. Replace all occurrences of "cat" with "dog" in the string "The cat sat on the mat.".

7. Check if the word "Python" is in the sentence "Learning Python is great!". Print the result.
