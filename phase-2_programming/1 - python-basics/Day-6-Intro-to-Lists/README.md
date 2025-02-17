# **Day 6: Introduction to Lists**


## **Objective**

Understand Python lists, their properties, and basic operations to store and manipulate collections of data.


### **Steps**:

1. Define and initialize lists.
2. Access list elements using indices.
3. Modify, add, and remove elements from lists.


### **Brief Description**

Lists are ordered collections of items in Python, used to store multiple values in a single variable. This lesson will cover creating lists, accessing individual items, and using basic list methods for modification.


### **Code Snippets**

**Defining a List**:

```py
fruits = ["apple", "banana", "cherry"]
print(fruits)
```

**Accessing List Elements**:

```py
Copy code
print(fruits[0])  # apple
print(fruits[-1])  # cherry
```

**Modifying List Elements**:

```py
fruits[1] = "blueberry"
print(fruits)  # ['apple', 'blueberry', 'cherry']
```

**Adding Elements**:

```py
fruits.append("date")
print(fruits)  # ['apple', 'blueberry', 'cherry', 'date']
```

**Inserting Elements**:

```py
fruits.insert(1, "mango")
print(fruits)  # ['apple', 'mango', 'blueberry', 'cherry', 'date']
```

**Removing Elements**:

```py
fruits.remove("mango")
print(fruits)  # ['apple', 'blueberry', 'cherry', 'date']
```

**Using pop()**:

```py
last_fruit = fruits.pop()
print(last_fruit)  # date
print(fruits)  # ['apple', 'blueberry', 'cherry']
```

**Slicing Lists**:

```py
print(fruits[0:2])  # ['apple', 'blueberry']
```

**Checking List Length**:

```py
print(len(fruits))  # 3
```

**Using in to Check Membership**:

```py
print("apple" in fruits)  # True
print("mango" in fruits)  # False
```


### **Exercises**

1. Create a list of your favorite movies and print the first and last movies in the list.

2. Add two more movies to your list and then remove one of them.

3. Write a program to store the names of three friends in a list and print a message for each friend, such as:

```py
friends = ["Alice", "Bob", "Charlie"]
for friend in friends:
    print(f"Hello, {friend}! How are you?")
```

4. Create a list of numbers and print:

    - The entire list.
    - The first three numbers.
    - The last two numbers.
    
5. Check if the number 5 is in your list of numbers and print an appropriate message.