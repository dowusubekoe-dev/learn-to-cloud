Here's a comprehensive list of 100 simple Python scripts covering each of the requested concepts for a beginner Cloud Support Engineer. The examples progress from the very basics to slightly more complex applications to help build foundational Python skills.

---

### **Basic Data Types and Variables**

1. **Define integers, floats, and strings.**
    ```python
    age = 25
    height = 5.9
    name = "John"
    ```

2. **Define a boolean variable.**
    ```python
    is_cloud_engineer = True
    ```

3. **Print the types of different variables.**
    ```python
    print(type(age), type(height), type(name), type(is_cloud_engineer))
    ```

4. **Assign and print multiple variables on a single line.**
    ```python
    x, y, z = 5, 10, 15
    print(x, y, z)
    ```

5. **Create a list of AWS services.**
    ```python
    aws_services = ["EC2", "S3", "Lambda"]
    ```

6. **Create a dictionary with a few key-value pairs.**
    ```python
    cloud_providers = {"AWS": "Amazon", "Azure": "Microsoft", "GCP": "Google"}
    ```

7. **Access a dictionary value by its key.**
    ```python
    print(cloud_providers["AWS"])
    ```

8. **Update a value in a dictionary.**
    ```python
    cloud_providers["AWS"] = "Amazon Web Services"
    ```

9. **Define a set of cloud environments.**
    ```python
    environments = {"dev", "test", "prod"}
    ```

10. **Add and remove items from a set.**
    ```python
    environments.add("staging")
    environments.remove("test")
    ```

11. **Convert between data types (int to float, str to int, etc.).**
    ```python
    number = 10
    float_number = float(number)
    ```

12. **Check if an item is in a list.**
    ```python
    print("S3" in aws_services)
    ```

13. **Concatenate two lists.**
    ```python
    other_services = ["DynamoDB", "ECS"]
    all_services = aws_services + other_services
    ```

14. **Create a tuple of immutable items.**
    ```python
    regions = ("us-east-1", "us-west-2")
    ```

15. **Unpack values from a tuple.**
    ```python
    region1, region2 = regions
    ```

16. **Create a variable with `None` as its value.**
    ```python
    no_value = None
    ```

17. **Update a variable’s value and print it.**
    ```python
    no_value = "Now has a value"
    ```

18. **Use the `len()` function to count items in a list.**
    ```python
    print(len(aws_services))
    ```

19. **Check if a dictionary has a specific key.**
    ```python
    print("AWS" in cloud_providers)
    ```

20. **Copy a list to another variable.**
    ```python
    services_copy = aws_services.copy()
    ```

---

### **Simple I/O Operations**

21. **Print a welcome message.**
    ```python
    print("Welcome to Cloud Support Training!")
    ```

22. **Ask for a user’s name and print it.**
    ```python
    name = input("Enter your name: ")
    print("Hello, " + name)
    ```

23. **Read an integer from the user and double it.**
    ```python
    num = int(input("Enter a number: "))
    print("Double:", num * 2)
    ```

24. **Take a floating-point input and square it.**
    ```python
    num = float(input("Enter a decimal number: "))
    print("Square:", num ** 2)
    ```

25. **Prompt the user to enter multiple values.**
    ```python
    region = input("Enter the region: ")
    service = input("Enter the AWS service: ")
    print(f"Region: {region}, Service: {service}")
    ```

26. **Ask for two numbers and add them.**
    ```python
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("Sum:", num1 + num2)
    ```

27. **Write output to a file.**
    ```python
    with open("output.txt", "w") as file:
        file.write("Hello, Cloud Engineer!")
    ```

28. **Read input from a file.**
    ```python
    with open("output.txt", "r") as file:
        content = file.read()
    print(content)
    ```

29. **Append data to an existing file.**
    ```python
    with open("output.txt", "a") as file:
        file.write("\nWelcome to Python!")
    ```

30. **Check if a file exists before reading.**
    ```python
    import os
    if os.path.exists("output.txt"):
        with open("output.txt", "r") as file:
            print(file.read())
    ```

31. **Print the length of user input.**
    ```python
    user_input = input("Enter a message: ")
    print("Length of input:", len(user_input))
    ```

32. **Ask the user for a list of AWS services.**
    ```python
    services = input("Enter AWS services separated by commas: ").split(',')
    print(services)
    ```

33. **Check if input is numeric.**
    ```python
    user_input = input("Enter a value: ")
    print(user_input.isdigit())
    ```

34. **Print each character of a string entered by the user.**
    ```python
    text = input("Enter text: ")
    for char in text:
        print(char)
    ```

35. **Count the number of words in user input.**
    ```python
    words = input("Enter a sentence: ").split()
    print("Word count:", len(words))
    ```

36. **Convert input to uppercase.**
    ```python
    text = input("Enter text: ")
    print(text.upper())
    ```

37. **Reverse the input text.**
    ```python
    text = input("Enter text: ")
    print(text[::-1])
    ```

38. **Replace characters in user input.**
    ```python
    text = input("Enter text: ")
    print(text.replace("a", "@"))
    ```

39. **Print every other character in input text.**
    ```python
    text = input("Enter text: ")
    print(text[::2])
    ```

40. **Convert the input text to a list of characters.**
    ```python
    text = input("Enter text: ")
    print(list(text))
    ```

---

### **Comments and Documentation**

41. **Single-line comment.**
    ```python
    # This is a single-line comment
    ```

42. **Multi-line comment with triple quotes.**
    ```python
    """
    This is a multi-line comment.
    Used for documentation.
    """
    ```

43. **Document a function using docstrings.**
    ```python
    def add(a, b):
        """This function returns the sum of two numbers."""
        return a + b
    ```

---


### **Basic Mathematical Operations**

61. **Add two numbers.**
    ```python
    x = 5
    y = 3
    result = x + y
    print("Sum:", result)
    ```

62. **Subtract two numbers.**
    ```python
    result = x - y
    print("Difference:", result)
    ```

63. **Multiply two numbers.**
    ```python
    result = x * y
    print("Product:", result)
    ```

64. **Divide two numbers.**
    ```python
    result = x / y
    print("Quotient:", result)
    ```

65. **Perform integer division.**
    ```python
    result = x // y
    print("Integer Quotient:", result)
    ```

66. **Find the remainder using modulo.**
    ```python
    result = x % y
    print("Remainder:", result)
    ```

67. **Raise a number to a power.**
    ```python
    result = x ** y
    print("Exponent:", result)
    ```

68. **Find the square root of a number.**
    ```python
    import math
    result = math.sqrt(16)
    print("Square root:", result)
    ```

69. **Calculate the absolute value of a number.**
    ```python
    result = abs(-10)
    print("Absolute value:", result)
    ```

70. **Round a number to the nearest integer.**
    ```python
    result = round(4.56)
    print("Rounded:", result)
    ```

71. **Use `math.ceil()` to round up.**
    ```python
    result = math.ceil(4.1)
    print("Rounded up:", result)
    ```

72. **Use `math.floor()` to round down.**
    ```python
    result = math.floor(4.9)
    print("Rounded down:", result)
    ```

73. **Calculate the maximum of two numbers.**
    ```python
    print(max(10, 20))
    ```

74. **Calculate the minimum of two numbers.**
    ```python
    print(min(10, 20))
    ```

75. **Calculate the sum of a list of numbers.**
    ```python
    numbers = [1, 2, 3, 4]
    print(sum(numbers))
    ```

76. **Convert degrees to radians.**
    ```python
    degrees = 90
    radians = math.radians(degrees)
    print("Radians:", radians)
    ```

77. **Convert radians to degrees.**
    ```python
    rad = math.pi
    degrees = math.degrees(rad)
    print("Degrees:", degrees)
    ```

78. **Calculate the logarithm (base 10) of a number.**
    ```python
    result = math.log10(100)
    print("Logarithm base 10:", result)
    ```

79. **Calculate the natural logarithm (base e) of a number.**
    ```python
    result = math.log(10)
    print("Natural Logarithm:", result)
    ```

80. **Calculate the sine of an angle in radians.**
    ```python
    angle = math.pi / 2  # 90 degrees
    result = math.sin(angle)
    print("Sine:", result)
    ```

---

### **String Formatting**

81. **Format a string using the `+` operator.**
    ```python
    name = "Alice"
    print("Hello, " + name + "!")
    ```

82. **Format a string using f-strings.**
    ```python
    age = 30
    print(f"{name} is {age} years old.")
    ```

83. **Format a string using `.format()`.**
    ```python
    print("My name is {} and I am {} years old.".format(name, age))
    ```

84. **Format multiple values with `.format()`.**
    ```python
    city, country = "Seattle", "USA"
    print("I live in {}, {}.".format(city, country))
    ```

85. **Align text to the left using f-strings.**
    ```python
    print(f"{name:<10} is learning Python.")
    ```

86. **Align text to the right using f-strings.**
    ```python
    print(f"{name:>10} is learning Python.")
    ```

87. **Center text using f-strings.**
    ```python
    print(f"{name:^10} is learning Python.")
    ```

88. **Format numbers with two decimal places.**
    ```python
    pi = 3.14159265
    print(f"Pi to 2 decimal places: {pi:.2f}")
    ```

89. **Pad a number with zeros using `.zfill()`.**
    ```python
    number = 42
    print(str(number).zfill(5))
    ```

90. **Display a percentage.**
    ```python
    score = 0.85
    print(f"Score: {score:.0%}")
    ```

91. **Format a number as currency.**
    ```python
    price = 49.99
    print(f"Price: ${price:.2f}")
    ```

92. **Format scientific notation.**
    ```python
    large_number = 123456789
    print(f"{large_number:.2e}")
    ```

93. **Capitalize the first letter of each word.**
    ```python
    text = "python programming"
    print(text.title())
    ```

94. **Uppercase all letters.**
    ```python
    print(text.upper())
    ```

95. **Lowercase all letters.**
    ```python
    print(text.lower())
    ```

96. **Strip whitespace from a string.**
    ```python
    text_with_space = "   Hello World   "
    print(text_with_space.strip())
    ```

97. **Format numbers with comma separators.**
    ```python
    large_number = 1000000
    print(f"{large_number:,}")
    ```

98. **Format hex, octal, and binary values.**
    ```python
    number = 255
    print(f"Hex: {number:x}, Octal: {number:o}, Binary: {number:b}")
    ```

99. **Replace text within a formatted string.**
    ```python
    text = "AWS is the best cloud provider."
    print(text.replace("AWS", "Azure"))
    ```

100. **Insert variables into a multi-line formatted string.**
    ```python
    service, region = "S3", "us-west-1"
    info = f"""
    Service: {service}
    Region: {region}
    """
    print(info)
    ```

---
