# Indices may also be negative numbers

word = 'Python'
#Indexing is used to obtain individual character
word[-1]  # last character
print(word[-1])

word[-2]  # second-last character
print(word[-2])

word[-6]
print(word[-6])

# Note that since -0 is the same as 0, negative indices start from -1.

# Slicing is also supported and allows you to obtain substring.

word[0:2] # characters from position 0 (included) to 2 (excluded)
print(word[0:2])

word[2:5]  # characters from position 2 (included) to 5 (excluded)
print(word[2:5])
