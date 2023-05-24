# Tuples
In Python, a tuple is an ordered, immutable collection of elements. Tuples are similar to lists, but the main difference is that tuples cannot be modified once they are created. They are created by enclosing comma-separated values within parentheses `()`.

Here are some examples of using tuples in Python:

```python
point = (3, 4)                            # Creating a tuple representing a 2D point
colors = ("red", "green", "blue")          # Creating a tuple of colors
mixed = (1, "apple", True, 3.14)           # Creating a tuple with mixed data types

print(point)                              # Output: (3, 4)
print(colors)                             # Output: ("red", "green", "blue")
print(mixed)                              # Output: (1, "apple", True, 3.14)

# Accessing tuple elements by index
print(point[0])                           # Output: 3
print(colors[2])                          # Output: "blue"
print(mixed[-1])                          # Output: 3.14

# Tuple packing and unpacking
name = "Alice"
age = 25
person = (name, age)                      # Packing values into a tuple
print(person)                            # Output: ("Alice", 25)

name, age = person                        # Unpacking values from a tuple
print(name)                              # Output: "Alice"
print(age)                               # Output: 25

# Immutable nature of tuples
# Trying to modify a tuple will raise a TypeError
point[0] = 5                             # Raises a TypeError: 'tuple' object does not support item assignment

# Tuple length and membership check
print(len(colors))                       # Output: 3
print("green" in colors)                 # Output: True

# Tuple concatenation and repetition
combined = point + colors                 # Concatenating two tuples
repeated = colors * 3                     # Repeating a tuple

# Iterating over a tuple
for element in mixed:
    print(element)

```

These examples showcase various operations and characteristics of tuples in Python. Tuples can be created, accessed by index, packed and unpacked, but they cannot be modified once created. Tuples can be concatenated, repeated, and iterated over.

Tuples are commonly used when you want to represent a collection of related but immutable values. They provide a way to group multiple values together while ensuring their immutability.