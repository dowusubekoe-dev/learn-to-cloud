# **Day 7: List Access and Modification**


## **Objective**

Learn to modify lists using methods like sorting, reversing, and copying.


### **Steps**:

1. Use methods like sort() and reverse() to organize lists.
2. Create copies of lists to avoid unintended modifications.
3. Iterate through lists using loops.


### **Brief Description**

Python lists offer several methods to modify their content. You can sort, reverse, and copy lists to suit your needs. Today, you'll also explore iterating through lists using loops.


### **Code Snippets**

**Sorting a List**:

```py
numbers = [3, 1, 4, 1, 5, 9]
numbers.sort()
print(numbers)  # [1, 1, 3, 4, 5, 9]
```

**Reversing a List**:

```py
numbers.reverse()
print(numbers)  # [9, 5, 4, 3, 1, 1]
```

**Using sorted()**:

```py
unsorted = [6, 2, 8, 4]
print(sorted(unsorted))  # [2, 4, 6, 8]
print(unsorted)  # [6, 2, 8, 4] (unchanged)
```

**Copying a List**:

```py
original = [1, 2, 3]
copied = original[:]
copied.append(4)
print(original)  # [1, 2, 3]
print(copied)  # [1, 2, 3, 4]
```

**Iterating Through a List**:

```py
for num in numbers:
    print(num)
```

**Finding the Maximum Value**:

```py
print(max(numbers))  # 9
```

**Finding the Minimum Value**:

```py
print(min(numbers))  # 1
```

**Calculating the Sum**:

```py
print(sum(numbers))  # 23
```

**Combining Two Lists**:

```py
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(combined)  # [1, 2, 3, 4, 5, 6]
```

**Clearing a List**:

```py
numbers.clear()
print(numbers)  # []
```


### **Exercises**

1. Create a list of numbers and:

      - Sort the list in ascending and descending order.
      - Reverse the list.

2. Write a program that:

3. Combines two lists.

      - Creates a sorted copy of the combined list.
      - Iterate through a list of cities and print a message for each city:

```py
cities = ["New York", "London", "Paris"]
for city in cities:
    print(f"I want to visit {city}.")
```

4. Find the maximum, minimum, and sum of a list of numbers.

5. Write a program that:

      - Copies a list of favorite foods.
      - Adds a new item to the copy.
      - Confirms the original list is unchanged.
